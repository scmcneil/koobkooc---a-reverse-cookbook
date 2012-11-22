# Copyright Sheena C. McNeil

import sys, os, sqlite3, intermediary

conn = sqlite3.connect('.koobkooc_database.db')
cur = conn.cursor()

# Initialize all the tables
try:
	cur.execute('create table if not exists recipes( id integer primary key autoincrement, name text unique, recipe_file text)')
	cur.execute('create table if not exists meats( id integer primary key autoincrement, name text unique)')
	cur.execute('create table if not exists veggies( id integer primary key autoincrement, name text unique)')
	cur.execute('create table if not exists starches( id integer primary key autoincrement, name text unique)')
	cur.execute('create table if not exists recipe_veggies( recipe_id integer, veggie_id integer)')
	cur.execute('create table if not exists recipe_starches( recipe_id integer, starch_id integer)')
	cur.execute('create table if not exists recipe_meats( recipe_id integer, meat_id integer)')
	conn.commit()
except:
	pass
	
# Populate starches table (only the first time)
cur.execute('insert or ignore into starches (name) values ("Rice")')
cur.execute('insert or ignore into starches (name) values ("Noodles")')
cur.execute('insert or ignore into starches (name) values ("Potatoes")')
conn.commit()

# Database functions
# ADD
def ADD():
	''' Adds a recipe into the database'''
	name = intermediary.get_name()
	meat = intermediary.get_meat()
	VEGGIES = intermediary.get_veggies()
	starch = intermediary.get_starch()
	recipe = intermediary.get_recipe()
	# Put the name of the recipe and the file into the database
	cur.execute('insert or ignore into recipes (name, recipe_file) values (?,?)', (name, recipe))
	rid = get_recipe_id(name)
	# Try to put the meats and vegetables into the database in case they are not already there
	VIDS = {}
	for veggie in VEGGIES:
		add_veggie(veggie)
		id = get_veggie_id(veggie)
		VIDS.update({veggie: id})
	cur.excute('insert or ignore into meats (name) values ("%s")' meat)
	mid = get_meat_id(meat)
	sid = get_starch_id(starch)
	# Put the meat, vegetable, and starch relationships into the database
	#cur.execute("insert into recipe_meats values (recipe_id, meat_id) where recipe_id and meat_id in (select r.id as recipe_id, m.id as meat_id from recipes r, meats m where r.name = '%(r)s' and m.name = '%(m)s'" % {r : name, m : meat})
	for value in VIDS.values():
		add_recipe_veggie(rid, value)
	add_recipe_meat(rid, mid)
	add_recipe_starch(rid, sid)
	conn.commit()
	
def get_recipe_id(recipe):
	'''gets the ID of a recipe'''
	for row in cur.execute("select id from recipes where name='%s'" % recipe):
		return row[0]

def add_veggie(veggie):
	'''adds a vegetable to the  veggies table'''
	cur.execute('insert or ignore into veggies (name) values ("%s")' % veggie)
	conn.commit()
	
def get_veggie_id(veggie):
	'''gets the ID of a veggie'''
	for row in cur.execute("select * from veggies where name='%s'" % veggie):
		return row[0]
		
def get_meat_id(meat):
	'''gets the ID of a meat'''
	for row in cur.execute("select * from meats where name='%s'" % meat):
		return row[0]
		
def get_starch_id(starch):
	'''gets the ID of a starch'''
	for row in cur.execute("select * from starches where name='%s'" % starch):
		return row[0]

def add_recipe_veggie(recipe, veggie):
	'''adds a recipe and vegetable relationship the the proper table'''
	cur.execute('insert into recipe_veggies (recipe_id, veggie_id) values (?,?)', (recipe, veggie))
	conn.commit()

def add_recipe_meat(recipe, meat):
	'''adds a recipe and meat relationship the the proper table'''
	cur.execute('insert into recipe_meats (recipe_id, meat_id) values (?,?)', (recipe, meat))
	conn.commit()

def add_recipe_starch(recipe, starch):
	'''adds a recipe and starch relationship the the proper table'''
	cur.execute('insert into recipe_starches (recipe_id, starch_id) values (?,?)', (recipe, starch))
	conn.commit()




















