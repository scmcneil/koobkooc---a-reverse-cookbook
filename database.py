#Copyright Sheena C. McNeil

import sys
import os
import sqlite3

conn = sqlite3.connect("recipes.db")
cur = conn.cursor()

try:
    cur.execute("create table if not exists recipes(recipe_name text, meat text, veggie_one text, veggie_two text, veggie_three text, veggie_four text, recipe_file text)")
except:
    pass
	
def Add_to_db(recipe, meat, VEGGIES, full_path):
    g = open(full_path)
    recipe_string = ''
    recipe_string = g.read()
    cur.execute("insert into recipes values (?,?,?,?,?,?,?)", (recipe, meat, VEGGIES[0], VEGGIES[1], VEGGIES[2], VEGGIES[3], recipe_string))
    conn.commit()

def Delete_from_db(recipe_name):
    query = "delete from recipes where recipe_name = '%s'" % recipe_name
    cur.execute(query)
    conn.commit()

def Print_db():
    for row in cur.execute("select recipe_name, meat, veggie_one, veggie_two, veggie_three, veggie_four from recipes"):
        print ('-'*10)
        print ('Recipe:', row[0])
        print ('Meat:', row[1])
        for x in range(2, 6):
            if row[x] != 'none':
                print ('Veggie', (x-1), ':', row[x] )

def Find_recipe(MEAT, VEGGIES, NUM):
	qualifying_recipes = []
	query = "select * from recipes where meat = '%s'" % MEAT
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
