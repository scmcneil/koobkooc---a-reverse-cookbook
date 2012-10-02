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
    Construction_screen = 16
    def __init__(self, parent=None):
        super(wizard, self).__init__()
        self.resize(720,650)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + '/images/koobkooc.jpg'))
        #Add the screens to the wizard
        self.setPage(wizard.Open_screen, Screen1(self))
        self.setPage(wizard.DB_function_screen, Screen2(self))
        self.setPage(wizard.Type_to_add, Screen3(self))
        self.setPage(wizard.Set_parameters, Screen4(self))
        self.setPage(wizard.Set_recipe, Screen5(self))
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
        self.check1 = QtGui.QCheckBox('&Database', self)
        self.check1.move(225, 275)
        self.check1.stateChanged.connect(self.nextId)
        self.check2 = QtGui.QCheckBox('&Recipe Lookup', self)
        self.check2.move(225, 300)
        self.check2.stateChanged.connect(self.nextId)
    def nextId(self):
        if self.check1.checkState() == 2:
            return wizard.DB_function_screen
        else:
            return wizard.Construction_screen

class Screen2(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen2, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/images/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("What database function would you like to perform?", self)
        self.label.move(225, 250)
        self.check1 = QtGui.QCheckBox('&Add a Recipe', self)
        self.check1.move(225, 275)
        self.check1.stateChanged.connect(self.nextId)
        self.check2 = QtGui.QCheckBox('&Edit a Recipe', self)
        self.check2.move(225, 300)
        self.check2.stateChanged.connect(self.nextId)
        self.check3 = QtGui.QCheckBox('&Delete a Recipe', self)
        self.check3.move(225, 325)
        self.check3.stateChanged.connect(self.nextId)
    def nextId(self):
        if self.check1.checkState() == 2:
            return wizard.Type_to_add
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
        print('\n', intermediary.get_recipe())
        database.ADD()
        

if ( __name__ == '__main__' ):
    app = None

    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    wizard = wizard()
    wizard.show()
    if ( app ):
        app.exec_()
