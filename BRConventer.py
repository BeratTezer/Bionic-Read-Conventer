from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint, QRect, QEasingCurve
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect, QMessageBox
from BRConventer_UI import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import time
import sys
import os

class BRConventerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(BRConventerApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.convertButton.clicked.connect(self.start)
        self.ui.pasteButton.clicked.connect(self.paste)
        self.ui.copyButton.clicked.connect(self.copy)

    def start(self):
        outputText = ""
        
        caution = QMessageBox()
        caution.setWindowIcon(QtGui.QIcon('R_L.png'))
        caution.setIcon(QMessageBox.Warning)
        caution.setText("You need to paste your text before converting!")
        caution.setWindowTitle("Bionic-Read Conventer")
        caution.setStandardButtons(QMessageBox.Ok)
        
        while True:
            if self.ui.inputTextBox.toPlainText() != "":
                inputText = self.ui.inputTextBox.toPlainText()
                convertType = self.ui.typeSelector.currentText()
                
                if convertType == "For HTML":
                    mark = "<b>"
                    markC = "</b>"
                    for word in inputText.split(" "):
                        if len(word) == 1:
                            outputText += mark + word + markC
                        elif len(word) == 2:
                            outputText += mark + list(word)[0] + markC + list(word)[1]
                        elif len(word) == 3:
                            outputText += mark + list(word)[0] + list(word)[1] + markC + list(word)[2]
                        else:
                            outputText += mark
                            for counter in range(0,int((len(word)*6)/10)+1):
                                outputText += word[counter]
                            outputText += markC
                            for counter in range(int((len(word)*6)/10)+1, len(word)):
                                outputText += word[counter]
                        outputText += " "
                elif convertType == "For Python":
                    inputText = self.ui.inputTextBox.toPlainText()
                convertType = self.ui.typeSelector.currentText()
                
                if convertType == "For Python":
                    mark = "\\033[1m"
                    markC = "\\033[0m"
                    for word in inputText.split(" "):
                        if len(word) == 1:
                            outputText += mark + word + markC
                        elif len(word) == 2:
                            outputText += mark + list(word)[0] + markC + list(word)[1]
                        elif len(word) == 3:
                            outputText += mark + list(word)[0] + list(word)[1] + markC + list(word)[2]
                        else:
                            outputText += mark
                            for counter in range(0,int((len(word)*6)/10)+1):
                                outputText += word[counter]
                            outputText += markC
                            for counter in range(int((len(word)*6)/10)+1, len(word)):
                                outputText += word[counter]
                        outputText += " "
                elif convertType == "For Direct":
                    pass
                else:
                    pass
                break
            else:
                caution.exec()
                break
            
        if self.ui.inputTextBox.toPlainText() != "":
            self.ui.outputTextBox.setPlainText(outputText)
            
        self.ui.notificationLabel_3.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Converted!</span></p></body></html>"))
        self.notification(self.ui.notificationLabel_3)
        
    def paste(self):
        time.sleep(0.05)
        self.ui.inputTextBox.paste()
        
        self.ui.notificationLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Pasted!</span></p></body></html>"))
        self.notification(self.ui.notificationLabel)
        
    def copy(self):
        time.sleep(0.05)
        self.ui.outputTextBox.selectAll()
        self.ui.outputTextBox.copy()
        
        self.ui.notificationLabel_2.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Copied!</span></p></body></html>"))
        self.notification(self.ui.notificationLabel_2)
    
    def notification(self, item):
        self.item = item
        item.setStyleSheet(
            "    background-color: rgb(255, 255, 255, 1);"
            "    border-style: solid;\n"
            "    border-width: 2px;\n"
            "    border-color: white;\n"
            "    border-radius: 20px;\n"
            "    opacity: 1\n"
        )
        self.anim = QPropertyAnimation(item, b"pos")
        self.anim.setEndValue(QPoint(300, 520))
        self.anim.setDuration(350)
        self.anim.finished.connect(self.resetNotification)
        self.anim.start()
        
    def resetNotification(self):
        self.anim = QPropertyAnimation(self.item, b"pos")
        self.anim.setEndValue(QPoint(300, 590))
        self.anim.setDuration(350)
        time.sleep(0.5)
        self.anim.start()
                            
def BRConventerWindow():
    BRConventerWindow = QtWidgets.QApplication(sys.argv)
    win = BRConventerApp()
    win.show()
    sys.exit(BRConventerWindow.exec_())
    
BRConventerWindow()