# -*- encoding: utf-8 -*-

from flask import g
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
# Entreprises
################################################################################


def create_entreprise(**kwargs):
    sql_cmd = u"""\
        INSERT INTO entreprises(nom_entreprise, numero_telephone, site_web, type_entreprise, nombre_salarie, adresse_id)
        VALUES (%(nom_entreprise)s , %(numero_telephone)s , %(site_web)s, %(type_entreprise)s, %(nombre_salarie)s, %(adresse_id)s)
        ;"""
    kwargs['adresse_id'] = create_adresse(**kwargs)
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        g.db.commit()


def list_entreprises():
    sql_cmd = u"""\
        SELECT entreprise_id, nom_entreprise, type_entreprise, nombre_salarie, adresse, ville, numero_telephone, site_web
        FROM entreprises
        JOIN adresses ON adresses.adresse_id = entreprises.adresse_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall


def get_entreprise(_id):
    sql_cmd = u"""\
        SELECT entreprises.*, adresses.ville, adresses.code_postal, adresses.adresse
        FROM entreprises
        JOIN adresses ON adresses.adresse_id = entreprises.adresse_id
        WHERE entreprise_id = %(entreprise_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'entreprise_id': _id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None

def str_entreprise(_id):
    e = get_entreprise(_id)
    if e:
        return u'Entreprise: {} à {}'.format(e['nom_entreprise'], e['ville'])
    else:
        return u'None'

def update_entreprise(_id, **kwargs):
    sql_cmd = u"""\
        UPDATE entreprises SET
        nom_entreprise = %(nom_entreprise)s,
        numero_telephone = %(numero_telephone)s,
        site_web = %(site_web)s,
        type_entreprise = %(type_entreprise)s,
        nombre_salarie = %(nombre_salarie)s
        WHERE entreprise_id = %(entreprise_id)s
        RETURNING adresse_id
        ;"""
    kwargs.update({'entreprise_id': _id})
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        adresse_id = cur.fetchone()[0]
        update_adresse(adresse_id, **kwargs)
        update_secteurs_entreprise(_id, kwargs['secteurs'])
        g.db.commit()



def delete_entreprise(_id, cursor=None):
    pass


################################################################################
# Secteurs
################################################################################


def create_secteur(**kwargs):
    sql_cmd = u"""\
        INSERT INTO secteurs(nom_secteur)
        VALUES (%(nom_secteur)s)
        ;"""
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        g.db.commit()


def list_secteurs():
    sql_cmd = u"""\
        SELECT secteur_id, nom_secteur
        FROM secteurs
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall

def list_aggregate_entreprises_secteurs():
    sql_cmd = u"""\
        SELECT entreprises.entreprise_id, secteurs.secteur_id, secteurs.nom_secteur
        FROM secteurs
        JOIN appartient ON appartient.secteur_id = secteurs.secteur_id
        JOIN entreprises ON entreprises.entreprise_id = appartient.entreprise_id
        ORDER BY entreprises.entreprise_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    listagg = {}
    for el in listall:
        if el['entreprise_id'] in listagg:
            listagg[el['entreprise_id']].append({'secteur_id': el['secteur_id'], 'nom_secteur': el['nom_secteur']})
        else:
            listagg[el['entreprise_id']] = [{'secteur_id': el['secteur_id'], 'nom_secteur': el['nom_secteur']}]
    return listagg


def list_aggregate_secteurs_entreprises():
    sql_cmd = u"""\
        SELECT secteurs.secteur_id, entreprises.entreprise_id, entreprises.nom_entreprise
        FROM secteurs
        JOIN appartient ON appartient.secteur_id = secteurs.secteur_id
        JOIN entreprises ON entreprises.entreprise_id = appartient.entreprise_id
        ORDER BY secteurs.secteur_id
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    listagg = {}
    for el in listall:
        if el['secteur_id'] in listagg:
            listagg[el['secteur_id']].append({'entreprise_id': el['entreprise_id'], 'nom_entreprise': el['nom_entreprise']})
        else:
            listagg[el['secteur_id']] = [{'entreprise_id': el['entreprise_id'], 'nom_entreprise': el['nom_entreprise']}]
    return listagg


def get_secteur(_id):
    sql_cmd = u"""\
        SELECT *
        FROM secteurs
        WHERE secteur_id = %(secteur_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'secteur_id': _id})
        listall = cur.fetchall()
    if listall:
        listall = sanitize_fetched_data(listall)
        assert len(listall) == 1
        return listall[0]
    else:
        return None


def update_secteur(_id, **kwargs):
    sql_cmd = u"""\
        UPDATE secteurs SET
        nom_secteur = %(nom_secteur)s
        WHERE secteur_id = %(secteur_id)s
        ;"""
    kwargs.update({'secteur_id': _id})
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, kwargs)
        g.db.commit()



def create_appartient(secteur_id, entreprise_id):
    sql_cmd = u"""\
        INSERT INTO appartient(secteur_id, entreprise_id)
        VALUES (%(secteur_id)s, %(entreprise_id)s)
        ;"""
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, {'secteur_id': secteur_id, 'entreprise_id': entreprise_id})
        g.db.commit()

def delete_appartient(secteur_id, entreprise_id):
    sql_cmd = u"""\
        DELETE
        FROM appartient
        WHERE secteur_id = %(secteur_id)s AND entreprise_id = %(entreprise_id)s
        ;"""
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, {'secteur_id': secteur_id, 'entreprise_id': entreprise_id})
        g.db.commit()

def delete_appartient_entreprise(entreprise_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM appartient
        WHERE entreprise_id = %(entreprise_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'entreprise_id': entreprise_id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'entreprise_id': entreprise_id})
            g.db.commit()

def delete_secteur(_id):
    sql_cmd = u"""\
        DELETE
        FROM appartient
        WHERE secteur_id = %(secteur_id)s
        ;
        DELETE
        FROM secteurs
        WHERE secteur_id = %(secteur_id)s
        ;"""
    with g.db.cursor() as cur:
        cur.execute(sql_cmd, {'secteur_id': _id})
        g.db.commit()

def update_secteurs_entreprise(entreprise_id, secteur_ids_target):
    secteurs_agg = list_aggregate_entreprises_secteurs()
    secteur_ids_current = [secteur['secteur_id'] for secteur in secteurs_agg[entreprise_id]] if entreprise_id in secteurs_agg else []
    for st in secteur_ids_current:
        if st not in secteur_ids_target:
            delete_appartient(st, entreprise_id)
    for st in secteur_ids_target:
        if st not in secteur_ids_current:
            create_appartient(st, entreprise_id)
