# Copyright Sheena C. McNeil

import sys
import os
import database

def DB():
	db_instruction = raw_input('DATABASE INSTRUCTION: ')
	if db_instruction == 'add':
		database.Add_to_db()
	if db_instruction == 'delete':
		database.Delete_from_db()
	elif db_instruction == 'print':
		database.Print_db()

def RECIPES():
	meat = raw_input("What type of meat would you like to use? ")
	num_veggies = raw_input("How many vegetables would you like to use? ")
	VEGGIES = []
	for x in range(0, int(num_veggies)):
		veggie = raw_input("veggie: ").lower()
		VEGGIES.append(veggie)

	stop = False
	while stop == False:
		recipes = database.Find_recipe(meat, VEGGIES, int(num_veggies))
		for x in recipes:
			print x
		choose_recipe = raw_input("Which recipe would you like to view? ")
		database.Print_recipe(choose_recipe)
		view_other =  raw_input('\n\nWould you like to go back and view a different recipe? (y/n)')
		if view_other == 'y':
			os.system('clear')
		if view_other == 'n':
			stop = True

print ('Welcome to koobkooc---a-reverse-cookbook')
print ('OPTIONS: find a recipe or modify the database')
keep_going = True
while keep_going == True:
	instruction = raw_input('INSTRUCTION: ')
	if instruction != 'database' and instruction != 'recipes':
		print 'USAGE: "recipes" or "database"'
		instruction  = raw_input('INSTRUCTION: ')

	if instruction == 'database':
		DB()
	if instruction == 'recipes':
		RECIPES()
	go_on = raw_input('Do you want to do something else? (y/n): ')
	if go_on == 'n':
		keep_going = False

