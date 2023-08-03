import os,sys
import data
from PyQt5.QtWidgets import QMainWindow,QApplication

os.chdir(os.path.split(os.path.realpath(__file__))[0])

def LaunchMainWidget():
    application = QApplication(sys.argv)
    MainWindow = QMainWindow()
    from main import MyMainWindow
    data.ui = MyMainWindow()
    data.ui.show()
    sys.exit(application.exec_())

if __name__=='__main__':
    LaunchMainWidget()