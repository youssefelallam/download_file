import os
import sys
import urllib.request
from os import path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
from downUI import Ui_MainWindow


class MainApp(QMainWindow , Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_UI()
        self.handel_Button()


    def handel_UI(self):
        self.setWindowTitle("Downloader")
        self.setFixedSize(487,227)

    def handel_Button(self):
        self.pushButton.clicked.connect(self.Downlowd)
        self.pushButton_2.clicked.connect(self.handel_Browse)

    def handel_Progress(self, blocknum, blocksize, totalsize):
        read = blocknum * blocksize
        if totalsize > 0 :
            percent = read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()

    def handel_Browse(self):
        save_place = QFileDialog.getSaveFileName(self,caption="Save As",directory=".",filter="All files (*.*)")
        save = (str(save_place)[2:].split(',')[0]).replace("'","")
        self.lineEdit_2.setText(save)
        

    def Downlowd(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url, save_location , self.handel_Progress)
            QMessageBox.information(self, "Download completed", "The Download Finished")
            
        except Exception:
            QMessageBox.warning(self, "Download error", "The Download faild")
        
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
