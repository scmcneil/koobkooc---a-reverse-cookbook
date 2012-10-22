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
    global RECIPE_TYPE
    RECIPE_TYPE = recipe_type

def set_name(name):
    global NAME
    NAME = str(name).lower()

def set_meat(meat):
    global MEAT
    MEAT = str(meat).lower()

def set_veggie1(veggie1):
    global VEGGIE1
    VEGGIE1 = str(veggie1).lower()

def set_veggie2(veggie2):
    global VEGGIE2
    VEGGIE2 = str(veggie2).lower()

def set_veggie3(veggie3):
    global VEGGIE3
    VEGGIE3 = str(veggie3).lower()

def set_veggie4(veggie4):
    global VEGGIE4
    VEGGIE4 = str(veggie4).lower()

def set_starch(starch):
    global STARCH
    STARCH = str(starch).lower()

def set_recipe(recipe):
    global RECIPE
    RECIPE = str(recipe)

def send_the_things():
    VEGGIES = [VEGGIE1, VEGGIE2, VEGGIE3, VEGGIE4]
    return NAME, MEAT, VEGGIES, STARCH, RECIPE

def get_recipe_type():
    return RECIPE_TYPE

def get_name():
    return NAME

def get_meat():
    return MEAT

def get_veggies():
    VEGGIES = [VEGGIE1, VEGGIE2, VEGGIE3, VEGGIE4]
    return VEGGIES

def get_veggies_for_search():
    VEGGIES = []
    if VEGGIE1 != 'none':
        VEGGIES.append(VEGGIE1)
    if VEGGIE2 != 'none':
        VEGGIES.append(VEGGIE2)
    if VEGGIE3 != 'none':
        VEGGIES.append(VEGGIE3)
    if VEGGIE4 != 'none':
        VEGGIES.append(VEGGIE4)

    return VEGGIES

def get_recipe():
    return RECIPE

def get_starch():
    return STARCH




