# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'douban_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 1438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_head = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_head.setObjectName("comboBox_head")
        self.comboBox_head.addItem("")
        self.comboBox_head.addItem("")
        self.gridLayout.addWidget(self.comboBox_head, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 16, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_excel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_excel.setObjectName("lineEdit_excel")
        self.gridLayout.addWidget(self.lineEdit_excel, 2, 1, 1, 1)
        self.comboBox_random_target = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_random_target.setObjectName("comboBox_random_target")
        self.comboBox_random_target.addItem("")
        self.comboBox_random_target.addItem("")
        self.gridLayout.addWidget(self.comboBox_random_target, 5, 1, 1, 1)
        self.comboBox_star = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_star.setObjectName("comboBox_star")
        self.comboBox_star.addItem("")
        self.comboBox_star.addItem("")
        self.comboBox_star.addItem("")
        self.comboBox_star.addItem("")
        self.comboBox_star.addItem("")
        self.comboBox_star.addItem("")
        self.gridLayout.addWidget(self.comboBox_star, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.textBrowser_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_display.setObjectName("textBrowser_display")
        self.gridLayout.addWidget(self.textBrowser_display, 15, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.lineEdit_movieurl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_movieurl.setObjectName("lineEdit_movieurl")
        self.gridLayout.addWidget(self.lineEdit_movieurl, 10, 1, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 9, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 2)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.gridLayout.addWidget(self.lineEdit_username, 8, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 14, 1, 1, 1)
        self.textEdit_comment = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_comment.setObjectName("textEdit_comment")
        self.gridLayout.addWidget(self.textEdit_comment, 11, 1, 1, 1)
        self.textBrowser_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_info.setObjectName("textBrowser_info")
        self.gridLayout.addWidget(self.textBrowser_info, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 2)
        self.lineEdit_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.gridLayout.addWidget(self.lineEdit_time, 12, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 15, 0, 1, 1)
        self.pushButton_loadexcel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_loadexcel.setObjectName("pushButton_loadexcel")
        self.gridLayout.addWidget(self.pushButton_loadexcel, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 0, 1, 1)
        self.lineEdit_blacklist = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_blacklist.setObjectName("lineEdit_blacklist")
        self.gridLayout.addWidget(self.lineEdit_blacklist, 13, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 45))
        self.menubar.setObjectName("menubar")
        self.menu_v1 = QtWidgets.QMenu(self.menubar)
        self.menu_v1.setObjectName("menu_v1")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_v1.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_head.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox_head.setItemText(1, _translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.label_7.setText(_translate("MainWindow", "?????????????????????"))
        self.label_11.setText(_translate("MainWindow", "EXCEL????????????"))
        self.comboBox_random_target.setItemText(0, _translate("MainWindow", "????????????"))
        self.comboBox_random_target.setItemText(1, _translate("MainWindow", "???????????????"))
        self.comboBox_star.setItemText(0, _translate("MainWindow", "0"))
        self.comboBox_star.setItemText(1, _translate("MainWindow", "5"))
        self.comboBox_star.setItemText(2, _translate("MainWindow", "4"))
        self.comboBox_star.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_star.setItemText(4, _translate("MainWindow", "2"))
        self.comboBox_star.setItemText(5, _translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "?????????"))
        self.label_6.setText(_translate("MainWindow", "????????????"))
        self.label_4.setText(_translate("MainWindow", "????????????"))
        self.label_12.setText(_translate("MainWindow", "??????????????????"))
        self.label_10.setText(_translate("MainWindow", "                         ????????????"))
        self.label_8.setText(_translate("MainWindow", "????????????"))
        self.label_13.setText(_translate("MainWindow", "???????????????????????????"))
        self.textBrowser_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.EXCEL??????????????????<span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">D:\\Jupyter\\</span><span style=\" font-family:\'??????,monospace\'; color:#000000;\">??????</span><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">\\</span><span style=\" font-family:\'??????,monospace\'; color:#000000;\">??????????????????</span><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">\\version1\\dist\\</span><span style=\" font-family:\'??????,monospace\'; color:#000000;\">??????</span><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">.xlsx</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'JetBrains Mono,monospace\'; color:#000000;\">????????????????????????????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.???????????????????????????????????????????????????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.?????????????????????????????????????????????????????????excel?????????????????????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.???????????????????????????url??????????????????????????????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.????????????<span style=\" font-weight:600;\">0</span>??????????????????<span style=\" font-weight:600;\">??????????????????</span>?????????1-5??????1-5????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">????????????</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.????????????????????????????????????????????????????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.???????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.????????????url:???????????????????????????url?????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            https://movie.douban.com/subject/30483667/</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.???????????????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.????????????????????????60-300??????-????????????60??????300??????????????????</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.???????????????35324548???35324549???35324542 ???????????????</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "????????????url"))
        self.label_9.setText(_translate("MainWindow", "                         ????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.pushButton_loadexcel.setText(_translate("MainWindow", "????????????excel"))
        self.label.setText(_translate("MainWindow", "?????????"))
        self.menu_v1.setTitle(_translate("MainWindow", "??????????????????v1"))
        self.menu.setTitle(_translate("MainWindow", "??????"))
