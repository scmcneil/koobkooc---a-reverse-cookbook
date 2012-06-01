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
	
def Add_to_db():
	keep_adding = True
	while keep_adding == True:
		recipe = raw_input('Recipe name: ')
		meat = raw_input('type of meat: ').lower()
		num_veggies = raw_input('number of vegetables (up to four): ')
		VEGGIES = []
		for x in range(0, int(num_veggies)):
			veggie = raw_input('veggie: ').lower()
			VEGGIES.append(veggie)

		if int(num_veggies) < 4:
			for x in range(int(num_veggies), 4):
				VEGGIES.append('none')


		flag = False
		for row in cur.execute("select * from recipes"):
			if row[0] == recipe:
				flag = True

		if flag == False:
			#open the file and read it in to a string.
			#use the string as the text for the database.
			f = recipe.lower() + '.txt'
			g = open(f)
			recipe_string = ''
			recipe_string = g.read()
			cur.execute("insert into recipes values (?,?,?,?,?,?,?)", (recipe, meat, VEGGIES[0], VEGGIES[1], VEGGIES[2], VEGGIES[3], recipe_string))
		conn.commit()

		go_on = raw_input('Keep adding? (y/n): ').lower()
		if go_on == 'n':
			keep_adding = False

def Delete_from_db():
	keep_deleting = True
	while keep_deleting == True:
		to_be_deleted = raw_input("Recipe name to delete: ")
		query = "delete from recipes where recipe_name = '%s'" % to_be_deleted
		cur.execute(query)
		conn.commit()
	
		go_on = raw_input('Keep deleting? (y/n): ')
		if go_on == 'n':
			keep_deleting = False

def Print_db():
	for row in cur.execute("select * from recipes"):
		print '-'*10
		print 'Recipe:', row[0]
		print 'Meat:', row[1]
	for x in range(2, 6):
		if row[x] != 'none':
			print 'Veggie', (x-1), ':', row[x] 

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
			qualifying_recipes.append(row[0])
	return qualifying_recipes

def Print_recipe(RECIPE):
	query = "select * from recipes where recipe_name = '%s'" % RECIPE
	for row in cur.execute(query):
		print row[6]
