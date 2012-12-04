import sys, os
from PyQt4 import QtGui, QtCore
import intermediary, database

class wizard(QtGui.QWizard):
    #Give each screen an id number
    Open_screen = 1
    DB_function_screen = 2
    Type_to_add = 3
    Set_parameters = 4
    Set_recipe = 5
    Type_to_edit = 6
    Edit_main_parameters = 8
    Edit_recipe = 9
    Type_to_delete = 10
    Select_main_to_delete = 11
    Type_to_search = 12
    Select_main_parameters = 13
    Select_recipe = 14
    View_reicpe = 15
    Construction_screen = 16
    Set_side_parameters = 17
    Edit_side_parameters = 18
    Select_side_to_delete = 19
    Select_side_parameters = 20
    Set_side_dish_relationship = 21
    def __init__(self, parent=None):
        super(wizard, self).__init__()
        self.resize(720,650)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + '/images/koobkooc.jpg'))
        self.setWizardStyle(QtGui.QWizard.ModernStyle)
        #Add the screens to the wizard
        self.setPage(wizard.Open_screen, OpenScreen(self))
        self.setPage(wizard.DB_function_screen, DBFunctionScreen(self))
        self.setPage(wizard.Type_to_add, TypeToAdd(self))
        self.setPage(wizard.Set_parameters, SetMainParameters(self))
        self.setPage(wizard.Set_recipe, SetRecipe(self))
        self.setPage(wizard.Type_to_edit, TypeToEdit(self))
        self.setPage(wizard.Edit_main_parameters, EditMainParameters(self))
        self.setPage(wizard.Edit_recipe, EditRecipe(self))
        self.setPage(wizard.Type_to_delete, TypeToDelete(self))
        self.setPage(wizard.Select_main_to_delete, SelectMainToDelete(self))
        self.setPage(wizard.Type_to_search, TypeToSearch(self))
        self.setPage(wizard.Select_main_parameters, SelectMainParameters(self))
        self.setPage(wizard.Select_recipe, SelectRecipe(self))
        self.setPage(wizard.View_reicpe, ViewRecipe(self))
        self.setPage(wizard.Construction_screen, UnderConstruction(self))
        self.setPage(wizard.Set_side_parameters, SetSideParameters(self))
        self.setPage(wizard.Edit_side_parameters, EditSideParameters(self))
        self.setPage(wizard.Select_side_to_delete, SelectSideToDelete(self))
        self.setPage(wizard.Select_side_parameters, SelectSideParameters(self))
        self.setPage(wizard.Set_side_dish_relationship, SetSideDishRelationship(self))
        self.setStartId(1)
        
class UnderConstruction(QtGui.QWizardPage):
    #This is a temporary page
    #Once the rest of the GUI is added in to this part, this page will go away
    def __init__(self, parent):
        super(UnderConstruction, self).__init__(parent)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/under_construction.jpg"))

