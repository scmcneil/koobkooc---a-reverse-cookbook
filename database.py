# Copyright Sheena C. McNeil

import sys, os, sqlite3, intermediary

conn = sqlite3.connect('.koobkooc_database.db')
cur = conn.cursor()
# Initialize all the tables
try:
    cur.execute('create table if not exists recipes( id integer primary key autoincrement, name text unique, recipe_file text)')
    cur.execute('create table if not exists meats( id integer primary key autoincrement, name text unique)')
    cur.execute('create table if not exists veggies( id integer primary key autoincrement, name text unique)')
    cur.execute('create table if not exists starches( id integer primary key, name text unique)')
    cur.execute('create table if not exists recipe_veggies( recipe_id integer, veggie_id integer)')
    cur.execute('create table if not exists recipe_starches( recipe_id integer, starch_id integer)')
    cur.execute('create table if not exists recipe_meats( recipe_id integer, meat_id integer)')
    conn.commit()
except:
    pass
	
# Populate starches table (only the first time)
cur.execute('insert or ignore into starches (id, name) values (1, "rice")')
cur.execute('insert or ignore into starches (id, name) values (2, "noodles")')
cur.execute('insert or ignore into starches (id, name) values (3, "potatoes")')
conn.commit()

# Database functions
# ADD
def ADD():
    ''' Adds a recipe into the database'''
    name = intermediary.get_name()
    meat = intermediary.get_meat()
    print(meat)
    VEGGIES = intermediary.get_veggies()
    print(VEGGIES)
    starch = intermediary.get_starch()
    print(starch)
    recipe = intermediary.get_recipe()
    # Put the name of the recipe and the file into the database
    cur.execute('insert or ignore into recipes (name, recipe_file) values (?,?)', (name, recipe))
    rid = get_recipe_id(name)
    # Try to put the meats and vegetables into the database in case they are not already there
    VIDS = {}
    for veggie in VEGGIES.values():
        if veggie != '':
            add_veggie(veggie)
            id = get_veggie_id(veggie)
            VIDS.update({veggie: id})
    print(VIDS)
    cur.execute('insert or ignore into meats (name) values ("%s")' % meat)
    mid = get_meat_id(meat)
    sid = get_starch_id(starch)
    print(sid)
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
    print('recipe: ', recipe)
    rid = get_recipe_id(recipe)
    #intermediary.set_id(rid)
    print('rid: ', rid)
    id = intermediary.get_id()
    print('get_id: ', id)
    name = get_recipe_name(id)
    print('name: ', name)
    # Update the veggies
    VEGGIES = intermediary.get_veggies()
    print('V: ', VEGGIES)
    print(VEGGIES)
    VIDS = set()
    for veggie in VEGGIES.values():
        if veggie != '':
            add_veggie(veggie)
            VIDS.add(get_veggie_id(veggie))
    ORIGINAL = set(get_recipe_veggies(rid))
    print('VIDS: ', VIDS)
    print('ORIGINAL: ', ORIGINAL)
    if VIDS != ORIGINAL:
        # this should be a set of the veggies that need to be deleted
        OLD = ORIGINAL - VIDS
        print('old: ', OLD)
        for old in OLD:
            cur.execute('delete from recipe_veggies where recipe_id=%1s and veggie_id=%2s' % (rid, old))
        conn.commit()
        # this should be a set of the new veggies that need to be added
        VIDS = VIDS - ORIGINAL
        for vid in VIDS:
            add_recipe_veggie(rid, vid)
        conn.commit()
    # Update the meat
    meat = get_meat_id(intermediary.get_meat())
    old_meat = get_recipe_meat(rid)
    if meat != old_meat:
        cur.execute('delete from recipe_meats where recipe_id=%u' % rid)
        add_recipe_meat(rid, meat)
    # Update the starch
    starch = get_starch_id(intermediary.get_starch())
    old_starch = get_recipe_starch(rid)
    if starch != old_starch:
        cur.execute('delete from recipe_starches where recipe_id=%u' % rid)
        add_recipe_meat(rid, starch)
    # Update the recipe file
    recipe_file = intermediary.get_recipe()
    print(recipe_file)
    if recipe_file != get_recipe_text(rid):
        cur.execute('update recipes set recipe_file="%s" where id=%u' % (recipe_file, rid))
    conn.commit()
    return

def FIND(recipe):
    '''finds the meat, veggies, and starch that goes with a recipe'''
    rid = get_recipe_id(recipe)
    intermediary.set_name(recipe)
    print('rid: ', rid)
    #find the meat
    mid = get_recipe_meat(rid)
    if mid != 'None':
        print('mid: ', mid)
        intermediary.set_meat(get_meat_name(get_recipe_meat(rid)))
        print('meat: ', intermediary.get_meat())
    #find the veggies
    VEGGIES = []
    VIDS = get_recipe_veggies(rid)
    for vid in VIDS:
        VEGGIES.append(get_veggie_name(vid))
    print('VIDS: ', VIDS, 'VEGGIES: ', VEGGIES)
    intermediary.set_veggies(VEGGIES)
    roar = intermediary.get_veggies()
    print('veggies: ', roar)
    #find the starch
    sid = get_recipe_starch(rid)
    print ('sid: ', sid)
    if sid != None:
        intermediary.set_starch(get_starch_name(sid))
    #find the recipe
    intermediary.set_recipe(get_recipe_text(recipe))

def SEARCH(meat, VEGGIES, starch):
    num_veggies = len(VEGGIES)
    VIDS = set()
    for veggie in VEGGIES:
        VIDS.add(get_veggie_id(veggie))
    mid = get_meat_id(meat)
    match_meat = set()
    for row in cur.execute('select recipe_id from recipe_meats where meat_id=%u' % mid):
        match_meat.add(row[0])
    sid = get_starch_id(starch)
    match_starch = set()
    for row in cur.execute('select recipe_id from recipe_meats where starch_id=%u' % sid):
        match_starch.add(row[0])
    match_meat_and_starch = match_meat.intersection(match_starch)
    qualifying_recipes = set()
    for id in match_meat_and_starch:
        for row in execute('select veggie_id from recipe_veggies where recipe_id=%u' % id):
            matches = 0
            for x in range(0, num_veggies):
                if VIDS[x] == row[0]:
                    matches += 1
            if matches == num_veggies:
                qualifying_recipes.add(id)
    return qualifying_recipes

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

def get_recipe_name(id):
    '''gets the name of a recipe'''
    for row in cur.execute("select name from recipes where id=%u" % id):
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
    for row in cur.execute("select id from starches where name='%s'" % starch):
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
    for row in cur.execute("select name from meats where id=%u" % meat_id):
        return row[0]
		
def get_starch_name(starch_id):
    '''gets the name of a starch'''
    for row in cur.execute("select name from starches where id=%u" % starch_id):
        return row[0]

