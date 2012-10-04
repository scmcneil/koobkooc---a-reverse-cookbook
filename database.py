#Copyright Sheena C. McNeil

import intermediary
import sys
import os
import sqlite3

conn = sqlite3.connect("recipes.db")
cur = conn.cursor()

try:
    cur.execute("create table if not exists recipes(recipe_name text, meat text, veggie_one text, veggie_two text, veggie_three text, veggie_four text, starch text, recipe_file text)")
except:
    pass

def get_name():
    name = intermediary.get_name()


def ADD():
    name = intermediary.get_name().lower()
    meat = intermediary.get_meat().lower()
    veggies = intermediary.get_veggies()
    veggies = list(map(str.lower, veggies))
    starch = intermediary.get_starch().lower()
    recipe_string = intermediary.get_recipe()
    cur.execute("insert into recipes values (?,?,?,?,?,?,?,?)", (name, meat, veggies[0], veggies[1], veggies[2], veggies[3], starch, recipe_string))
    conn.commit()

def Add_to_db(recipe, meat, VEGGIES, starch, full_path):
    g = open(full_path)
    recipe_string = ''
    recipe_string = g.read()
    cur.execute("insert into recipes values (?,?,?,?,?,?,?,?)", (recipe, meat, VEGGIES[0], VEGGIES[1], VEGGIES[2], VEGGIES[3], starch, recipe_string))
    conn.commit()

def Delete_from_db(recipe_name):
    query = "delete from recipes where recipe_name = '%s'" % recipe_name
    cur.execute(query)
    conn.commit()
    print('roar')

def Browse_db():
    recipes = []
    for row in cur.execute("select recipe_name from recipes"):
        recipes.append(row[0].title())
    return recipes

def Find_for_edit(recipe_name):
    recipe_name = recipe_name.lower()
    query = "select * from recipes where recipe_name = '%s'" % recipe_name
    for row in cur.execute(query):
        intermediary.set_name(recipe_name)
        intermediary.set_meat(row[1])
        intermediary.set_veggie1(row[2])
        intermediary.set_veggie2(row[3])
        intermediary.set_veggie3(row[4])
        intermediary.set_veggie4(row[5])
        intermediary.set_starch(row[6])
        intermediary.set_recipe(row[7])

def Edit_recipe(recipe):
    recipe = recipe.lower()
    meat = intermediary.get_meat().lower()
    veggies = intermediary.get_veggies()
    veggies = list(map(str.lower, veggies))
    starch = intermediary.get_starch().lower()
    recipe_string = intermediary.get_recipe()
    update = "update recipes set meat='" + meat
    update += "', veggie_one='" + veggies[0]
    update += "', veggie_two='" + veggies[1]
    update += "', veggie_three='" + veggies[2]
    update += "', veggie_four='" + veggies[3]
    update += "', starch='" + starch
    update += "', recipe_file='" + recipe_string
    update += "' where recipe_name='" + recipe + "'"
    cur.execute(update)
    conn.commit()

def Recipe_text(recipe):
    recipe = recipe.lower()
    query = "select recipe_file from recipes where recipe_name = '%s'" % recipe
    for row in cur.execute(query):
        return row[0]
    

def Print_db():
    for row in cur.execute("select recipe_name, meat, veggie_one, veggie_two, veggie_three, veggie_four, starch, recipe_file from recipes"):
        print ('-'*10)
        print ('Recipe: ', row[0].title())
        print ('Meat: ', row[1].title())
        for x in range(2, 6):
            if row[x] != 'none':
                print ('Veggie', (x-1), ': ', row[x].title() )
        print ('Starch: ', row[6].title())
        print (row[7])

def Find_recipe(MEAT, VEGGIES, NUM, STARCH):
	qualifying_recipes = []
	query = "select * from recipes where meat = '" + MEAT + "' and starch = '" + STARCH + "'"
	#print (query)
	for row in cur.execute(query):
		matches = 0
		for x in range(2, 7):
			for y in range(0, NUM):
				if VEGGIES[y] == row[x]:
					matches += 1
		if matches == NUM:
			qualifying_recipes.append(row[0].title())
	return qualifying_recipes

def Print_recipe(RECIPE):
    RECIPE = RECIPE.lower()
    query = "select recipe_file from recipes where recipe_name = '%s'" % RECIPE
    for row in cur.execute(query):
        print (row[0])
