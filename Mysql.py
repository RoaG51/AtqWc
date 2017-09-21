# -*- coding: utf-8 -*-
import web

def _create_db():
    return web.database(dbn='mysql', db="AtqWc", user="root", pw="sanguo")