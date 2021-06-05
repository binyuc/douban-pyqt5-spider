from ui_mainwindow import *
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from my_thread import WorkThread


# 继承UI文件的类
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 在这里是setupUI
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_spider)
        self.pushButton_loadexcel.clicked.connect(self.read_file)

    def read_file(self):
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", "/home")[0]
        self.lineEdit_excel.setText(directory1)

    def run_spider(self):
        self.textBrowser_display.append('------------开始------------')
        # 通常提取界面的数据可以输用text()
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        url = self.lineEdit_movieurl.text()
        comment = self.textEdit_comment.toPlainText()
        header = self.comboBox_head.currentText()
        random_target = self.comboBox_random_target.currentText()
        star = self.comboBox_star.currentText()
        time = self.lineEdit_time.text()
        excel = self.lineEdit_excel.text()
        blacklist = self.lineEdit_blacklist.text()
        # 这里是关键，需要将参数传给多线程的程序
        self.th = WorkThread(username, password, url, comment, header, random_target, star, time, excel, blacklist)

        self.pushButton.setChecked(True)
        self.pushButton.setDisabled(True)

        # 将线程th的信号finishSignal和UI主线程中的槽函数button_finish进行连接
        self.th.finishSignal.connect(self.end_spider)
        self.th.displaySignal.connect(self.display)
        # 启动线程
        self.th.start()

    def display(self, target_str):
        self.textBrowser_display.append(target_str)

    def end_spider(self):
        self.textBrowser_display.append('------------结束------------')
        # 设置按钮可用
        self.pushButton.setChecked(False)
        self.pushButton.setDisabled(False)
