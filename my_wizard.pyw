import sys, os
from PyQt4 import QtGui

class Screen1(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen1, self).__init__()
        self.initUI()

    def initUI(self):
        #self.setGeometry(300,300,700,589)
        self.resize(700,589)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
        self.col = QtGui.QColor(255,255,255)
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,589)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-02-01.jpg"))
        btnTutorial = QtGui.QPushButton('Tutorial', self)
        btnTutorial.clicked.connect(self.button_clicked)
        btnTutorial.resize(btnTutorial.sizeHint())
        btnTutorial.move(170, 555)
        
        btnDatabase = QtGui.QPushButton('Database', self)
        btnDatabase.clicked.connect(self.button_clicked)
        btnDatabase.resize(btnDatabase.sizeHint())
        btnDatabase.move(320, 555)
        
        btnRecipeLookup = QtGui.QPushButton('Recipe Lookup', self)
        btnRecipeLookup.clicked.connect(self.button_clicked)
        btnRecipeLookup.resize(btnRecipeLookup.sizeHint())        
        btnRecipeLookup.move(470, 555)

    def button_clicked(self):
        sender = self.sender
        #if sender == 'Tutorial':
            # Need to make a tutorial

        if sender == 'Database':
            under_construction()

        #elif sender == 'Recipe Lookup':


if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    window = Screen1()
    window.show()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
