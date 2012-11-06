# Copyright Sheena C. McNeil

import sys, os, sqlite3, imtermediary

conn = sqlite3.connect('.koobkooc_database.db')
cur = conn.cursor()

# Initialize all the tables
try:
	cur.execute('create table if not exists recipes( id tintint primary key autoincrement, name text, recipe_file text)')
	cur.execute('create table if not exists meats( id tinyint primary key autoincrement, name text)')
	cur.execute('create table if not exists veggies( id tinyint primary key autoincrement, name text)')
	cur.execute('create table if not exists starches( id tinyint primary key autoincrement, name text)')
	cur.execute('create table if not exists recipe_veggies( recipe_id tinyint, veggie_id tinyint)')
	cur.execute('create table if not exists recipe_starches( recipe_id tinyint, starch_id tinyint)')
	cur.execute('create table if not exists recipe_meats( recipe_id tinyint, meat_id tinyint)')
except:
	pass
	
# Populate starches table
cur.execute('insert into starches (name) values ("Rice")')
cur.execute('insert into starches (name) values ("Noodles")')
cur.execute('insert into starches (name) values ("Potatoes")')
conn.commit()


