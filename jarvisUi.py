# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUI(object):
    def setupUi(self, jarvisUI):
        jarvisUI.setObjectName("jarvisUI")
        jarvisUI.resize(1834, 942)
        self.centralwidget = QtWidgets.QWidget(jarvisUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, 0, 1920, 1080))
        self.label.setStyleSheet("background:transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/jarvis/jarvis gui material/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1660, 850, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1510, 850, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 731, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("E:/jarvis/jarvis gui material/Jarvis_Loading_Screen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1000, 60, 341, 71))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1200, 60, 341, 71))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1190, 600, 641, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("E:/jarvis/jarvis gui material/qC6V1W.webp"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        jarvisUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUI)
        QtCore.QMetaObject.connectSlotsByName(jarvisUI)

    def retranslateUi(self, jarvisUI):
        _translate = QtCore.QCoreApplication.translate
        jarvisUI.setWindowTitle(_translate("jarvisUI", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUI", "Exit"))
        self.pushButton_2.setText(_translate("jarvisUI", "Run"))
        self.textBrowser_2.setHtml(_translate("jarvisUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisUI()
    ui.setupUi(jarvisUI)
    jarvisUI.show()
    sys.exit(app.exec_())