class OpenScreen(QtGui.QWizardPage):
    #Screen that appears when the program is run
    def __init__(self, parent=None):
        super(OpenScreen, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel("What action would you like to take?", self)
        label.move(225, 250)
        #RadioButtons for control
        self.check1 = QtGui.QRadioButton('&Database', self)
        self.check1.move(225, 275)
        self.check2 = QtGui.QRadioButton('&Recipe Lookup', self)
        self.check2.move(225, 300)
        self.nextId()
    def nextId(self):
        if self.check1.isChecked():
            return wizard.DB_function_screen
        elif self.check2.isChecked():
            return wizard.Type_to_search
        else:
            return wizard.Type_to_search

class DBFunctionScreen(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(DBFunctionScreen, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What database function would you like to perform?", self)
        self.label.move(225, 250)
        #RadioButtons for control
        self.check1 = QtGui.QRadioButton('&Add a Recipe', self)
        self.check1.move(225, 275)
        self.check2 = QtGui.QRadioButton('&Edit a Recipe', self)
        self.check2.move(225, 300)
        self.check3 = QtGui.QRadioButton('&Delete a Recipe', self)
        self.check3.move(225, 325)
    def nextId(self):
        #Determine which screen to go to next
        if self.check1.isChecked():
            return wizard.Type_to_add
        elif self.check2.isChecked():
            return wizard.Type_to_edit
        elif self.check3.isChecked():
            return wizard.Type_to_delete
        else:
            return wizard.Construction_screen

class TypeToAdd(QtGui.QWizardPage):
    #Select the type of dish to add to the database
    def __init__(self, parent=None):
        super(TypeToAdd, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to add?", self)
        self.label.move(225, 250)
        self.mainRadio = QtGui.QRadioButton('&Main Dish', self)
        self.mainRadio.move(225, 275)
        self.sideRadio = QtGui.QRadioButton('&Side Dish', self)
        self.sideRadio.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.mainRadio.isChecked():
            intermediary.set_type('main')
            return wizard.Set_parameters
        #Side dishes not supported yet, so redirect to construction screen
        elif self.sideRadio.isChecked():
            intermediary.set_type('side')
            return wizard.Set_side_parameters
        else:
            return wizard.Set_parameters

class SetMainParameters(QtGui.QWizardPage):
    #set the search parameters and name for the dish
    def __init__(self, parent=None):
        super(SetMainParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Add a recipe')
        name = QtGui.QLabel('Recipe Name')
        meat = QtGui.QLabel('Meat')
        veggie1 = QtGui.QLabel('Veggie 1')
        veggie2 = QtGui.QLabel('Veggie 2')
        veggie3 = QtGui.QLabel('Veggie 3')
        veggie4 = QtGui.QLabel('Veggie 4')
        starch = QtGui.QLabel('Served on')
        
        nameEdit = QtGui.QLineEdit()
        meatEdit = QtGui.QLineEdit()
        veggie1Edit = QtGui.QLineEdit()
        veggie2Edit = QtGui.QLineEdit()
        veggie3Edit = QtGui.QLineEdit()
        veggie4Edit = QtGui.QLineEdit()
        self.starchRadio1 = QtGui.QRadioButton('&Rice', self)
        self.starchRadio2 = QtGui.QRadioButton('&Noodles', self)
        self.starchRadio3 = QtGui.QRadioButton('&Potatoes', self)

        nameEdit.textChanged[str].connect(self.name_changed)
        meatEdit.textChanged[str].connect(self.meat_changed)
        veggie1Edit.textChanged[str].connect(self.veggie1_changed)
        veggie2Edit.textChanged[str].connect(self.veggie2_changed)
        veggie3Edit.textChanged[str].connect(self.veggie3_changed)
        veggie4Edit.textChanged[str].connect(self.veggie4_changed)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(name, 2, 0)
        grid.addWidget(nameEdit, 2, 1)
        grid.addWidget(meat, 3, 0)
        grid.addWidget(meatEdit, 3, 1)
        grid.addWidget(veggie1, 4, 0)
        grid.addWidget(veggie1Edit, 4, 1)
        grid.addWidget(veggie2, 5, 0)
        grid.addWidget(veggie2Edit, 5, 1)
        grid.addWidget(veggie3, 6, 0)
        grid.addWidget(veggie3Edit, 6, 1)
        grid.addWidget(veggie4, 7, 0)
        grid.addWidget(veggie4Edit, 7, 1)
        grid.addWidget(starch, 8, 0)
        grid.addWidget(self.starchRadio1, 8, 1)
        grid.addWidget(self.starchRadio2, 9, 1)
        grid.addWidget(self.starchRadio3, 10, 1)
        self.setLayout(grid)
        
        self.nextId()

    #Take the input from the line-edits and sets it in the intermediary class
    def name_changed(self, text):
        intermediary.set_name(text)

    def meat_changed(self, text):
        intermediary.set_meat(text)

    def veggie1_changed(self, text):
        intermediary.set_veggie1(text)

    def veggie2_changed(self, text):
        intermediary.set_veggie2(text)

    def veggie3_changed(self, text):
        intermediary.set_veggie3(text)

    def veggie4_changed(self, text):
        intermediary.set_veggie4(text)

    def nextId(self):
        if self.starchRadio1.isChecked():
            intermediary.set_starch('Rice')
        elif self.starchRadio2.isChecked():
            intermediary.set_starch('Noodles')
        elif self.starchRadio3.isChecked():
            intermediary.set_starch('Potatoes')
        return wizard.Set_recipe

class SetSideParameters(QtGui.QWizardPage):
    def __init__(self, parent):
        super(SetSideParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Add a Side Dish')
        name = QtGui.QLabel('Recipe Name')
        ingredient1 = QtGui.QLabel('Ingredient 1')
        ingredient2 = QtGui.QLabel('Ingredient 2')
        ingredient3 = QtGui.QLabel('Ingredient 3')
        ingredient4 = QtGui.QLabel('Ingredient 4')
        ingredient5 = QtGui.QLabel('Ingredient 5')
        ingredient6 = QtGui.QLabel('Ingredient 6')
        
        nameEdit = QtGui.QLineEdit()
        self.ingredient1Edit = QtGui.QLineEdit()
        self.ingredient2Edit = QtGui.QLineEdit()
        self.ingredient3Edit = QtGui.QLineEdit()
        self.ingredient4Edit = QtGui.QLineEdit()
        self.ingredient5Edit = QtGui.QLineEdit()
        self.ingredient6Edit = QtGui.QLineEdit()

        nameEdit.textChanged[str].connect(self.name_changed)
        self.ingredient1Edit.textChanged[str].connect(self.ingredient1_changed)
        self.ingredient2Edit.textChanged[str].connect(self.ingredient2_changed)
        self.ingredient3Edit.textChanged[str].connect(self.ingredient3_changed)
        self.ingredient4Edit.textChanged[str].connect(self.ingredient4_changed)
        self.ingredient5Edit.textChanged[str].connect(self.ingredient5_changed)
        self.ingredient6Edit.textChanged[str].connect(self.ingredient6_changed)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(name, 2, 0)
        grid.addWidget(nameEdit, 2, 1)
        grid.addWidget(ingredient1, 4, 0)
        grid.addWidget(self.ingredient1Edit, 4, 1)
        grid.addWidget(ingredient2, 5, 0)
        grid.addWidget(self.ingredient2Edit, 5, 1)
        grid.addWidget(ingredient3, 6, 0)
        grid.addWidget(self.ingredient3Edit, 6, 1)
        grid.addWidget(ingredient4, 7, 0)
        grid.addWidget(self.ingredient4Edit, 7, 1)
        grid.addWidget(ingredient5, 8, 0)
        grid.addWidget(self.ingredient5Edit, 8, 1)
        grid.addWidget(ingredient6, 9, 0)
        grid.addWidget(self.ingredient6Edit, 9, 1)
        self.setLayout(grid)
        self.nextId()
        
    def name_changed(self, text):
        intermediary.set_name(text)

    def ingredient1_changed(self, text):
        intermediary.set_ingredient('1', text)

    def ingredient2_changed(self, text):
        intermediary.set_ingredient('2', text)

    def ingredient3_changed(self, text):
        intermediary.set_ingredient('3', text)

    def ingredient4_changed(self, text):
        intermediary.set_ingredient('4', text)

    def ingredient5_changed(self, text):
        intermediary.set_ingredient('5', text)

    def ingredient6_changed(self, text):
        intermediary.set_ingredient('6', text)

    def nextId(self):
        intermediary.set_type('side')
        return wizard.Set_recipe


class SetRecipe(QtGui.QWizardPage):
    def __init__(self, parent):
        super(SetRecipe, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.textEdit = QtGui.QTextEdit()
        openFile = QtGui.QPushButton('Open a File', self)
        openFile.clicked.connect(self.showDialog)
        label = QtGui.QLabel('Type in recipe or read in from file')
        addButton = QtGui.QPushButton('Add to database')
        addButton.clicked.connect(self.add_recipe)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.textEdit, 3, 0, 2, 0)
        grid.addWidget(openFile, 5, 0)
        grid.addWidget(addButton, 6, 0)
        self.setLayout(grid)
        self.nextId()

    def nextId(self):
        dish_type =  intermediary.get_type()
        if dish_type == 'main':
            #Makes the 'Final' button appear
            return -1
        elif dish_type == 'side':
            return wizard.Set_side_dish_relationship
    
    def showDialog(self):
        #Create a pop-up file browser to select a file to open
        cwd = os.getcwd()
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', cwd)
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.textEdit.setText(data)
        self.nextId()

    def add_recipe(self):
        #add the recipe and parameters to the database
        recipe = self.textEdit.toPlainText()
        intermediary.set_recipe(recipe)
        dish_type = intermediary.get_type()
        if dish_type == 'main':
            database.ADD_MAIN()
        elif dish_type == 'side':
            database.ADD_SIDE()

class SetSideDishRelationship(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SetSideDishRelationship, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        all_recipes = database.get_recipe_names('main')
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        label = QtGui.QLabel('Select a main dish to delete')
        addButton = QtGui.QPushButton('&Add Relationship')
        addButton.clicked.connect(self.add_relationship)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.recipes, 3, 0, 4, 0)
        grid.addWidget(addButton, 7, 0)
        self.setLayout(grid)
        self.nextId()

    def nextId(self):
        #Makes the 'Final' button appear
        return -1

    def listclicked(self, item):
        #Get the name of the recipe to be deleted
        recipe = str(self.recipes.currentItem().text()).lower()
        intermediary.set_relationship(intermediary.get_name(), recipe)

    def add_relationship(self):
        relation = intermediary.get_relationship()
        database.ADD_RELATIONSHIP(relation)

        #reset the list of recipes
        self.recipes.clear()
        all_recipes = database.get_recipes_not_related(database.get_recipe_id(intermediary.get_name()))
        print(all_recipes)
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(database.get_recipe_name(x))
                self.recipes.addItem(item)

class TypeToEdit(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(TypeToEdit, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to edit?", self)
        self.label.move(225, 250)
        self.mainRadio = QtGui.QRadioButton('&Main Dish', self)
        self.mainRadio.move(225, 275)
        self.sideRadio = QtGui.QRadioButton('&Side Dish', self)
        self.sideRadio.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.mainRadio.isChecked():
            return wizard.Edit_main_parameters
        elif self.sideRadio.isChecked():
            return wizard.Edit_side_parameters
        else:
            return wizard.Edit_main_parameters

class EditMainParameters(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(EditMainParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Edit a main dish')
        name = QtGui.QLabel('Recipe Name')
        meat = QtGui.QLabel('Meat')
        veggie1 = QtGui.QLabel('Veggie 1')
        veggie2 = QtGui.QLabel('Veggie 2')
        veggie3 = QtGui.QLabel('Veggie 3')
        veggie4 = QtGui.QLabel('Veggie 4')
        starch = QtGui.QLabel('Served on')
        
        self.nameShow = QtGui.QComboBox(self)
        self.nameShow.addItem('---select---')
        self.nameShow.activated[str].connect(self.listclicked)
        all_recipes = database.get_recipe_names('main')
        if len(all_recipes) > 0:
            for x in all_recipes:
                self.nameShow.addItem(x)
        
        self.meatEdit = QtGui.QLineEdit()
        self.veggie1Edit = QtGui.QLineEdit()
        self.veggie2Edit = QtGui.QLineEdit()
        self.veggie3Edit = QtGui.QLineEdit()
        self.veggie4Edit = QtGui.QLineEdit()
        self.starchRadio1 = QtGui.QRadioButton('&Rice', self)
        self.starchRadio2 = QtGui.QRadioButton('&Noodles', self)
        self.starchRadio3 = QtGui.QRadioButton('&Potatoes', self)
        
        self.meatEdit.textChanged[str].connect(self.meat_changed)
        self.veggie1Edit.textChanged[str].connect(self.veggie1_changed)
        self.veggie2Edit.textChanged[str].connect(self.veggie2_changed)
        self.veggie3Edit.textChanged[str].connect(self.veggie3_changed)
        self.veggie4Edit.textChanged[str].connect(self.veggie4_changed)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(name, 2, 0)
        grid.addWidget(self.nameShow, 2, 1)
        grid.addWidget(meat, 3, 0)
        grid.addWidget(self.meatEdit, 3, 1)
        grid.addWidget(veggie1, 4, 0)
        grid.addWidget(self.veggie1Edit, 4, 1)
        grid.addWidget(veggie2, 5, 0)
        grid.addWidget(self.veggie2Edit, 5, 1)
        grid.addWidget(veggie3, 6, 0)
        grid.addWidget(self.veggie3Edit, 6, 1)
        grid.addWidget(veggie4, 7, 0)
        grid.addWidget(self.veggie4Edit, 7, 1)
        grid.addWidget(starch, 8, 0)
        grid.addWidget(self.starchRadio1, 8, 1)
        grid.addWidget(self.starchRadio2, 9, 1)
        grid.addWidget(self.starchRadio3, 10, 1)
        self.setLayout(grid)

    def listclicked(self, text):
        database.FIND_MAIN(text)
        intermediary.set_id(database.get_recipe_id(text))
        intermediary.set_type('main')
        self.veggie1Edit.clear()
        self.veggie2Edit.clear()
        self.veggie3Edit.clear()
        self.veggie4Edit.clear()
        if intermediary.get_meat() != 'none':
            self.meatEdit.setText(intermediary.get_meat().title())
        VEGGIES = intermediary.get_veggies()
        if VEGGIES['1'] != '':
            self.veggie1Edit.setText(VEGGIES['1'].title())
        if VEGGIES['2'] != 'none':
            self.veggie2Edit.setText(VEGGIES['2'].title())
        if VEGGIES['3'] != 'none':
            self.veggie3Edit.setText(VEGGIES['3'].title())
        if VEGGIES['4'] != 'none':
            self.veggie4Edit.setText(VEGGIES['4'].title())
        starch = intermediary.get_starch().title()
        if starch == 'Rice':
            self.starchRadio1.setChecked(1)
        elif starch == 'Noodles':
            self.starchRadio2.setChecked(1)
        elif starch == 'Potatoes':
            self.starchRadio3.setChecked(1)

    def meat_changed(self, text):
        intermediary.set_meat(text)

    def veggie1_changed(self, text):
        intermediary.set_veggie1(text)

    def veggie2_changed(self, text):
        intermediary.set_veggie2(text)

    def veggie3_changed(self, text):
        intermediary.set_veggie3(text)

    def veggie4_changed(self, text):
        intermediary.set_veggie4(text)

    def nextId(self):
        if self.starchRadio1.isChecked():
            intermediary.set_starch('Rice')
        elif self.starchRadio2.isChecked():
            intermediary.set_starch('Noodles')
        elif self.starchRadio3.isChecked():
            intermediary.set_starch('Potatoes')
        return wizard.Edit_recipe

class EditSideParameters(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(EditSideParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Edit a side dish')
        name = QtGui.QLabel('Recipe Name')
        ingredient1 = QtGui.QLabel('Ingredient 1')
        ingredient2 = QtGui.QLabel('Ingredient 2')
        ingredient3 = QtGui.QLabel('Ingredient 3')
        ingredient4 = QtGui.QLabel('Ingredient 4')
        ingredient5 = QtGui.QLabel('Ingredient 5')
        ingredient6 = QtGui.QLabel('Ingredient 6')
        
        self.nameShow = QtGui.QComboBox(self)
        self.nameShow.addItem('---select---')
        self.nameShow.activated[str].connect(self.listclicked)
        all_recipes = database.get_recipe_names('side')
        if len(all_recipes) > 0:
            for x in all_recipes:
                self.nameShow.addItem(x)
        
        self.ingredient1Edit = QtGui.QLineEdit()
        self.ingredient2Edit = QtGui.QLineEdit()
        self.ingredient3Edit = QtGui.QLineEdit()
        self.ingredient4Edit = QtGui.QLineEdit()
        self.ingredient5Edit = QtGui.QLineEdit()
        self.ingredient6Edit = QtGui.QLineEdit()
        
        self.ingredient1Edit.textChanged[str].connect(self.ingredient1_changed)
        self.ingredient2Edit.textChanged[str].connect(self.ingredient2_changed)
        self.ingredient3Edit.textChanged[str].connect(self.ingredient3_changed)
        self.ingredient4Edit.textChanged[str].connect(self.ingredient4_changed)
        self.ingredient5Edit.textChanged[str].connect(self.ingredient5_changed)
        self.ingredient6Edit.textChanged[str].connect(self.ingredient6_changed)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(name, 2, 0)
        grid.addWidget(self.nameShow, 2, 1)
        grid.addWidget(ingredient1, 4, 0)
        grid.addWidget(self.ingredient1Edit, 4, 1)
        grid.addWidget(ingredient2, 5, 0)
        grid.addWidget(self.ingredient2Edit, 5, 1)
        grid.addWidget(ingredient3, 6, 0)
        grid.addWidget(self.ingredient3Edit, 6, 1)
        grid.addWidget(ingredient4, 7, 0)
        grid.addWidget(self.ingredient4Edit, 7, 1)
        grid.addWidget(ingredient5, 8, 0)
        grid.addWidget(self.ingredient5Edit, 8, 1)
        grid.addWidget(ingredient6, 9, 0)
        grid.addWidget(self.ingredient6Edit, 9, 1)
        self.setLayout(grid)
        self.nextId()

    def listclicked(self, text):
        database.FIND_SIDE(text)
        intermediary.set_id(database.get_recipe_id(text))
        intermediary.set_type('side')
        self.ingredient1Edit.clear()
        self.ingredient2Edit.clear()
        self.ingredient3Edit.clear()
        self.ingredient4Edit.clear()
        self.ingredient5Edit.clear()
        self.ingredient6Edit.clear()
        INGREDIENTS = intermediary.get_ingredients()
        if INGREDIENTS['1'] != '':
            self.ingredient1Edit.setText(INGREDIENTS['1'].title())
        if INGREDIENTS['2'] != '':
            self.ingredient2Edit.setText(INGREDIENTS['2'].title())
        if INGREDIENTS['3'] != '':
            self.ingredient3Edit.setText(INGREDIENTS['3'].title())
        if INGREDIENTS['4'] != '':
            self.ingredient4Edit.setText(INGREDIENTS['4'].title())
        if INGREDIENTS['5'] != '':
            self.ingredient5Edit.setText(INGREDIENTS['5'].title())
        if INGREDIENTS['6'] != '':
            self.ingredient6Edit.setText(INGREDIENTS['6'].title())

    def ingredient1_changed(self, text):
        intermediary.set_ingredient('1', text)

    def ingredient2_changed(self, text):
        intermediary.set_ingredient('2', text)

    def ingredient3_changed(self, text):
        intermediary.set_ingredient('3', text)

    def ingredient4_changed(self, text):
        intermediary.set_ingredient('4', text)

    def ingredient5_changed(self, text):
        intermediary.set_ingredient('5', text)

    def ingredient6_changed(self, text):
        intermediary.set_ingredient('6', text)

    def nextId(self):
        return wizard.Edit_recipe

class EditRecipe(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(EditRecipe, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.textEdit = QtGui.QTextEdit()
        fillButton = QtGui.QPushButton('Fill')
        fillButton.clicked.connect(self.fill)
        label = QtGui.QLabel('Edit recipe text')
        editButton = QtGui.QPushButton('Commit edits to database')
        editButton.clicked.connect(self.edit_recipe)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 0, 0)
        grid.addWidget(fillButton, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.textEdit, 3, 0, 4, 0)
        grid.addWidget(editButton, 7, 0)
        self.setLayout(grid)
        self.nextId()

    def nextId(self):
        #Makes the 'Final' button appear
        return -1

    def edit_recipe(self):
        #update the recipe and parameters in the database
        recipe_name = intermediary.get_name()
        recipe = self.textEdit.toPlainText()
        intermediary.set_recipe(recipe)
        if intermediary.get_type() == 'main':
	        database.EDIT_MAIN(recipe_name)
        elif intermediary.get_type() == 'side':
            database.EDIT_SIDE(recipe_name)

    def fill(self):
        #fills in textEdit with the recipe text from the database
        self.textEdit.clear()
        recipe_text = intermediary.get_recipe()
        self.textEdit.insertPlainText(recipe_text)

class TypeToDelete(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(TypeToDelete, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to delete?", self)
        self.label.move(225, 250)
        self.mainRadio = QtGui.QRadioButton('&Main Dish', self)
        self.mainRadio.move(225, 275)
        self.sideRadio = QtGui.QRadioButton('&Side Dish', self)
        self.sideRadio.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.mainRadio.isChecked():
            intermediary.set_type('main')
            return wizard.Select_main_to_delete
        elif self.sideRadio.isChecked():
            return wizard.Select_side_to_delete
        else:
            return wizard.Select_main_to_delete

class SelectMainToDelete(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectMainToDelete, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        all_recipes = database.get_recipe_names('main')
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        label = QtGui.QLabel('Select a main dish to delete')
        deleteButton = QtGui.QPushButton('&Delete')
        deleteButton.clicked.connect(self.delete_recipe)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.recipes, 3, 0, 4, 0)
        grid.addWidget(deleteButton, 7, 0)
        self.setLayout(grid)
        self.nextId()

    def nextId(self):
        #Makes the 'Final' button appear
        return -1

    def listclicked(self, item):
        #Get the name of the recipe to be deleted
        recipe = str(self.recipes.currentItem().text()).lower()
        intermediary.set_name(recipe)

    def delete_recipe(self):
        recipe = intermediary.get_name()
        database.DELETE(recipe)

        #reset the list of recipes
        self.recipes.clear()
        all_recipes = database.get_recipe_names('main')
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        
class SelectSideToDelete(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectSideToDelete, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        all_recipes = database.get_recipe_names('side')
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        label = QtGui.QLabel('Select a side dish to delete')
        deleteButton = QtGui.QPushButton('&Delete')
        deleteButton.clicked.connect(self.delete_recipe)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.recipes, 3, 0, 4, 0)
        grid.addWidget(deleteButton, 7, 0)
        self.setLayout(grid)
        self.nextId()

    def nextId(self):
        #Makes the 'Final' button appear
        return -1

    def listclicked(self, item):
        #Get the name of the recipe to be deleted
        recipe = str(self.recipes.currentItem().text()).lower()
        intermediary.set_name(recipe)

    def delete_recipe(self):
        recipe = intermediary.get_name()
        database.DELETE(recipe)
        #reset the list of recipes
        self.recipes.clear()
        all_recipes = database.get_recipe_names('side')
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)

class TypeToSearch(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(TypeToSearch, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to look up?", self)
        self.label.move(225, 250)
        self.mainRadio = QtGui.QRadioButton('&Main Dish', self)
        self.mainRadio.move(225, 275)
        self.sideRadio = QtGui.QRadioButton('&Side Dish', self)
        self.sideRadio.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.mainRadio.isChecked():
            return wizard.Select_main_parameters
        elif self.sideRadio.isChecked():
            return wizard.Select_side_parameters
        else:
            return wizard.Select_main_parameters

class SelectMainParameters(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectMainParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Find a recipe')
        meat = QtGui.QLabel('Meat')
        veggie1 = QtGui.QLabel('Veggie 1')
        veggie2 = QtGui.QLabel('Veggie 2')
        veggie3 = QtGui.QLabel('Veggie 3')
        veggie4 = QtGui.QLabel('Veggie 4')
        starch = QtGui.QLabel('Served on')

        meatSelect = QtGui.QComboBox(self)
        meatSelect.activated[str].connect(self.meatSelected)
        meatSelect.addItem('---select---')
        veggie1Select = QtGui.QComboBox(self)
        veggie1Select.activated[str].connect(self.veggie1Selected)
        veggie1Select.addItem('---select---')
        veggie2Select = QtGui.QComboBox(self)
        veggie2Select.activated[str].connect(self.veggie2Selected)
        veggie2Select.addItem('---select---')
        veggie3Select = QtGui.QComboBox(self)
        veggie3Select.activated[str].connect(self.veggie3Selected)
        veggie3Select.addItem('---select---')
        veggie4Select = QtGui.QComboBox(self)
        veggie4Select.activated[str].connect(self.veggie4Selected)
        veggie4Select.addItem('---select---')
        VEGGIES = database.get_veggie_names()
        for x in VEGGIES:
            veggie1Select.addItem(x)
            veggie2Select.addItem(x)
            veggie3Select.addItem(x)
            veggie4Select.addItem(x)
        MEAT = database.get_meat_names()
        for x in MEAT:
            meatSelect.addItem(x)
            
        self.starchRadio1 = QtGui.QRadioButton('&Rice', self)
        self.starchRadio2 = QtGui.QRadioButton('&Noodles', self)
        self.starchRadio3 = QtGui.QRadioButton('&Potatoes', self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(meat, 3, 0)
        grid.addWidget(meatSelect, 3, 1)
        grid.addWidget(veggie1, 4, 0)
        grid.addWidget(veggie1Select, 4, 1)
        grid.addWidget(veggie2, 5, 0)
        grid.addWidget(veggie2Select, 5, 1)
        grid.addWidget(veggie3, 6, 0)
        grid.addWidget(veggie3Select, 6, 1)
        grid.addWidget(veggie4, 7, 0)
        grid.addWidget(veggie4Select, 7, 1)
        grid.addWidget(starch, 8, 0)
        grid.addWidget(self.starchRadio1, 8, 1)
        grid.addWidget(self.starchRadio2, 9, 1)
        grid.addWidget(self.starchRadio3, 10, 1)
        self.setLayout(grid)

        self.nextId()

    def meatSelected(self, text):
        if text != '---select---':
            intermediary.set_meat(text) 
    def veggie1Selected(self, text):
        if text != '---select---':
            intermediary.set_veggie1(text) 
    def veggie2Selected(self, text):
        if text != '---select---':
            intermediary.set_veggie2(text) 
    def veggie3Selected(self, text):
        if text != '---select---':
            intermediary.set_veggie3(text) 
    def veggie4Selected(self, text):
        if text != '---select---':
            intermediary.set_veggie4(text)

    def nextId(self):
        intermediary.set_type('main')
        if self.starchRadio1.isChecked() == True:
            intermediary.set_starch('rice')
        elif self.starchRadio2.isChecked() == True:
            intermediary.set_starch('noodles')
        elif self.starchRadio3.isChecked() == True:
            intermediary.set_starch('potatoes')
        return wizard.Select_recipe

class SelectSideParameters(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectSideParameters, self).__init__()
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Find a recipe')
        ingredient1 = QtGui.QLabel('Ingredient 1')
        ingredient2 = QtGui.QLabel('Ingredient 2')
        ingredient3 = QtGui.QLabel('Ingredient 3')
        ingredient4 = QtGui.QLabel('Ingredient 4')
        ingredient5 = QtGui.QLabel('Ingredient 5')
        ingredient6 = QtGui.QLabel('Ingredient 6')

        ingredient1Select = QtGui.QComboBox(self)
        ingredient1Select.activated[str].connect(self.ingredient1Selected)
        ingredient1Select.addItem('---select---')
        ingredient2Select = QtGui.QComboBox(self)
        ingredient2Select.activated[str].connect(self.ingredient2Selected)
        ingredient2Select.addItem('---select---')
        ingredient3Select = QtGui.QComboBox(self)
        ingredient3Select.activated[str].connect(self.ingredient3Selected)
        ingredient3Select.addItem('---select---')
        ingredient4Select = QtGui.QComboBox(self)
        ingredient4Select.activated[str].connect(self.ingredient4Selected)
        ingredient4Select.addItem('---select---')
        ingredient5Select = QtGui.QComboBox(self)
        ingredient5Select.activated[str].connect(self.ingredient5Selected)
        ingredient5Select.addItem('---select---')
        ingredient6Select = QtGui.QComboBox(self)
        ingredient6Select.activated[str].connect(self.ingredient6Selected)
        ingredient6Select.addItem('---select---')
        INGREDIENTS = database.get_ingredient_names()
        for x in INGREDIENTS:
            ingredient1Select.addItem(x)
            ingredient2Select.addItem(x)
            ingredient3Select.addItem(x)
            ingredient4Select.addItem(x)
            ingredient5Select.addItem(x)
            ingredient6Select.addItem(x)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 0, 0)
        grid.addWidget(label, 1, 0)
        grid.addWidget(ingredient1, 4, 0)
        grid.addWidget(ingredient1Select, 4, 1)
        grid.addWidget(ingredient2, 5, 0)
        grid.addWidget(ingredient2Select, 5, 1)
        grid.addWidget(ingredient3, 6, 0)
        grid.addWidget(ingredient3Select, 6, 1)
        grid.addWidget(ingredient4, 7, 0)
        grid.addWidget(ingredient4Select, 7, 1)
        grid.addWidget(ingredient5, 8, 0)
        grid.addWidget(ingredient5Select, 8, 1)
        grid.addWidget(ingredient6, 9, 0)
        grid.addWidget(ingredient6Select, 9, 1)
        self.setLayout(grid)

        self.nextId()

    def ingredient1Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('1', text) 
    def ingredient2Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('2', text)  
    def ingredient3Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('3', text)  
    def ingredient4Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('4', text) 
    def ingredient5Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('5', text) 
    def ingredient6Selected(self, text):
        if text != '---select---':
            intermediary.set_ingredient('6', text) 

    def nextId(self):
        intermediary.set_type('side')
        return wizard.Select_recipe

class SelectRecipe(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectRecipe, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        intermediary.set_type('side')
        label = QtGui.QLabel('Select a recipe to view')
        self.searchButton = QtGui.QPushButton('Run Search', self)
        self.searchButton.clicked.connect(self.search)
        self.searchButton.move(350, 230)
        self.strictLabel = QtGui.QLabel('Strict Search?')
        self.strictRadio = QtGui.QRadioButton('&yes', self)
        self.nonstrictRadio = QtGui.QRadioButton('&no', self)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.strictLabel, 3, 0)
        grid.addWidget(self.strictRadio, 4, 0)
        grid.addWidget(self.nonstrictRadio, 5, 0)
        grid.addWidget(self.recipes, 6, 0, 4, 0)
        self.setLayout(grid)

    def search(self):
        self.recipes.clear()
        strict = False
        if self.strictRadio.isChecked():
            strict = True
        if intermediary.get_type() == 'main':
            MEAT = intermediary.get_meat()
            VEGGIES = intermediary.get_veggies()
            NUM = len(VEGGIES)
            STARCH = intermediary.get_starch()
            RECIPES = database.SEARCH_MAIN(MEAT, VEGGIES, STARCH, strict)
        elif intermediary.get_type() == 'side':
            INGREDIENTS = intermediary.get_ingredients()
            RECIPES = database.SEARCH_SIDE(INGREDIENTS, strict)
        if len(RECIPES) > 0:
            for x in RECIPES:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)

    def listclicked(self, item):
        recipe = str(self.recipes.currentItem().text())
        if intermediary.get_type() == 'main':
            database.FIND_MAIN(recipe)
        elif intermediary.get_type() == 'side':
            database.FIND_SIDE(recipe)

class ViewRecipe(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(ViewRecipe, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.textView = QtGui.QTextEdit()
        self.textView.setReadOnly(True)
        self.textView.setGeometry(10, 230, 680, 400)
        fillButton = QtGui.QPushButton('Fill', self)
        fillButton.move(10, 210)
        fillButton.clicked.connect(self.fill)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(pic)
        layout.addWidget(self.textView)
        self.setLayout(layout)
        self.nextId()

    def fill(self):
        #fills in textEdit with the recipe text from the database
        self.textView.clear()
        recipe_text = intermediary.get_recipe()
        self.textView.insertPlainText(recipe_text)

    def nextId(self):
        #Makes the 'Final' button appear
        return -1
        

if ( __name__ == '__main__' ):
    app = None

    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    wizard = wizard()
    wizard.show()
    if ( app ):
        app.exec_()
