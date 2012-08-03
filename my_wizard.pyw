import sys, os
from PyQt4 import QtGui

class UnderConstruction(QtGui.QWizardPage):
    def __init__(self, parent):
        super(UnderConstruction, self).__init__(parent)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/under_construction.jpg"))

class Screen1(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen1, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))

        #btnTutorial = QtGui.QPushButton('Tutorial', self)
        #btnTutorial.clicked.connect(self.button_clicked)
        #btnTutorial.resize(btnTutorial.sizeHint())
        #btnTutorial.move(170, 555)
        
        #btnDatabase = QtGui.QPushButton('Database', self)
        #btnDatabase.clicked.connect(self.button_clicked)
        #btnDatabase.resize(btnDatabase.sizeHint())
        #btnDatabase.move(320, 555)
        
        #btnRecipeLookup = QtGui.QPushButton('Recipe Lookup', self)
        #btnRecipeLookup.clicked.connect(self.button_clicked)
        #btnRecipeLookup.resize(btnRecipeLookup.sizeHint())        
        #btnRecipeLookup.move(470, 555)

        #self.layout = QtGui.QVBoxLayout(self)
        #self.buttonGroup = QtGui.QVButtonGroup('Temp', self)
        self.radio1 = QtGui.QRadioButton('Database', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('Recipe Lookup', self)
        self.radio1.setChecked(1)
        self.radio2.move(225, 300)
        

    def button_clicked(self):
        sender = self.sender
        #if sender == 'Tutorial':
            # Need to make a tutorial

        #if sender == 'Database':
            
        #elif sender == 'Recipe Lookup':


if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(700,589)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen1(wizard))
    #wizard.addPage(UnderConstruction(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
