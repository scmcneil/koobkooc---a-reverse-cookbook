import sys, os
from PyQt4 import QtGui, QtCore

class wizard(QtGui.QWizard):
    #Give each screen an id number
    Open_screen = 1
    DB_function_screen = 2
    Construction_screen = 3
    def __init__(self, parent=None):
        super(wizard, self).__init__()
        self.resize(720,650)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon(os.getcwd() + '/images/koobkooc.jpg'))
        #Add the screens to the wizard
        self.setPage(wizard.Open_screen, Screen1(self))
        self.setPage(wizard.DB_function_screen, Screen2(self))
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
        return wizard.Construction_screen

if ( __name__ == '__main__' ):
    app = None

    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    wizard = wizard()
    wizard.show()
    if ( app ):
        app.exec_()
