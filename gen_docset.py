#!/usr/bin/env python
# coding:utf-8

import os
import sqlite3
import sys
import os.path

__author__ = 'qingfeng'

res_dir = sys.argv[1]
doc_id = ""

db = sqlite3.connect("{}/docSet.dsidx".format(res_dir))
cur = db.cursor()


cur.execute('DROP TABLE searchIndex;')
cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

pages = ["Guide"]

sql = 'INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)'

doc_dir = "{}/Documents/{}".format(res_dir, doc_id)


for root, dirs, files in os.walk("/Users/qingfeng/project/_site"):
    for name in files:
        if root == '/Users/qingfeng/project/_site':
            if name.endswith('html'):
                path = '/' + name
                cur.execute(sql, (name[:-5], 'Guide', path))

db.commit()
db.close()
