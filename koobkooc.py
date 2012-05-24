# Copyright Sheena C. McNeil

import sys
import database




def DB():
	db_instruction = raw_input('DATABASE INSTRUCTION: ')
	if db_instruction == 'add':
		database.Add_to_db()
	elif db_instruction == 'print':
		database.Print_db()



print ('Welcome to koobkooc---a-reverse-cookbook')
print ('OPTIONS: find a recipe or modify the database')
keep_going = True
while keep_going == True:
	instruction = raw_input('INSTRUCTION: ')
	if instruction == 'database':
		DB()
	
	if instruction == 'recipes':
		RECIPES()
	go_on = raw_input('Do you want to do something else? (y/n): ')
	if go_on == 'n':
		keep_going = False

