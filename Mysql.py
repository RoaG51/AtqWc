# -*- coding: utf-8 -*-
import web

def _create_db():
    db = AtqWc
    user = root
    pw = sanguo
    return web.database(dbn='mysql', db=db, user=user, pw=pw)