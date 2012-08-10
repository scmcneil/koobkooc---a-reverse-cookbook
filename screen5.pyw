import sys, os
from PyQt4 import QtGui

class Screen5(QtGui.QWizardPage):
    def __init__(self, paretn=None):
        super(Screen5, self).__init__()
        self.initUI()

    def initUI(self):
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
        

if ( __name__ == '__main__' ):
    # create the application if necessary
    app = None
    if ( not QtGui.QApplication.instance() ):
        app = QtGui.QApplication([])
    
    wizard = QtGui.QWizard()
    wizard.resize(720,650)
    wizard.setWindowTitle('koobkooc---a-reverse-cookbook')
    wizard.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
    wizard.addPage(Screen5(wizard))
    wizard.exec_()
    
    # execute the application if we've created it
    if ( app ):
        app.exec_()
