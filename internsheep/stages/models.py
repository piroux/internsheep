# -*- encoding: utf-8 -*-

from flask import g, flash
from psycopg2.extras import DictCursor, NamedTupleCursor

from collections import OrderedDict

from ..geo.models import *

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
# Affectations
################################################################################


def create_affectation(cursor=None, **kwargs):
    sql_cmd = u"""\
        INSERT INTO affectations(eleve_id, responsable_id, proposition_id)
        VALUES (%(eleve_id)s , %(responsable_id)s , %(proposition_id)s)
        RETURNING proposition_id
        ;"""
    if cursor:
        cursor.execute(sql_cmd, kwargs)
        _id = cursor.fetchone()[0]
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            _id = cur.fetchone()[0]
            g.db.commit()
    return _id


def list_affectations():
    sql_cmd = u"""\
        SELECT eleve_id, responsable_id, proposition_id
        FROM affectations
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def get_affectation(_id):
    sql_cmd = u"""\
        SELECT *
        FROM affectations
        WHERE proposition_id = %(proposition_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'proposition_id': _id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None

def get_affectation_eleve(eleve_id):
    sql_cmd = u"""\
        SELECT *
        FROM affectations
        WHERE eleve_id = %(eleve_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'eleve_id': eleve_id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None


def update_affectation(_id, cursor=None, **kwargs):
    sql_cmd = u"""\
        UPDATE affectations SET
        responsable_id = %(responsable_id)s,
        eleve_id = %(eleve_id)s
        WHERE proposition_id = %(proposition_id)s
        RETURNING proposition_id
        ;"""
    kwargs.update({'proposition_id': _id})
    if cursor:
        cursor.execute(sql_cmd, kwargs)
        proposition_id = cursor.fetchone()
        if proposition_id:
            proposition_id = proposition_id[0]
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            g.db.commit()
            proposition_id = cursor.fetchone()
            if proposition_id:
                proposition_id = proposition_id[0]
    return proposition_id


def delete_affectation(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM affectations
        WHERE proposition_id = %(proposition_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'proposition_id': _id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'proposition_id': _id})
            g.db.commit()

def delete_affectation_eleve(eleve_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM affectations
        WHERE eleve_id = %(eleve_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'eleve_id': eleve_id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'eleve_id': eleve_id})
            g.db.commit()

def delete_affectation_responsable(responsable_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM affectations
        WHERE responsable_id = %(responsable_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'responsable_id': responsable_id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'responsable_id': responsable_id})
            g.db.commit()

################################################################################
# Consultations
################################################################################


def create_consultation(cursor=None, **kwargs):
    sql_cmd = u"""\
        INSERT INTO consultations(eleve_id, proposition_id)
        VALUES (%(eleve_id)s, %(proposition_id)s)
        RETURNING eleve_id, proposition_id
        ;"""
    if cursor:
        cursor.execute(sql_cmd, kwargs)
        _id = cursor.fetchone()[0]
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            _id = cur.fetchone()[0]
            g.db.commit()
    return _id


def list_consultations():
    sql_cmd = u"""\
        SELECT eleve_id, proposition_id
        FROM consultations
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall


def get_consultation(_id1, _id2):
    sql_cmd = u"""\
        SELECT *
        FROM consultations
        WHERE eleve_id = %(eleve_id)s AND proposition_id = %(proposition_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'eleve_id': _id1, 'proposition_id': _id2})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None


def update_consultation(_id1, _id2, cursor=None, **kwargs):
    pass


def delete_consultation(_id1, _id2, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM consultations
        WHERE eleve_id = %(eleve_id)s AND proposition_id = %(proposition_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'eleve_id': _id1, 'proposition_id': _id2})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'eleve_id': _id1, 'proposition_id': _id2})
            g.db.commit()


def delete_consultations_eleve(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM consultations
        WHERE eleve_id = %(eleve_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'eleve_id': _id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'eleve_id': _id})
            g.db.commit()

def delete_consultations_proposition(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM consultations
        WHERE proposition_id = %(proposition_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'proposition_id': _id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'proposition_id': _id})
            g.db.commit()

################################################################################
# Propositions
################################################################################


def create_proposition(**kwargs):
    sql_cmd = u"""\
        INSERT INTO propositions_stage(sujet, annee, domaine, groupe, date_debut, date_fin, indemnite, contact_id, adresse_id)
        VALUES (%(sujet)s, %(annee)s, %(domaine)s, %(groupe)s, %(date_debut)s, %(date_fin)s, %(indemnite)s, %(contact_id)s, %(adresse_id)s)
        RETURNING proposition_id
        ;"""
    print "create_proposition: START"
    with g.db.cursor() as cur:
        adresse_id = create_adresse(cursor=cur, **kwargs)
        kwargs.update({'adresse_id': adresse_id})
        cur.execute(sql_cmd, kwargs)
        proposition_id = cur.fetchone()[0]
        kwargs.update({'proposition_id': proposition_id})

        if ((kwargs['eleve_id'] == 0) and (kwargs['responsable_id'] != 0)) or ((kwargs['eleve_id'] != 0) and (kwargs['responsable_id'] == 0)):
            flash(u"Attention: Eleve et Responsable doivent aller de paire - Champs ignorés", 'danger')
        elif (kwargs['eleve_id'] != 0) and (kwargs['responsable_id'] != 0):
            create_affectation(cursor=cur, **kwargs)

        g.db.commit()
    print "create_proposition: END"
    return proposition_id


def list_propositions():
    sql_cmd = u"""\
        SELECT propositions_stage.proposition_id, sujet,
        CASE
            WHEN affectations.responsable_id IS NULL AND affectations.eleve_id IS NULL THEN 'En attente_primary'
            WHEN affectations.responsable_id IS NULL OR affectations.eleve_id IS NULL THEN 'En cours_warning'
            ELSE 'Affectée_default'
        END AS Affectation_tag,
        propositions_stage.annee, domaine, groupe, date_debut, date_fin, indemnite, ville, code_postal,
        concat_ws(' ', peleves.prenom, peleves.nom) AS eleve,
        concat_ws(' ', presponsables.prenom, presponsables.nom) AS responsable,
        concat_ws(' ', pcontacts.prenom, pcontacts.nom) AS contact
        FROM propositions_stage
        JOIN adresses ON adresses.adresse_id = propositions_stage.adresse_id
        JOIN contacts ON contacts.contact_id = propositions_stage.contact_id
        JOIN personnes pcontacts ON pcontacts.personne_id = contacts.personne_id
        LEFT JOIN affectations ON affectations.proposition_id = propositions_stage.proposition_id
        LEFT JOIN responsables_pedagogiques ON responsables_pedagogiques.responsable_id = affectations.responsable_id
        LEFT JOIN personnes presponsables ON presponsables.personne_id = responsables_pedagogiques.personne_id
        LEFT JOIN eleves ON eleves.eleve_id = affectations.eleve_id
        LEFT JOIN personnes peleves ON peleves.personne_id = eleves.personne_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall


def get_proposition(_id):
    sql_cmd = u"""\
        SELECT propositions_stage.*, adresses.adresse, adresses.ville, adresses.code_postal, affectations.eleve_id, affectations.responsable_id
        FROM propositions_stage
        JOIN adresses ON adresses.adresse_id = propositions_stage.adresse_id
        LEFT JOIN affectations ON affectations.proposition_id = propositions_stage.proposition_id
        WHERE propositions_stage.proposition_id = %(proposition_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'proposition_id': _id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None

def update_proposition(_id, cursor=None, **kwargs):
    sql_cmd = u"""\
        UPDATE propositions_stage SET
        sujet = %(sujet)s,
        annee = %(annee)s,
        domaine = %(domaine)s,
        groupe = %(groupe)s,
        date_debut = %(date_debut)s,
        date_fin = %(date_fin)s,
        indemnite = %(indemnite)s,
        contact_id = %(contact_id)s
        WHERE proposition_id = %(proposition_id)s
        RETURNING adresse_id
        ;"""
    print "update_proposition: START"
    with g.db.cursor() as cur:
        kwargs.update({'proposition_id': _id})
        cur.execute(sql_cmd, kwargs)
        adresse_id = cur.fetchone()[0]
        kwargs.update({'adresse_id': adresse_id})
        update_adresse(adresse_id, cursor=cur, **kwargs)

        if ((kwargs['eleve_id'] == 0) and (kwargs['responsable_id'] != 0)) or ((kwargs['eleve_id'] != 0) and (kwargs['responsable_id'] == 0)):
            flash(u"Attention: Eleve et Responsable doivent aller de paire. Changements ignorés pour ces champs", 'danger')
        else:
            old_affectation = get_affectation(_id)
            new_affectation = get_affectation_eleve(kwargs['eleve_id'])
            if old_affectation and new_affectation:
                update_affectation(_id, cursor=cur, **kwargs)
            elif old_affectation and not new_affectation:
                delete_affectation(_id, cursor=cur)
            elif not old_affectation and not new_affectation:
                create_affectation(cursor=cur, **kwargs)
        """
        success_update_affectation = update_affectation(_id, cursor=cur, **kwargs)
        if not success_update_affectation:
            create_affectation(cursor=cur, **kwargs)
        """
        g.db.commit()
    print "update_proposition: END"
    return _id


def delete_proposition(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM propositions_stage
        WHERE proposition_id = %(proposition_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'proposition_id': _id})
    else:
        with g.db.cursor() as cur:
            proposition = get_proposition(_id)
            delete_consultations_proposition(proposition['proposition_id'], cursor=cur)
            delete_affectation(proposition['proposition_id'], cursor=cur)
            cur.execute(sql_cmd, {'proposition_id': _id})
            delete_adresse(proposition['adresse_id'], cursor=cur)
            g.db.commit()
