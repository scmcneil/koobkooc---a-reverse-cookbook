#Copyright Sheena C. McNeil

import database, intermediary
import sys, os
from PyQt4 import QtGui

#This sequence of screen allows the user to add a recipe to the database

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
        
    def showDialog(self):
        #Create a pop-up file browser to select a file to open
        cwd = os.getcwd()
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', cwd)
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.textEdit.setText(data)

    def add_recipe(self):
        #add the recipe and parameters to the database
        recipe = self.textEdit.toPlainText()
        print(recipe)
        intermediary.set_recipe(recipe)
        database.ADD()
            

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

if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon(os.getcwd() + '/images/koobkooc.jpg'))
    wizard.setOption(QtGui.QWizard.NoCancelButton)
    wizard.addPage(Screen3(wizard))
    wizard.addPage(Screen4(wizard))
    wizard.addPage(Screen5(wizard))
    wizard.exec_()
    
    # execute the application if we've created it

    if ( app ):
        app.exec_()
