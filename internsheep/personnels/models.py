# -*- encoding: utf-8 -*-

from flask import g, flash
from psycopg2.extras import DictCursor, NamedTupleCursor

from collections import OrderedDict

from ..geo.models import *
from ..organisations.models import *
from ..stages.models import *


def sanitize_fetched_data(l):
    lout = []
    for d in l:
        dout = OrderedDict()
        din = d._asdict()
        for k, v in din.items():
            new_k = k.split('.')[-1]
            if type(din[k]) in (str, unicode):
                dout[new_k] = unicode(din[k].decode('utf-8').strip())
            else:
                dout[new_k] = din[k]
        if dout:
            lout.append(dout)
    return lout

################################################################################
# Personnes
################################################################################


def create_personne(cursor=None, **kwargs):
    sql_cmd = u"""\
        INSERT INTO personnes(nom, prenom, adresse_mail, numero_telephone)
        VALUES (%(nom)s , %(prenom)s , %(adresse_mail)s, %(numero_telephone)s)
        RETURNING personne_id
        ;"""
    print kwargs
    if cursor:
        cursor.execute(sql_cmd, kwargs)
        _id = cursor.fetchone()[0]
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            _id = cur.fetchone()[0]
            g.db.commit()
    return _id


def list_personnes():
    sql_cmd = u"""\
        SELECT personne_id, nom, prenom, adresse_mail, numero_telephone
        FROM personnes
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall


def get_personne(_id):
    sql_cmd = u"""\
        SELECT *
        FROM personnes
        WHERE personne_id = %(personne_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'personne_id': _id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None


def update_personne(_id, cursor=None, **kwargs):
    sql_cmd = u"""\
        UPDATE personnes SET
        nom = %(nom)s,
        prenom = %(prenom)s,
        adresse_mail = %(adresse_mail)s,
        numero_telephone = %(numero_telephone)s
        WHERE personne_id = %(personne_id)s
        ;"""
    print kwargs
    kwargs.update({'personne_id': _id})
    print kwargs
    if cursor:
        cursor.execute(sql_cmd, kwargs)
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            g.db.commit()


def delete_personne(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM personnes
        WHERE personne_id = %(personne_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'personne_id': _id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'personne_id': _id})
            g.db.commit()

################################################################################
# Eleves
################################################################################


def create_eleve(**kwargs):
    sql_cmd = u"""\
        INSERT INTO eleves(annee, departement, personne_id, adresse_id)
        VALUES (%(annee)s , %(departement)s, %(personne_id)s, %(adresse_id)s)
        RETURNING eleve_id
        ;"""
    with g.db.cursor() as cur:
        personne_id = create_personne(cursor=cur, **kwargs)
        adresse_id = create_adresse(cursor=cur, **kwargs)
        kwargs.update({'personne_id': personne_id, 'adresse_id': adresse_id})
        cur.execute(sql_cmd, kwargs)
        _id = cur.fetchone()[0]
        g.db.commit()
    return _id

def list_eleves():
    sql_cmd = u"""\
        SELECT eleve_id, nom AS nom_eleve, prenom, adresse_mail, numero_telephone, annee, departement, ville, code_postal, adresse
        FROM eleves
        JOIN personnes ON personnes.personne_id = eleves.personne_id
        JOIN adresses ON adresses.adresse_id = eleves.adresse_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def list_eleves_non_affectes():
    sql_cmd = u"""\
        SELECT eleves.eleve_id AS eleve_id, nom AS nom_eleve, prenom, adresse_mail, numero_telephone, annee, departement, ville, code_postal, adresse
        FROM eleves
        JOIN personnes ON personnes.personne_id = eleves.personne_id
        JOIN adresses ON adresses.adresse_id = eleves.adresse_id
        LEFT JOIN affectations ON affectations.eleve_id = eleves.eleve_id
        WHERE affectations.eleve_id IS NULL
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def get_eleve(_id, cursor=None):
    sql_cmd = u"""\
        SELECT personnes.personne_id, eleve_id, adresses.adresse_id, nom, prenom, adresse_mail, numero_telephone, annee, departement, ville, code_postal, adresse
        FROM eleves
        JOIN personnes ON personnes.personne_id = eleves.personne_id
        JOIN adresses ON adresses.adresse_id = eleves.adresse_id
        WHERE eleve_id = %(eleve_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'eleve_id': _id})
        listall = cursor.fetchall()
        return listall
    else:
        with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute(sql_cmd, {'eleve_id': _id})
            listall = cur.fetchall()
        if listall:
            listall = sanitize_fetched_data(listall)
            assert len(listall) == 1
            return listall[0]
        else:
            return None

##
def str_eleve(_id):
    e = get_eleve(_id)
    if e:
        return u'Eleve: {} {} de {}({}) {}/{}'.format(
            e['prenom'], e['nom'], e['ville'], e['code_postal'], e['departement'], e['annee'])
    else:
        return u'None'

def update_eleve(_id, **kwargs):
    sql_cmd = u"""\
        UPDATE eleves SET
        annee = %(annee)s,
        departement = %(departement)s
        WHERE eleve_id = %(eleve_id)s
        RETURNING personne_id, adresse_id
        ;"""
    kwargs.update({'eleve_id': _id})
    print "kwargs: ", kwargs
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        personne_id, adresse_id = cur.fetchone()
        print "_id, personne_id, adresse_id :", _id, personne_id, adresse_id
        update_personne(personne_id, cursor=cur, **kwargs)
        update_adresse(adresse_id, cursor=cur, **kwargs)
        print get_eleve(_id, cursor=cur)
        g.db.commit()

def delete_eleve(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM eleves
        WHERE eleve_id = %(eleve_id)s
        ;"""
    if cursor:
        eleve = get_eleve(_id, cursor=cursor)
        delete_consultations_eleve(_id, cursor=cursor)
        delete_affectation_eleve(_id, cursor=cursor)
        cursor.execute(sql_cmd, {'eleve_id': _id})
        delete_adresse(eleve[0][2], cursor=cursor)
        delete_personne(eleve[0][0], cursor=cursor)
    else:
        with g.db.cursor() as cur:
            eleve = get_eleve(_id, cursor=cur)
            delete_consultations_eleve(_id, cursor=cur)
            delete_affectation_eleve(_id, cursor=cur)
            cur.execute(sql_cmd, {'eleve_id': _id})
            delete_adresse(eleve[0][2], cursor=cur)
            delete_personne(eleve[0][0], cursor=cur)
            g.db.commit()


################################################################################
# Contacts
################################################################################


def create_contact(**kwargs):
    sql_cmd = u"""\
        INSERT INTO contacts(fonction, personne_id, entreprise_id)
        VALUES (%(fonction)s, %(personne_id)s, %(entreprise_id)s)
        RETURNING contact_id
        ;"""
    with g.db.cursor() as cur:
        personne_id = create_personne(cursor=cur, **kwargs)
        kwargs.update({'personne_id': personne_id})
        cur.execute(sql_cmd, kwargs)
        _id = cur.fetchone()[0]
        g.db.commit()
    return _id

def list_contacts():
    sql_cmd = u"""\
        SELECT contact_id, nom AS nom_contact, prenom, adresse_mail, personnes.numero_telephone, fonction, nom_entreprise
        FROM contacts
        JOIN personnes ON personnes.personne_id = contacts.personne_id
        JOIN entreprises ON entreprises.entreprise_id = contacts.entreprise_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def get_contact(_id, cursor=None):
    sql_cmd = u"""\
        SELECT personnes.personne_id, contact_id, adresses.adresse_id, nom, prenom, personnes.adresse_mail, personnes.numero_telephone, fonction, nom_entreprise, ville, code_postal, adresse
        FROM contacts
        JOIN personnes ON personnes.personne_id = contacts.personne_id
        JOIN entreprises ON entreprises.entreprise_id = contacts.entreprise_id
        JOIN adresses ON adresses.adresse_id = entreprises.adresse_id
        WHERE contact_id = %(contact_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'contact_id': _id})
        listall = cursor.fetchall()
        return listall
    else:
        with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute(sql_cmd, {'contact_id': _id})
            listall = cur.fetchall()
        if listall:
            listall = sanitize_fetched_data(listall)
            assert len(listall) == 1
            return listall[0]
        else:
            return None

