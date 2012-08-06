import sys
from PyQt4 import QtGui

class Open_file(QtGui.QWidget):
    
    def __init__(self):
        super(Open_file, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        openFile = QtGui.QPushButton('Open a File', self)
        openFile.clicked.connect(self.showDialog)
        openFile.resize(openFile.sizeHint())
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(openFile, 1, 0)
        grid.addWidget(self.textEdit, 2, 0, 5, 0)
        self.setLayout(grid)       
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fname, 'r')
        with f:        
            data = f.read()
            self.textEdit.setText(data)
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Open_file()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
