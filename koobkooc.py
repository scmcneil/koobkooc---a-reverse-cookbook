# Copyright Sheena C. McNeil

import sys
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
		veggie = raw_input("veggie: ")
		VEGGIES.append(veggie)

print ('Welcome to koobkooc---a-reverse-cookbook')
print ('OPTIONS: find a recipe or modify the database')
keep_going = True
while keep_going == True:
	instruction = raw_input('INSTRUCTION: ')
	if instruction != 'database' and instruction != 'recipes':
		print 'USAGE: "recipes" or "database"'
		instruction = raw_input('INSTRUCTION: ')
	elif instruction == 'database':
		DB()
	elif instruction == 'recipes':
		RECIPES()
	go_on = raw_input('Do you want to do something else? (y/n): ')
	if go_on == 'n':
		keep_going = False

