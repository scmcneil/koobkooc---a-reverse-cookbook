import sys, os
from PyQt4 import QtGui

class Screen2(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen2, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.label = QtGui.QLabel("<font sive = 24><b> What database function would you like to perform? </b></font>", self)
        self.label.move(225, 250)
        self.radio1 = QtGui.QRadioButton('&Add a Recipe', self)
        self.radio1.move(225, 275)
        self.radio2 = QtGui.QRadioButton('&Edit a Recipe', self)
        self.radio2.move(225, 300)
        self.radio3 = QtGui.QRadioButton('&Delete a Recipe', self)
        self.radio3.move(225, 325)


if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen2(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
