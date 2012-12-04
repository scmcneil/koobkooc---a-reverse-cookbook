# Copyright Sheena C. McNeil

import sys, os, sqlite3, intermediary

conn = sqlite3.connect('.koobkooc_database.db')
cur = conn.cursor()
# Initialize all the tables
try:
    cur.execute('create table if not exists recipes( id integer primary key autoincrement, type text, name text unique, recipe_file text)')
    cur.execute('create table if not exists meats( id integer primary key autoincrement, name text unique)')
    cur.execute('create table if not exists veggies( id integer primary key autoincrement, name text unique)')
    cur.execute('create table if not exists starches( id integer primary key, name text unique)')
    cur.execute('create table if not exists ingredients( id integer primary key autoincrement, name text unique)')
    cur.execute('create table if not exists recipe_veggies( recipe_id integer, veggie_id integer)')
    cur.execute('create table if not exists recipe_starches( recipe_id integer, starch_id integer)')
    cur.execute('create table if not exists recipe_meats( recipe_id integer, meat_id integer)')
    cur.execute('create table if not exists side_ingredients( recipe_id integer, ingredient_id integer)')
    cur.execute('create table if not exists recipe_sides( main_id integer, side_id integer)')
    conn.commit()
except:
    pass
	
# Populate starches table (only the first time)
cur.execute('insert or ignore into starches (id, name) values (1, "rice")')
cur.execute('insert or ignore into starches (id, name) values (2, "noodles")')
cur.execute('insert or ignore into starches (id, name) values (3, "potatoes")')
conn.commit()

# Database functions

def ADD_MAIN():
    ''' Adds a main dish to the database'''
    name = intermediary.get_name()
    meat = intermediary.get_meat()
    VEGGIES = intermediary.get_veggies()
    starch = intermediary.get_starch()
    recipe = intermediary.get_recipe()
    #dish_type = intermediary.get_type()
    dish_type = 'main'
    # Put the name of the recipe and the file into the database
    cur.execute('insert or ignore into recipes (name, type, recipe_file) values (?,?,?)', (name, dish_type, recipe))
    rid = get_recipe_id(name)
    # Try to put the meats and vegetables into the database in case they are not already there
    for veggie in VEGGIES.values():
        if veggie != '':
            add_veggie(veggie)
            id = get_veggie_id(veggie)
            add_recipe_veggie(rid, id)
    cur.execute('insert or ignore into meats (name) values ("%s")' % meat)
    mid = get_meat_id(meat)
    sid = get_starch_id(starch)
    # Put the meat, vegetable, and starch relationships into the database
    add_recipe_meat(rid, mid)
    add_recipe_starch(rid, sid)
    conn.commit()

def ADD_SIDE():
    name = intermediary.get_name()
    recipe = intermediary.get_recipe()
    dish_type = intermediary.get_type()
    cur.execute('insert or ignore into recipes (name, type, recipe_file) values (?,?,?)', (name, dish_type, recipe))
    rid = get_recipe_id(name)
    INGREDIENTS = intermediary.get_ingredients()
    for ingred in INGREDIENTS.values():
        if ingred != '':
            add_ingredient(ingred)
            id = get_ingredient_id(ingred)
            print(id)
            add_side_ingredient(rid, id)

def DELETE(recipe):
    '''permenantly deletes a recipe from the database'''
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

def EDIT_MAIN(recipe):
    rid = get_recipe_id(recipe)
    id = intermediary.get_id()
    name = get_recipe_name(id)
    # Update the veggies
    VEGGIES = intermediary.get_veggies()
    VIDS = set()
    for veggie in VEGGIES.values():
        if veggie != '':
            add_veggie(veggie)
            VIDS.add(get_veggie_id(veggie))
    ORIGINAL = set(get_recipe_veggies(rid))
    if VIDS != ORIGINAL:
        # this should be a set of the veggies that need to be deleted
        OLD = ORIGINAL - VIDS
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
    if recipe_file != get_recipe_text(rid):
        cur.execute('update recipes set recipe_file="%s" where id=%u' % (recipe_file, rid))
    conn.commit()
    return

def EDIT_SIDE(recipe):
    rid = get_recipe_id(recipe)
    INGREDIENTS = intermediary.get_ingredients()
    IIDS = set()
    for ingred in INGREDIENTS.values():
        if ingred != '':
            add_ingredient(ingred)
            IIDS.add(get_ingredient_id(ingred))
    ORIGINAL = set(get_side_ingredients(rid))
    if IIDS != ORIGINAL:
        OLD = ORIGINAL - IIDS
        for old in OLD:
            cur.execute('delete from side_ingredients where recipe_id=%1s and ingredient_id=%2s' % (rid, old))
        IIDS = IIDS - ORIGINAL
        for iid in IIDS:
            add_side_ingredient(rid, iid)
    recipe_file = intermediary.get_recipe()
    if recipe_file != get_recipe_text(rid):
        cur.execute('update recipes set recipe_file="%s" where id=%u' % (recipe_file, rid))
    conn.commit()

