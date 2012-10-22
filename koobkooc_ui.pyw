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
    Edit_parameters = 8
    Edit_recipe = 9
    Type_to_delete = 10
    Select_to_delete = 11
    Type_to_search = 12
    Select_parameters = 13
    Select_recipe = 14
    View_reicpe = 15
    Construction_screen = 16
    def __init__(self, parent=None):
        super(wizard, self).__init__()
        self.resize(720,650)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + '/images/koobkooc.jpg'))
        self.setWizardStyle(QtGui.QWizard.ModernStyle)
        #Add the screens to the wizard
        self.setPage(wizard.Open_screen, Screen1(self))
        self.setPage(wizard.DB_function_screen, Screen2(self))
        self.setPage(wizard.Type_to_add, Screen3(self))
        self.setPage(wizard.Set_parameters, Screen4(self))
        self.setPage(wizard.Set_recipe, Screen5(self))
        self.setPage(wizard.Type_to_edit, Screen6(self))
        self.setPage(wizard.Edit_parameters, Screen8(self))
        self.setPage(wizard.Edit_recipe, Screen9(self))
        self.setPage(wizard.Type_to_delete, Screen10(self))
        self.setPage(wizard.Select_to_delete, Screen11(self))
        self.setPage(wizard.Type_to_search, Screen12(self))
        self.setPage(wizard.Select_parameters, Screen13(self))
        self.setPage(wizard.Select_recipe, Screen14(self))
        self.setPage(wizard.View_reicpe, Screen15(self))
        self.setPage(wizard.Construction_screen, UnderConstruction(self))
        self.setStartId(1)
        
class UnderConstruction(QtGui.QWizardPage):
    #This is a temporary page
    #Once the rest of the GUI is added in to this part, this page will go away
    def __init__(self, parent):
        super(UnderConstruction, self).__init__(parent)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/under_construction.jpg"))

class Screen1(QtGui.QWizardPage):
    #Screen that appears when the program is run
    def __init__(self, parent=None):
        super(Screen1, self).__init__()
        self.initUI()

    def initUI(self):
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
        if self.check1.isChecked() == True:
            return wizard.DB_function_screen
        elif self.check2.isChecked() == True:
            return wizard.Type_to_search
        else:
            return wizard.Construction_screen

class Screen2(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen2, self).__init__()
        self.initUI()

    def initUI(self):
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
        if self.check1.isChecked() == True:
            return wizard.Type_to_add
        elif self.check2.isChecked() == True:
            return wizard.Type_to_edit
        elif self.check3.isChecked() == True:
            return wizard.Type_to_delete
        else:
            return wizard.Construction_screen

