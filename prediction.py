# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prediction.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from tcs import printfunction
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 40, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sentence = QtWidgets.QTextEdit(self.centralwidget)
        self.sentence.setGeometry(QtCore.QRect(40, 370, 691, 61))
        self.sentence.setObjectName("sentence")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 450, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.prediction1 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction1.setGeometry(QtCore.QRect(50, 100, 113, 20))
        self.prediction1.setObjectName("prediction1")
        self.prediction2 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction2.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.prediction2.setObjectName("prediction2")
        self.prediction3 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction3.setGeometry(QtCore.QRect(310, 100, 113, 20))
        self.prediction3.setObjectName("prediction3")
        self.prediction4 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction4.setGeometry(QtCore.QRect(440, 100, 113, 20))
        self.prediction4.setObjectName("prediction4")
        self.prediction5 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction5.setGeometry(QtCore.QRect(570, 100, 113, 20))
        self.prediction5.setObjectName("prediction5")
        self.prediction6 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction6.setGeometry(QtCore.QRect(50, 150, 113, 20))
        self.prediction6.setObjectName("prediction6")
        self.prediction7 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction7.setGeometry(QtCore.QRect(180, 150, 113, 20))
        self.prediction7.setObjectName("prediction7")
        self.prediction8 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction8.setGeometry(QtCore.QRect(310, 150, 113, 20))
        self.prediction8.setObjectName("prediction8")
        self.prediction9 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction9.setGeometry(QtCore.QRect(440, 150, 113, 20))
        self.prediction9.setObjectName("prediction9")
        self.prediction10 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction10.setGeometry(QtCore.QRect(570, 150, 113, 20))
        self.prediction10.setObjectName("prediction10")
        self.prediction11 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction11.setGeometry(QtCore.QRect(50, 200, 113, 20))
        self.prediction11.setObjectName("prediction11")
        self.prediction12 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction12.setGeometry(QtCore.QRect(180, 200, 113, 20))
        self.prediction12.setObjectName("prediction12")
        self.prediction13 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction13.setGeometry(QtCore.QRect(310, 200, 113, 20))
        self.prediction13.setObjectName("prediction13")
        self.prediction14 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction14.setGeometry(QtCore.QRect(440, 200, 113, 20))
        self.prediction14.setObjectName("prediction14")
        self.prediction15 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction15.setGeometry(QtCore.QRect(570, 200, 113, 20))
        self.prediction15.setObjectName("prediction15")
        self.prediction16 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction16.setGeometry(QtCore.QRect(50, 250, 113, 20))
        self.prediction16.setObjectName("prediction16")
        self.prediction17 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction17.setGeometry(QtCore.QRect(180, 250, 113, 20))
        self.prediction17.setObjectName("prediction17")
        self.prediction18 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction18.setGeometry(QtCore.QRect(310, 250, 113, 20))
        self.prediction18.setObjectName("prediction18")
        self.prediction19 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction19.setGeometry(QtCore.QRect(440, 250, 113, 20))
        self.prediction19.setObjectName("prediction19")
        self.prediction20 = QtWidgets.QLineEdit(self.centralwidget)
        self.prediction20.setGeometry(QtCore.QRect(570, 250, 113, 20))
        self.prediction20.setObjectName("prediction20")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 340, 261, 16))

        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        path,path2,path3,path4,path5,path6,path7,path8,path9,path10,path11,path12,path13,path14,path15,path16,path17,path18,path19,path20=printfunction()
        self.prediction1.setText(str(path[len(path)-1]))
        self.prediction2.setText(str(path[len(path2)-1]))
        self.prediction3.setText(str(path[len(path3)-1]))
        self.prediction4.setText(str(path[len(path4)-1]))
        self.prediction5.setText(str(path[len(path5)-1]))
        self.prediction6.setText(str(path[len(path6)-1]))
        self.prediction7.setText(str(path[len(path7)-1]))
        self.prediction8.setText(str(path[len(path8)-1]))
        self.prediction9.setText(str(path[len(path9)-1]))
        self.prediction10.setText(str(path[len(path10)-1]))
        self.prediction11.setText(str(path[len(path11)-1]))
        self.prediction12.setText(str(path[len(path12)-1]))
        self.prediction13.setText(str(path[len(path13)-1]))
        self.prediction14.setText(str(path[len(path14)-1]))
        self.prediction15.setText(str(path[len(path15)-1]))
        self.prediction16.setText(str(path[len(path16)-1]))
        self.prediction17.setText(str(path[len(path17)-1]))
        self.prediction18.setText(str(path[len(path18)-1]))
        self.prediction19.setText(str(path[len(path19)-1]))
        self.prediction20.setText(str(path[len(path20)-1]))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CROWD PREDICTION"))
        self.sentence.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "VISUALIZE"))
        self.label_2.setText(_translate("MainWindow", "WHAT COMMUTERS SHOULD BE AWARE OF"))
        self.label_3.setText(_translate("MainWindow", "Regions 1-20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
