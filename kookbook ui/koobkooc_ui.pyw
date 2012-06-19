import sys, os
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
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
        btnTutorial.resize(btnTutorial.sizeHint())
        btnTutorial.move(170, 555)
        btnDatabase = QtGui.QPushButton('Database', self)
        btnDatabase.resize(btnDatabase.sizeHint())
        btnDatabase.move(320, 555)
        btnRecipeLookup = QtGui.QPushButton('Recipe Lookup', self)
        btnRecipeLookup.resize(btnRecipeLookup.sizeHint())        
        btnRecipeLookup.move(470, 555)
        self.show()

    def closeEvent(self, event):       
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
