import json
import sys
 
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
 
import findStudent
import modifyStudent

import pymysql

#打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Qjj030107', db='demo')

#创建游标对象
cur = conn.cursor()
 
# 主界面UI、布局
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 669)
        MainWindow.setMinimumSize(QSize(1450, 669))
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_savaFile = QPushButton(self.centralwidget)
        self.pushButton_savaFile.setObjectName("pushButton_savaFile")
        self.horizontalLayout.addWidget(self.pushButton_savaFile)
        self.pushButton_deleteStudent = QPushButton(self.centralwidget)
        self.pushButton_deleteStudent.setObjectName("pushButton_deleteStudent")
        self.horizontalLayout.addWidget(self.pushButton_deleteStudent)
        self.pushButton_findStudent = QPushButton(self.centralwidget)
        self.pushButton_findStudent.setObjectName("pushButton_findStudent")
        self.horizontalLayout.addWidget(self.pushButton_findStudent)
        self.pushButton_modifyStudent = QPushButton(self.centralwidget)
        self.pushButton_modifyStudent.setObjectName("pushButton_modifyStudent")
        self.horizontalLayout.addWidget(self.pushButton_modifyStudent)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_id = QLabel(self.centralwidget)
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_2.addWidget(self.label_id)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_2.addWidget(self.label_name)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_math = QLabel(self.centralwidget)
        self.label_math.setObjectName("label_math")
        self.horizontalLayout_2.addWidget(self.label_math)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_english = QLabel(self.centralwidget)
        self.label_english.setObjectName("label_english")
        self.horizontalLayout_2.addWidget(self.label_english)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.label_python = QLabel(self.centralwidget)
        self.label_python.setObjectName("label_python")
        self.horizontalLayout_2.addWidget(self.label_python)
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.pushButton_insertStudent = QPushButton(self.centralwidget)
        self.pushButton_insertStudent.setObjectName("pushButton_insertStudent")
        self.horizontalLayout_2.addWidget(self.pushButton_insertStudent)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(5, item)
        # item = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1082, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

 
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理系统"))
        self.pushButton.setText(_translate("MainWindow", "导入班级信息"))
        self.pushButton_findStudent.setText(_translate("MainWindow", "查询学生信息"))
        self.pushButton_savaFile.setText(_translate("MainWindow", "导出班级信息"))
        self.pushButton_deleteStudent.setText('删除学生信息')
        self.pushButton_modifyStudent.setText('修改学生信息')
        self.pushButton_save.setText('保存数据')
        self.label_id.setText(_translate("MainWindow", "学号"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_math.setText(_translate("MainWindow", "班级"))
        self.label_english.setText(_translate("MainWindow", "科目"))
        self.label_python.setText(_translate("MainWindow", "成绩"))
        self.pushButton_insertStudent.setText(_translate("MainWindow", "添加"))
 
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "班级"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "科目"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "成绩"))
        item = self.tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("MainWindow", "总分"))
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("MainWindow", "平均分"))

# 用户操作类（继承主界面UI）
class Index(QMainWindow):
    def __init__(self):
        super(Index, self).__init__()
        self.index_ui = Ui_MainWindow()
        self.index_ui.setupUi(self)
 
        # 设置
        self.index_ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.index_ui.pushButton_insertStudent.clicked.connect(self.insertStudent)  # 新增信息
        # self.index_ui.pushButton.clicked.connect(self.inputFile)  # 导入班级信息
        # self.index_ui.pushButton_savaFile.clicked.connect(self.saveFile)  # 导出班级信息
        # self.index_ui.pushButton_findStudent.clicked.connect(self.findStudent)  # 查询信息
        # self.index_ui.pushButton_deleteStudent.clicked.connect(self.deleteStudent)  # 删除信息
        # self.index_ui.pushButton_modifyStudent.clicked.connect(self.modifyStudent)  # 修改信息
        # self.index_ui.pushButton_save.clicked.connect(self.saveData)  # 数据保存
 
        # 初始化
        try:
            self.openDefaultData()
        except:
            pass
 
     # 增加学生信息模块
    def insertStudent(self):
        try:
            grade = float(self.index_ui.lineEdit_5.text())
        except:
            QMessageBox.critical(self, '警告', '成绩请输入数字')
        try:
            id = self.index_ui.lineEdit.text()
            name = self.index_ui.lineEdit_2.text()
            class1 = self.index_ui.lineEdit_3.text()
            subject = self.index_ui.lineEdit_4()

 
            if class1 == '' or subject == '' or grade == '' or id == '' or name == '':
                QMessageBox.critical(self, '警告', '输入项不能为空')
                exit()
            if grade > 100 or grade < 0:
                QMessageBox.critical(self, '警告', '成绩输入有误')
                exit()
            sum = round( grade, 2)
            average = round(sum / 3, 2)
            items = [[id,
                      name,
                      class1,
                      subject,
                      grade,
                      sum,
                      average
                      ]]
            try:
                cur.execute("INSERT INTO student (id, name, class1, subject, grade, sum, average) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, name, class1, subject, grade, sum, average))
                conn.commit()
                self.freshTable(items)
                self.index_ui.lineEdit.clear()
                self.index_ui.lineEdit_2.clear()
                self.index_ui.lineEdit_3.clear()
                self.index_ui.lineEdit_4.clear()
                self.index_ui.lineEdit_5.clear()
            except pymysql.Error as e:
                QMessageBox.critical(self, '数据库错误', f"数据库操作失败: {e}")
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Index()
    main.show()
    sys.exit(app.exec_())