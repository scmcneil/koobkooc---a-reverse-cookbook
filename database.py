#Copyright Sheena C. McNeil

import sys
import os
import sqlite3

conn = sqlite3.connect("recipes.db")
cur = conn.cursor()

try:
    cur.execute("create table if not exists recipes(recipe_name text, meat text, veggie_one text, veggie_two text, veggie_three text, veggie_four text)")
except:
    pass
	
def Add_to_db():
	keep_adding = True
	while keep_adding == True:
		recipe = raw_input('Recipe name: ')
		meat = raw_input('type of meat: ')
		num_veggies = raw_input('number of vegetables (up to four): ')
		VEGGIES = []
		for x in range(0, int(num_veggies)):
			veggie = raw_input('veggie: ')
			VEGGIES.append(veggie)

		if int(num_veggies) < 4:
			for x in range(int(num_veggies), 4):
				VEGGIES.append('none')


		flag = False
		for row in cur.execute("select * from recipes"):
			if row[0] == recipe:
				flag = True

		if flag == False:
			cur.execute("insert into recipes values (?,?,?,?,?,?)", (recipe, meat, VEGGIES[0], VEGGIES[1], VEGGIES[2], VEGGIES[3]))
		conn.commit()

		go_on = raw_input('Keep adding? (y/n): ')
		if go_on == 'n':
			keep_adding = False

def Delete_from_db():
	keep_deleting = True
	while keep_deleting == True:
		print 'roar'
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


