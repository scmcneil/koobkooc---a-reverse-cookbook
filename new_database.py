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
    cur.execute('insert or ignore into meats (name) values ("%s")' % meat)
    mid = get_meat_id(meat)
    sid = get_starch_id(starch)
    # Put the meat, vegetable, and starch relationships into the database
    for value in VIDS.values():
        add_recipe_veggie(rid, value)
    add_recipe_meat(rid, mid)
    add_recipe_starch(rid, sid)
    conn.commit()
	
def DELETE(recipe):
    '''premenantly deletes a recipe from the database'''
    rid = get_recipe_id(recipe)
    #get rid of the veggie relationships
    cur.execute('delete from recipe_veggies where recipe_id=%u' % rid)
    #get rid of the meat relationships
    cur.execute('delete from recipe_meats where recipe_id=%u' % rid)
    #get rid of the starch relationships
    cur.execute('delete from recipe_starches where recipe_id=%u' % rid)
    #get rid of the recipe itself
    cur.execute('delete from recipes where id=%u' % rid)
    conn.commit()

def EDIT(recipe):
    return

def FIND(recipe):
    '''finds the meat, veggies, and starch that goes with a recipe'''
    rid = get_recipe_id(recipe)
    #find the meat
    intermediary.set_meat(get_meat_name(get_recipe_meat(rid)))
    #find the veggies
    VIDS = get_recipe_veggies(rid)
    for vid in VIDS:
        VEGGIES.append(get_veggie_name(vid))
    intermediary.set_veggie1(VEGGIE[0])
    intermediary.set_veggie2(VEGGIE[1])
    intermediary.set_veggie3(VEGGIE[2])
    intermediary.set_veggie4(VEGGIE[3])
    #find the starch
    intermediary.set_starch(get_starch_name(get_starch_id(rid)))

def SEARCH(meat, VEGGIES, starch):
    num_veggies = len(VEGGIES)
    mid = get_meat_id(meat)
    match_meat = set()
    for row in cur.execute('select recipe_id from recipe_meats where meat_id=%u' % mid)
        match_meat.add(row[0])
    sid = get_starch_id(starch)
    match_starch = set()
    for row in cur.execute('select recipe_id from recipe_meats where starch_id=%u' % sid):
        match_starch.add(row[0])
    match_meat_and_starch = set()
    for meat in match_meat:
        for starch in match_starch:
            if meat == starch:
                match_meat_and_starch.add(meat)

    return

def get_recipe_names():
    '''gets the names of all the recipes in the database'''
    recipes = []
    for row in cur.execute('select name from recipes order by name'):
        recipes.append(row[0])
    return recipes

def get_veggie_names():
    '''gets the names of all the vegetables in the database'''
    VEGGIES = set()
    for row in cur.execute('select name from veggies order by name'):
        VEGGIES.add(row[0])
    return VEGGIES

def get_meat_names():
    '''gets the names of all the meats in the database'''
    MEATS = set()
    for row in cur.execute('select name from meats order by name'):
        MEATS.add(row[0])
    return MEATS

def get_recipe_id(recipe):
    '''gets the ID of a recipe'''
    for row in cur.execute("select id from recipes where name='%s'" % recipe):
        return row[0]

def get_recipe_text(recipe):
    for row in cur.execute('select recipe_file from recipes where name="%s"' % recipe):
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

def get_recipe_meat(recipe_id):
    for row in cur.execute('select meat_id from recipe_meats where recipe_id=%u' % recipe_id):
        return row[0]

def get_recipe_veggies(recipe_id):
    VEGGIES = []
    for row in cur.execute('select veggie_id from recipe_veggies where recipe_id=%u' % recipe_id):
        VEGGIES.append(row[0])
    return VEGGIES

def get_recipe_starch(recipe_id):
    for row in cur.execute('select starch_id from recipe_starches where recipe_id=%u' % recipe_id):
        return row[0]

def get_veggie_name(veggie_id):
    '''gets the name of a veggie'''
    for row in cur.execute("select name from veggies where id=%u" % veggie_id):
        return row[0]
		
def get_meat_name(meat_id):
    '''gets the name of a meat'''
    for row in cur.execute("select name from meats where name='%s'" % meat_id):
        return row[0]
		
def get_starch_name(starch_id):
    '''gets the name of a starch'''
    for row in cur.execute("select name from starches where name='%s'" % starch_id):
        return row[0]


