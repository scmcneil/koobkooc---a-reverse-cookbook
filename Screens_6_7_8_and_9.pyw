import sys, os
import database, intermediary
from PyQt4 import QtGui

class Screen9(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen9, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.textEdit = QtGui.QTextEdit()
        fillButton = QtGui.QPushButton('Fill')
        fillButton.clicked.connect(self.fill)
        label = QtGui.QLabel('Edit recipe text')
        editButton = QtGui.QPushButton('Commit edits to database')
        editButton.clicked.connect(self.edit_recipe)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 0, 0)
        grid.addWidget(fillButton)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.textEdit, 3, 0, 4, 0)
        grid.addWidget(editButton, 7, 0)
        self.setLayout(grid)

    def edit_recipe(self):
        #update the recipe and parameters in the database

    def fill(self):
        recipe_text = intermediary.get_recipe()
        self.textEdit.insertPlainText(recipe_text)

class Screen8(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen8, self).__init__()
        self.initUI()

    def initUI(self):
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        label = QtGui.QLabel('Edit a recipe')
        name = QtGui.QLabel('Recipe Name')
        meat = QtGui.QLabel('Meat')
        veggie1 = QtGui.QLabel('Veggie 1')
        veggie2 = QtGui.QLabel('Veggie 2')
        veggie3 = QtGui.QLabel('Veggie 3')
        veggie4 = QtGui.QLabel('Veggie 4')
        starch = QtGui.QLabel('Served on')
        
        recipe = database.get_name()
        print (recipe)
        
        self.nameShow = QtGui.QComboBox(self)
        self.nameShow.addItem('---select---')
        self.nameShow.activated[str].connect(self.listclicked)
        all_recipes = database.Browse_db()
        if len(all_recipes) > 0:
            for x in all_recipes:
                print(x)
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
        #recipe = self.nameShow.currentItem().text()
        print(text)
        database.Find_for_edit(text)
        if intermediary.get_meat() != 'none':
            self.meatEdit.setText(intermediary.get_meat())
        VEGGIES = intermediary.get_veggies()
        if VEGGIES[0] != 'none':
            self.veggie1Edit.setText(VEGGIES[0])
        if VEGGIES[1] != 'none':
            self.veggie2Edit.setText(VEGGIES[1])
        if VEGGIES[2] != 'none':
            self.veggie3Edit.setText(VEGGIES[2])
        if VEGGIES[3] != 'none':
            self.veggie4Edit.setText(VEGGIES[3])
        starch = intermediary.get_starch()
        if starch == 'Rice':
            self.starchRadio1.setChecked(1)
        elif starch == 'Noodles':
            self.starchRadio2.setChecked(1)
        elif starch == 'Potatoes':
            self.starchRadio3.setChecked(1)
        #print(intermediary.get_recipe())
        #print(intermediary.get_name())

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

class Screen7(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen7, self).__init__()
        self.initUI()

    def initUI(self):
        spacer = QtGui.QLabel(self)
        spacer.setGeometry(0,0,10,225)
        spacer.setPixmap(QtGui.QPixmap(os.getcwd() + '/spacer.jpg'))
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.recipes = QtGui.QListWidget()
        all_recipes = database.Browse_db()
        if len(all_recipes) > 0:
            for x in all_recipes:
                print(x)
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        
        label = QtGui.QLabel('Select a recipe to edit')
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(spacer, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.recipes, 3, 0, 4, 0)
        self.setLayout(grid)
        
    def listclicked(self, item):
        recipe = self.recipes.currentItem().text()
        intermediary.set_name(recipe)
        print(intermediary.get_name())

class Screen6(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Screen6, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What type of recipe would you like to edit?", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Main Dish', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Side Dish', self)
        self.radio2.move(225, 300)


if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    #wizard.addPage(Screen6(wizard))
    #wizard.addPage(Screen7(wizard))
    wizard.addPage(Screen8(wizard))
    wizard.addPage(Screen9(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
