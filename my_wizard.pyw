import sys, os
from PyQt4 import QtGui

class UnderConstruction(QtGui.QWizardPage):
    #This is a temporary page
    #Once the rest of the GUI is added in to this part, this page will go away
    def __init__(self, parent):
        super(UnderConstruction, self).__init__(parent)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/under_construction.jpg"))

class Screen1(QtGui.QWizardPage):
    #Screen that appears when the program is run
    def __init__(self, parent=None):
        super(Screen1, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.radio1 = QtGui.QRadioButton('&Database', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Recipe Lookup', self)
        self.radio2.move(225, 300)

        self.NextButton.clicked.connect(self.roar)
    def roar(self):
        if radio1.isChecked():
            wizard.addPage(UnderConstruction(self))

        


if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    #add each screen into the GUI
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen1(wizard))
    wizard.addPage(UnderConstruction(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
