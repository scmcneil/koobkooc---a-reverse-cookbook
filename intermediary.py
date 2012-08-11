#Copyright Sheena C. McNeil

import sys, os

RECIPE_TYPE = ''
NAME = 'none'
MEAT = 'none'
VEGGIE1 = 'none'
VEGGIE2 = 'none'
VEGGIE3 = 'none'
VEGGIE4 = 'none'
STARCH = 'none'
RECIPE = ''

def set_types(recipe_type):
    RECIPE_TYPE = recipe_type

def set_name(name):
    global NAME
    NAME = name
    #print(NAME)

def set_meat(meat):
    global MEAT
    MEAT = meat
    #print(MEAT)

def set_veggie1(veggie1):
    global VEGGIE1
    VEGGIE1 = veggie1
    #print(VEGGIE1)

def set_veggie2(veggie2):
    global VEGGIE2
    VEGGIE2 = veggie2
    #print(VEGGIE2)

def set_veggie3(veggie3):
    global VEGGIE3
    VEGGIE3 = veggie3
    #print(VEGGIE3)

def set_veggie4(veggie4):
    global VEGGIE4
    VEGGIE4 = veggie4
    #print(VEGGIE4)

def set_starch(starch):
    global STARCH
    STARCH = starch
    #print(STARCH)

def set_recipe(recipe):
    global RECIPE
    RECIPE = recipe
    #print(RECIPE)

def send_the_things():
    VEGGIES = [VEGGIE1, VEGGIE2, VEGGIE3, VEGGIE4]
    #print(VEGGIES)
    return NAME, MEAT, VEGGIES, STARCH, RECIPE

def get_recipe_type():
    return RECIPE_TYPE

def get_name():
    #print(NAME)
    return NAME

def get_meat():
    return MEAT

def get_veggies():
    VEGGIES = [VEGGIE1, VEGGIE2, VEGGIE3, VEGGIE4]
    return VEGGIES

def get_recipe():
    return RECIPE

def get_starch():
    return STARCH




