# -*- coding: utf-8 -*-
import web
import sae.const

def _create_db():
    db = sae.const.MYSQL_DB
    user = sae.const.MYSQL_USER
    pw = sae.const.MYSQL_PASS
    host = sae.const.MYSQL_HOST
    port = int(sae.const.MYSQL_PORT)
    host_s = sae.const.MYSQL_HOST_S
    return web.database(dbn='mysql', host=host, port=port, db=db, user=user, pw=pw)