class Screen3(QtGui.QWizardPage):
    #Select the type of dish to add to the database
    def __init__(self, parent=None):
        super(Screen3, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to add?", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Main Dish', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Side Dish', self)
        self.radio2.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.radio1.isChecked() == True:
            return wizard.Set_parameters
        #Side dishes not supported yet, so redirect to construction screen
        elif self.radio2.isChecked() == True:
            return wizard.Construction_screen
        else:
            return wizard.Construction_screen

class Screen4(QtGui.QWizardPage):
    #set the search parameters and name for the dish
    def __init__(self, parent=None):
        super(Screen4, self).__init__()
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
        setButton = QtGui.QPushButton('Set search parameters', self)
        setButton.clicked.connect(self.set_parameters)
        self.setLabel = QtGui.QLabel(self)

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
        grid.addWidget(setButton, 11, 0)
        grid.addWidget(self.setLabel, 11, 1)
        self.setLayout(grid)
        
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

    def set_parameters(self):
        if self.starchRadio1.isChecked() == True:
            intermediary.set_starch('Rice')
        elif self.starchRadio2.isChecked():
            intermediary.set_starch('Noodles')
        elif self.starchRadio3.isChecked():
            intermediary.set_starch('Potatoes')
        self.setLabel.setText('Parameters set!')

class Screen5(QtGui.QWizardPage):
    def __init__(self, parent):
        super(Screen5, self).__init__()
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
        self.nextId

    def nextId(self):
        #Makes the 'Final' button appear
        return -1
    
    def showDialog(self):
        #Create a pop-up file browser to select a file to open
        cwd = os.getcwd()
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', cwd)
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.textEdit.setText(data)
        self.nextId

    def add_recipe(self):
        #add the recipe and parameters to the database
        recipe = self.textEdit.toPlainText()
        print(recipe)
        intermediary.set_recipe(recipe)
        print('\n', intermediary.get_recipe())
        database.ADD()

class Screen6(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen6, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to edit?", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Main Dish', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Side Dish', self)
        self.radio2.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.radio1.isChecked() == True:
            return wizard.Edit_parameters
        #Side dishes not supported yet, so redirect to construction screen
        elif self.radio2.isChecked() == True:
            return wizard.Construction_screen
        else:
            return wizard.Construction_screen

class Screen8(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen8, self).__init__()
        self.initUI()

    def initUI(self):
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/images/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        label = QtGui.QLabel('Edit a recipe')
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
        all_recipes = database.Browse_db()
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

        setButton = QtGui.QPushButton('Re-set search parameters', self)
        setButton.clicked.connect(self.set_parameters)
        self.setLabel = QtGui.QLabel(self)
        
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
        grid.addWidget(setButton, 11, 0)
        grid.addWidget(self.setLabel, 11, 1)
        self.setLayout(grid)

    def listclicked(self, text):
        database.Find_for_edit(text)
        if intermediary.get_meat() != 'none':
            self.meatEdit.setText(intermediary.get_meat().title())
        VEGGIES = intermediary.get_veggies()
        if VEGGIES[0] != 'none':
            self.veggie1Edit.setText(VEGGIES[0].title())
        if VEGGIES[1] != 'none':
            self.veggie2Edit.setText(VEGGIES[1].title())
        if VEGGIES[2] != 'none':
            self.veggie3Edit.setText(VEGGIES[2].title())
        if VEGGIES[3] != 'none':
            self.veggie4Edit.setText(VEGGIES[3].title())
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

    def set_parameters(self):
        if self.starchRadio1.isChecked() == True:
            intermediary.set_starch('Rice')
        elif self.starchRadio2.isChecked():
            intermediary.set_starch('Noodles')
        elif self.starchRadio3.isChecked():
            intermediary.set_starch('Potatoes')
        self.setLabel.setText('Parameters re-set!')

class Screen9(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen9, self).__init__()
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
        database.Edit_recipe(recipe_name)
        print(intermediary.get_name())
        print('roar')

    def fill(self):
        #fills in textEdit with the recipe text from the database
        self.textEdit.clear()
        recipe_text = intermediary.get_recipe()
        self.textEdit.insertPlainText(recipe_text)

class Screen10(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen10, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to delete?", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Main Dish', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Side Dish', self)
        self.radio2.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.radio1.isChecked() == True:
            return wizard.Select_to_delete
        #Side dishes not supported yet, so redirect to construction screen
        elif self.radio2.isChecked() == True:
            return wizard.Construction_screen
        else:
            return wizard.Construction_screen

class Screen11(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen11, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        all_recipes = database.Browse_db()
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        label = QtGui.QLabel('Select a recipe to delete')
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
        recipe = self.recipes.currentItem().text().lower()
        intermediary.set_name(recipe)

    def delete_recipe(self):
        recipe = intermediary.get_name()
        database.Delete_from_db(recipe)

        #reset the list of recipes
        self.recipes.clear()
        all_recipes = database.Browse_db()
        if len(all_recipes) > 0:
            for x in all_recipes:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        
        

class Screen12(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen12, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to look up?", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Main Dish', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Side Dish', self)
        self.radio2.move(225, 300)

    def nextId(self):
        #Determine which screen to go to next
        if self.radio1.isChecked() == True:
            return wizard.Select_parameters
        #Side dishes not supported yet, so redirect to construction screen
        elif self.radio2.isChecked() == True:
            return wizard.Construction_screen
        else:
            return wizard.Construction_screen

class Screen13(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen13, self).__init__()
        self.initUI()

    def initUI(self):
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
        VEGGIES = database.Find_veggies()
        for x in VEGGIES:
            veggie1Select.addItem(x)
            veggie2Select.addItem(x)
            veggie3Select.addItem(x)
            veggie4Select.addItem(x)
        MEAT = database.Find_meat()
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
        if self.starchRadio1.isChecked() == True:
            intermediary.set_starch('rice')
        elif self.starchRadio2.isChecked() == True:
            intermediary.set_starch('noodles')
        elif self.starchRadio3.isChecked() == True:
            intermediary.set_starch('potatoes')
        return wizard.Select_recipe


class Screen14(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen14, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        #self.recipes.clicked.connect(self.listclicked)
        label = QtGui.QLabel('Select a recipe to view')
        self.searchButton = QtGui.QPushButton('Run Search', self)
        self.searchButton.clicked.connect(self.search)
        self.searchButton.move(155, 230)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.recipes, 3, 0, 4, 0)
        self.setLayout(grid)

    def search(self):
        MEAT = intermediary.get_meat()
        VEGGIES = intermediary.get_veggies_for_search()
        NUM = len(VEGGIES)
        STARCH = intermediary.get_starch()
        RECIPES = database.Find_recipe(MEAT, VEGGIES, NUM, STARCH)
        print(VEGGIES)
        print(RECIPES)
        if len(RECIPES) > 0:
            for x in RECIPES:
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)

    def listclicked(self, item):
        recipe = str(self.recipes.currentItem().text())
        #recipe_text = database.Recipe_text(recipe)
        database.Find_for_edit(recipe)

class Screen15(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen15, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.textView = QtGui.QTextBrowser()
        fillButton = QtGui.QPushButton('Fill', self)
        fillButton.move(10, 210)
        fillButton.clicked.connect(self.fill)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(self.textView, 3, 0, 8, 0)
        self.setLayout(grid)
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
