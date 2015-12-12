# -*- encoding: utf-8 -*-

from flask import g
from psycopg2.extras import DictCursor, NamedTupleCursor

from collections import OrderedDict


def sanitize_fetched_data(l):
    lout = []
    for d in l:
        dout = OrderedDict()
        din = d._asdict()
        for k, v in din.items():
            if type(din[k]) in (str, unicode):
                dout[k] = unicode(din[k].decode('utf-8').strip())
            else:
                dout[k] = din[k]
        lout.append(dout)
    return lout


################################################################################
# Adresses
################################################################################


def create_adresse(cursor=None, **kwargs):
    sql_cmd = u"""\
        INSERT INTO adresses(ville, code_postal, adresse)
        VALUES (%(ville)s, %(code_postal)s, %(adresse)s)
        RETURNING adresse_id;
        ;"""
    if cursor:
        cursor.execute(sql_cmd, kwargs)
        adresse_id = cursor.fetchone()[0]
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            g.db.commit()
            adresse_id = cur.fetchone()[0]
    return adresse_id


def list_adresses():
    sql_cmd = u"""\
        SELECT ville, code_postal, adresse
        FROM adresses
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd)
        listall = cur.fetchall()
    listall = sanitize_fetched_data(listall)
    return listall


def get_adresse(_id, raw=False):
    sql_cmd = u"""\
        SELECT *
        FROM adresses
        WHERE adresse_id = %(addresse_id)s
        ;"""
    with g.db.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute(sql_cmd, {'adresse_id': _id})
        listall = cur.fetchall()
    if raw:
        return listall
    else:
        if listall:
            listall = sanitize_fetched_data(listall)
            assert len(listall) == 1
            return listall[0]
        else:
            return None

def str_adresse(_id):
    e = get_adresse(_id)
    if e:
        return u'Adresse: {} à {}({})'.format(e['adresse'], e['ville'], e['code_postal'])
    else:
        return u'None'

def update_adresse(_id, cursor=None, **kwargs):
    sql_cmd = u"""\
        UPDATE adresses SET
        ville = %(ville)s,
        code_postal = %(code_postal)s,
        adresse = %(adresse)s
        WHERE adresse_id = %(adresse_id)s
        ;"""
    kwargs.update({'adresse_id': _id})
    if cursor:
        cursor.execute(sql_cmd, kwargs)
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, kwargs)
            g.db.commit()


def delete_adresse(_id, cursor=None):
    sql_cmd = u"""\
        DELETE
        FROM adresses
        WHERE adresse_id = %(adresse_id)s
        ;"""
    if cursor:
        cursor.execute(sql_cmd, {'adresse_id': _id})
    else:
        with g.db.cursor() as cur:
            cur.execute(sql_cmd, {'adresse_id': _id})
            g.db.commit()