##
def str_contact(_id):
    e = get_contact(_id)
    print e
    if e:
        return u'Contact: {} {} de {} à {}({})'.format(
            e['prenom'], e['nom'], e['ville'], e['code_postal'], e['nom_entreprise'])
    else:
        return u'None'

def update_contact(_id, **kwargs):
    sql_cmd = u"""\
        UPDATE contacts SET
        fonction = %(fonction)s,
        entreprise_id = %(entreprise_id)s
        WHERE contact_id = %(contact_id)s
        RETURNING personne_id, entreprise_id
        ;"""
    kwargs.update({'contact_id': _id})
    print "kwargs: ", kwargs
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        personne_id, entreprise_id = cur.fetchone()
        print "_id, personne_id, entreprise_id :", _id, personne_id, entreprise_id
        update_personne(personne_id, cursor=cur, **kwargs)
        print get_contact(_id, cursor=cur)
        g.db.commit()

def delete_contact(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM contacts
        WHERE contact_id = %(contact_id)s
        ;"""
    if cursor:
        contact = get_contact(_id, cursor=cursor)
        delete_consultations_eleve(_id, cursor=cursor)
        delete_affectation_eleve(_id, cursor=cursor)

        cursor.execute("SELECT proposition_id FROM propositions_stage WHERE contact_id = %(contact_id)s", {'contact_id': _id})
        for proposition_id in cursor.fetchall():
            delete_proposition(proposition_id[0], cursor=cursor)

        cursor.execute(sql_cmd, {'contact_id': _id})
        delete_adresse(contact[0][2], cursor=cursor)
        delete_personne(contact[0][0], cursor=cursor)
    else:
        with g.db.cursor() as cur:
            contact = get_contact(_id, cursor=cur)
            delete_consultations_eleve(_id, cursor=cur)
            delete_affectation_eleve(_id, cursor=cur)

            cur.execute("SELECT proposition_id FROM propositions_stage WHERE contact_id = %(contact_id)s", {'contact_id': _id})
            for proposition_id in cur.fetchall():
                delete_proposition(proposition_id[0], cursor=cur)

            cur.execute(sql_cmd, {'contact_id': _id})
            delete_personne(contact[0][0], cursor=cur)
            g.db.commit()

################################################################################
# Responsable
################################################################################


def create_responsable(**kwargs):
    sql_cmd = u"""\
        INSERT INTO responsables_pedagogiques(personne_id)
        VALUES (%(personne_id)s)
        RETURNING responsable_id
        ;"""
    with g.db.cursor() as cur:
        personne_id = create_personne(cursor=cur, **kwargs)
        kwargs.update({'personne_id': personne_id})
        cur.execute(sql_cmd, kwargs)
        _id = cur.fetchone()[0]
        g.db.commit()
    return _id

def list_responsables():
    sql_cmd = u"""\
        SELECT responsable_id, nom AS nom_responsable, prenom, adresse_mail, numero_telephone
        FROM responsables_pedagogiques
        JOIN personnes ON personnes.personne_id = responsables_pedagogiques.personne_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def get_responsable(_id, cursor=None):
    sql_cmd = u"""\
        SELECT personnes.personne_id, responsable_id, nom, prenom, adresse_mail, numero_telephone
        FROM responsables_pedagogiques
        JOIN personnes ON personnes.personne_id = responsables_pedagogiques.personne_id
        WHERE responsable_id = %(responsable_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'responsable_id': _id})
        listall = cursor.fetchall()
        return listall
    else:
        with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute(sql_cmd, {'responsable_id': _id})
            listall = cur.fetchall()
        if listall:
            listall = sanitize_fetched_data(listall)
            assert len(listall) == 1
            return listall[0]
        else:
            return None


def str_responsable(_id):
    e = get_responsable(_id)
    if e:
        return u'Responsable: {} '.format(e['prenom'], e['nom'])
    else:
        return u'None'

def update_responsable(_id, **kwargs):
    sql_cmd = u"""\
        SELECT personne_id
        FROM responsables_pedagogiques
        WHERE responsable_id = %(responsable_id)s
        ;"""
    kwargs.update({'responsable_id': _id})
    print "kwargs: ", kwargs
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        personne_id = cur.fetchone()[0]
        print "_id, personne_id :", _id, personne_id
        update_personne(personne_id, cursor=cur, **kwargs)
        print get_responsable(_id, cursor=cur)
        g.db.commit()

def delete_responsable(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM responsables_pedagogiques
        WHERE responsable_id = %(responsable_id)s
        ;"""
    if cursor:
        responsable = get_responsable(_id, cursor=cursor)
        delete_affectation_responsable(_id, cursor=cursor)
        cursor.execute(sql_cmd, {'responsable_id': _id})
        delete_personne(responsable[0][0], cursor=cursor)
    else:
        with g.db.cursor() as cur:
            responsable = get_responsable(_id, cursor=cur)
            delete_affectation_responsable(_id, cursor=cur)
            cur.execute(sql_cmd, {'responsable_id': _id})
            delete_personne(responsable[0][0], cursor=cur)
            g.db.commit()
