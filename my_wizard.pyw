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

        #self.layout = QtGui.QVBoxLayout(self)
        #self.buttonGroup = QtGui.QVButtonGroup('Temp', self)
        self.radio1 = QtGui.QRadioButton('&Database', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Recipe Lookup', self)
        #self.radio1.setChecked(1)
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
    wizard.addPage(Screen1(wizard))
    wizard.addPage(UnderConstruction(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