def FIND_MAIN(recipe):
    '''finds the meat, veggies, and starch that go with a main dish recipe'''
    rid = get_recipe_id(recipe)
    intermediary.set_name(recipe)
    intermediary.set_type(get_recipe_type(recipe))
    #find the meat
    mid = get_recipe_meat(rid)
    if mid != 'None':
        intermediary.set_meat(get_meat_name(get_recipe_meat(rid)))
    #find the veggies
    VEGGIES = []
    VIDS = get_recipe_veggies(rid)
    for vid in VIDS:
        VEGGIES.append(get_veggie_name(vid))
    intermediary.set_veggies(VEGGIES)
    roar = intermediary.get_veggies()
    #find the starch
    sid = get_recipe_starch(rid)
    if sid != None:
        intermediary.set_starch(get_starch_name(sid))
    #find the recipe
    intermediary.set_recipe(get_recipe_text(recipe))

def FIND_SIDE(recipe):
    '''finds the ingredients that go with a side dish recipe'''
    rid = get_recipe_id(recipe)
    intermediary.set_name(recipe)
    intermediary.set_type(get_recipe_type(recipe))
    # find the ingredients
    IIDS = get_side_ingredients(rid)
    INGREDIENTS = []
    for iid in IIDS:
        INGREDIENTS.append(get_ingredient_name(iid))
    intermediary.set_ingredients(INGREDIENTS)
    intermediary.set_recipe(get_recipe_text(recipe))


def SEARCH_MAIN(meat, VEGGIES, starch, strict):
    num_veggies = len(VEGGIES)
    VIDS = set()
    for veggie in VEGGIES.values():
        if veggie != '':
            VIDS.add(get_veggie_id(veggie))
    if meat != 'none':
        mid = get_meat_id(meat)
        match_meat = set()
        for row in cur.execute('select recipe_id from recipe_meats where meat_id=%u' % mid):
            match_meat.add(row[0])

    if starch != 'none':
        sid = get_starch_id(starch)
        match_starch = set()
        for row in cur.execute('select recipe_id from recipe_starches where starch_id=%u' % sid):
            match_starch.add(row[0])
        if meat != 'none':
            match_meat_and_starch = match_meat.intersection(match_starch)
        elif meat == 'none':
            match_meat_and_starch = match_starch
    elif starch == 'none' and meat != 'none':
        match_meat_and_starch = match_meat
    qualifying_recipes = set()

    for id in match_meat_and_starch:
        if VIDS > set():
            temp = set()
            for row in cur.execute('select veggie_id from recipe_veggies where recipe_id=%u' % id):
                temp.add(row[0])
            if strict:
                if temp == VIDS:
                    qualifying_recipes.add(get_recipe_name(id))
            elif not strict:
                if temp.intersection(VIDS) > set():
                    qualifying_recipes.add(get_recipe_name(id))
        elif VIDS == set():
            qualifying_recipes.add(get_recipe_name(id))
            
    qualifying_recipes = sorted(qualifying_recipes, key=lambda item: (int(item.partition(' ')[0])
                                        if item[0].isdigit() else float('inf'), item))
    return qualifying_recipes

def SEARCH_SIDE(ingredients, strict):
    IIDS = set()
    for ingred in ingredients.values():
        if ingred != '':
            IIDS.add(get_ingredient_id(ingred))
    
    partial = set()
    for id in IIDS:
        for row in cur.execute('select recipe_id from side_ingredients where ingredient_id=%u' % id):
            partial.add(row[0])
    qualifying_recipes = set()
    for id in partial:
        temp = set(get_side_ingredients(id))
        if strict:
            if temp == IIDS:
                qualifying_recipes.add(get_recipe_name(id))
        elif not strict:
            if temp.intersection(IIDS) > set():
                qualifying_recipes.add(get_recipe_name(id))
    qualifying_recipes = sorted(qualifying_recipes, key=lambda item: (int(item.partition(' ')[0])
                                        if item[0].isdigit() else float('inf'), item))
    return qualifying_recipes
                


def get_recipe_names(dish_type):
    '''gets the names of all the recipes of certain type in the database'''
    recipes = []
    #dish_type = intermediary.get_type()
    for row in cur.execute('select name from recipes where type="%s" order by name' % dish_type):
        recipes.append(row[0])
    print(recipes)
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

def get_ingredient_names():
    '''gets the names of all the ingredients in the database'''
    INGREDIENTS = set()
    for row in cur.execute('select name from ingredients order by name'):
        INGREDIENTS.add(row[0])
    return INGREDIENTS

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

def get_recipe_type(recipe):
    for row in cur.execute('select type from recipes where name="%s"' % recipe):
        return row[0]

def add_veggie(veggie):
    '''adds a vegetable to the veggies table'''
    cur.execute('insert or ignore into veggies (name) values ("%s")' % veggie)
    conn.commit()

def add_ingredient(ingredient):
    '''adds an ingredient into the ingredients table'''
    cur.execute('insert or ignore into ingredients (name) values ("%s")' % ingredient)
    conn.commit()

def get_ingredient_id(ingredient):
    '''gets the ID of an ingredient'''
    for row in cur.execute('select id from ingredients where name="%s"' % ingredient):
        return row[0]

def get_ingredient_name(ingredient):
    '''gets the name of an ingredient'''
    for row in cur.execute('select name from ingredients where id=%u' % ingredient):
        return row[0]
	
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

def add_side_ingredient(recipe, ingredient):
    '''adds a side and ingredient relationship'''
    cur.execute('insert into side_ingredients(recipe_id, ingredient_id) values (?,?)', (recipe, ingredient))
    conn.commit()

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

def get_side_ingredients(recipe_id):
    INGREDIENTS = []
    for row in cur.execute('select ingredient_id from side_ingredients where recipe_id=%u' % recipe_id):
        INGREDIENTS.append(row[0])
    return INGREDIENTS

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
