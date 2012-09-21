# Copyright Sheena C. McNeil

import sys, os
import database
from PyQt4 import QtGui

class Browser(QtGui.QWidget):
    
    def __init__(self):
        super(Browser, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(700,900)
        self.setWindowTitle('koobkooc---a-reverse-cookbook')
        self.setWindowIcon(QtGui.QIcon('koobkooc.jpg'))
        self.col = QtGui.QColor(255,255,255)
        pic = QtGui.QLabel(self)
        pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/koobkooc-01.jpg"))
        self.textBrowser = QtGui.QTextBrowser()
        self.recipes = QtGui.QListWidget()
        all_recipes = database.Browse_db()
        if len(all_recipes) > 0:
            for x in all_recipes:
                print(x)
                item = QtGui.QListWidgetItem(x)
                self.recipes.addItem(item)
        self.recipes.clicked.connect(self.listclicked)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(pic)
        layout.addWidget(self.recipes)
        layout.addWidget(self.textBrowser)
        self.setLayout(layout)
        self.show()
        
    def listclicked(self, item):
        recipe = self.recipes.currentItem().text()
        recipe_text = database.Recipe_text(recipe)
        self.textBrowser.setText(recipe_text)
        print (item)
        print (self.recipes.currentItem().text())
        print ('roar')
            
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Browser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
