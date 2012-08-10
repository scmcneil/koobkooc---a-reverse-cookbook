import sys, os
from PyQt4 import QtGui

class Screen5(QtGui.QWizardPage):
    def __init__(self, parent):
        super(Screen5, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.textEdit = QtGui.QTextEdit()
        openFile = QtGui.QPushButton('Open a File', self)
        openFile.clicked.connect(self.showDialog)
        label = QtGui.QLabel('Type in recipe or read in from file')
        #openFile.resize(openFile.sizeHint())
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(pic, 1, 0)
        grid.addWidget(label, 2, 0)
        grid.addWidget(self.textEdit, 3, 0, 2, 0)
        grid.addWidget(openFile, 5, 0)
        self.setLayout(grid)
        
    def showDialog(self):
        cwd = os.getcwd()
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', cwd)
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.textEdit.setText(data)

class Screen4(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen4, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
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
        starchRadio1 = QtGui.QRadioButton('&Rice', self)
        starchRadio2 = QtGui.QRadioButton('&Noodles', self)
        starchRadio3 = QtGui.QRadioButton('&Potatoes', self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        #grid.addWidget(pic)
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
        grid.addWidget(starchRadio1, 8, 1)
        grid.addWidget(starchRadio2, 9, 1)
        grid.addWidget(starchRadio3, 10, 1)
        self.setLayout(grid)


class Screen3(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen3, self).__init__()
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
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
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen3(wizard))
    wizard.addPage(Screen4(wizard))
    wizard.addPage(Screen5(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
