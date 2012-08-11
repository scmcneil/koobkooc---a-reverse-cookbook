import sys, os
from PyQt4 import QtGui

class Screen3(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen3, self).__init__()
        self.initUI()

    def initUI(self):
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
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
