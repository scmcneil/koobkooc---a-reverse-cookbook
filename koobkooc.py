# Copyright Sheena C. McNeil

import sys
import os
import database
#--------Database Functions--------#
def DB():
	db_instruction = input('DATABASE INSTRUCTION: ')
	if db_instruction == 'add':
		database.Add_to_db()
	elif db_instruction == 'delete':
		database.Delete_from_db()
	elif db_instruction == 'print':
		database.Print_db()

#--------Recipe Functions/Finding--------#
def RECIPES():
	meat = input("What type of meat would you like to use? ")
	num_veggies = input("How many vegetables would you like to use? ")
	VEGGIES = []
	for x in range(0, int(num_veggies)):
		veggie = input("veggie: ").lower()
		VEGGIES.append(veggie)

	stop = False
	while stop == False:
		recipes = database.Find_recipe(meat, VEGGIES, int(num_veggies))
		if len(recipes) > 0:
			for x in recipes:
				print (x)
			choose_recipe = input("Which recipe would you like to view? ")
			database.Print_recipe(choose_recipe)
			view_other =  input('\n\nWould you like to go back and view a different recipe? (y/n): ')
			if view_other == 'y':
				os.system('clear')
			if view_other == 'n':
				stop = True
		elif len(recipes) == 0:
			print('No recipes match your search')
			search_again = input('Would you like to try a new search? (y/n): ')
			if search_again == 'y':
				RECIPES()
#---------------Main---------------------#

def main():
        print ('Welcome to koobkooc---a-reverse-cookbook')
        print ('OPTIONS: find a recipe or modify the database')
        keep_going = True
        while keep_going == True:
                instruction = input('INSTRUCTION: ')
                if instruction != 'database' and instruction != 'recipe':
                        print ('USAGE: "recipe" or "database"')
                        instruction  = input('INSTRUCTION: ')
                if instruction == 'database':
                        DB()
                if instruction == 'recipe':
                        RECIPES()
                go_on = input('Do you want to do something else? (y/n): ')
                if go_on == 'n':
                        keep_going = False

if __name__ == '__main__':
        main()
