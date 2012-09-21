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
        label = QtGui.QLabel('Edit recipe text')
        self.textEdit.setText(intermediary.get_recipe())
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.textEdit, 3, 0, 4, 0)
        self.setLayout(grid)

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
        #recipe = self.nameShow.currentItem().text()
        print(text)
        database.Find_for_edit(text)
        self.meatEdit.setText(intermediary.get_meat())
        VEGGIES = intermediary.get_veggies()
        self.veggie1Edit.setText(VEGGIES[0])
        self.veggie2Edit.setText(VEGGIES[1])
        self.veggie3Edit.setText(VEGGIES[2])
        self.veggie4Edit.setText(VEGGIES[3])
        print(intermediary.get_name())

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
    wizard.addPage(Screen6(wizard))
    #wizard.addPage(Screen7(wizard))
    wizard.addPage(Screen8(wizard))
    wizard.addPage(Screen9(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
