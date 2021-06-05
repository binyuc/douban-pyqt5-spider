import sys
from PyQt5.QtWidgets import QApplication
from spider import MainWindow
from PyQt5.QtGui import QIcon
import os

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r'D:\Jupyter\爬虫\豆瓣自动发帖\douban_env\Lib\site-packages\PyQt5\Qt\plugins'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('g10.ico'))
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
# pyinstaller -F main.py --noconsole --icon="g10.ico"
# pyuic5 -o ui_mainwindow.py douban_ui.ui
# D:\Jupyter\爬虫\豆瓣自动发帖\version2\dist\群发测试文案库.xlsx
