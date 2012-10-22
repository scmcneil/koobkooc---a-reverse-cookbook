# Copyright Sheena C. McNeil

import sys
import os
import database
import sqlite3

conn = sqlite3.connect("recipes.db")
cur = conn.cursor()

try:
    cur.execute("create table if not exists recipes(recipe_name text, meat text, veggie_one text, veggie_two text, veggie_three text, veggie_four text, recipe_file text)")
except:
    pass

#--------Database Functions--------#
def DB():
    db_instruction = input('DATABASE INSTRUCTION: ')
    if db_instruction == 'add':
        keep_adding = True
        while keep_adding == True:
            recipe = input('Recipe name: ').lower()
            flag = False
            for row in cur.execute("select * from recipes"):
                if row[0] == recipe:
                    flag = True
                    print ('Recipe is already in database')

            meat = input('type of meat: ').lower()
            starch = input('starch: ').lower()
            num_veggies = input('number of vegetables (up to four): ')
            VEGGIES = []
            for x in range(0, int(num_veggies)):
                veggie = input('veggie: ').lower()
                VEGGIES.append(veggie)

            if int(num_veggies) < 4:
                for x in range(int(num_veggies), 4):
                    VEGGIES.append('none')

            if flag == False:
                in_dir = input('Is the recipe file in the current directory and a *.txt file? (y/n)')
            if in_dir =='y':
                full_path = recipe + '.txt'
            elif in_dir == 'n':
                file_path = input('Recipe file to acces by path:  ')
                full_path = os.path.abspath(file_path)

            database.Add_to_db(recipe, meat, VEGGIES, starch, full_path)
            go_on = input('Keep adding? (y/n): ').lower()
            if go_on == 'n':
                keep_adding = False
        
    elif db_instruction == 'delete':
        keep_deleting = True
        while keep_deleting == True:
            to_be_deleted = input("Recipe name to delete: ").lower()
            database.Delete_from_db(to_be_deleted)
            #cur.execute(query)
            #conn.commit()
    
            go_on = input('Keep deleting? (y/n): ')
            if go_on == 'n':
                keep_deleting = False
        
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
    starch = input('starch: ').lower()
    recipes = database.Find_recipe(meat, VEGGIES, int(num_veggies), starch)
    stop = False
    while stop == False:
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
            elif search_again == 'n':
                stop = True
                
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
        elif instruction == 'database':
            DB()
        elif instruction == 'recipe':
            RECIPES()
        go_on = input('Do you want to do something else? (y/n): ')
        if go_on == 'n':
            keep_going = False

if __name__ == '__main__':
        main()
