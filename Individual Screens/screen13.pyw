import sys, os
from PyQt4 import QtGui

class Screen13(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen13, self).__init__()
        self.initUI()

    def initUI(self):
        pic = QtGui.QLabel(self)
        pic.setGeometry(0,0,700,225)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        label = QtGui.QLabel('Find a recipe')
        meat = QtGui.QLabel('Meat')
        veggie1 = QtGui.QLabel('Veggie 1')
        veggie2 = QtGui.QLabel('Veggie 2')
        veggie3 = QtGui.QLabel('Veggie 3')
        veggie4 = QtGui.QLabel('Veggie 4')
        starch = QtGui.QLabel('Served on')

        meatEdit = QtGui.QComboBox(self)
        meatEdit.addItem('---select---')
        veggie1Edit = QtGui.QComboBox(self)
        veggie1Edit.addItem('---select---')
        veggie2Edit = QtGui.QComboBox(self)
        veggie2Edit.addItem('---select---')
        veggie3Edit = QtGui.QComboBox(self)
        veggie3Edit.addItem('---select---')
        veggie4Edit = QtGui.QComboBox(self)
        veggie4Edit.addItem('---select---')
        starchRadio1 = QtGui.QRadioButton('&Rice', self)
        starchRadio2 = QtGui.QRadioButton('&Noodles', self)
        starchRadio3 = QtGui.QRadioButton('&Potatoes', self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        #grid.addWidget(pic)
        grid.addWidget(label, 1, 0)
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

if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen13(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
