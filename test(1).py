import json
import sys
 
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
 
import findStudent
import modifyStudent
import manageCourse

import pymysql


#打开数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='Qjj030107', db='demo')

#创建游标对象
cur = conn.cursor()
 
# 主界面UI、布局
class Ui_MainWindow(object):
    #界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 1000)
        MainWindow.setMinimumSize(QSize(1, 669))
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

        self.pushButton_deleteStudent = QPushButton(self.centralwidget)
        self.pushButton_deleteStudent.setObjectName("pushButton_deleteStudent")
        self.horizontalLayout.addWidget(self.pushButton_deleteStudent)

        self.pushButton_findStudent = QPushButton(self.centralwidget)
        self.pushButton_findStudent.setObjectName("pushButton_findStudent")
        self.horizontalLayout.addWidget(self.pushButton_findStudent)

        self.pushButton_modifyStudent = QPushButton(self.centralwidget)
        self.pushButton_modifyStudent.setObjectName("pushButton_modifyStudent")
        self.horizontalLayout.addWidget(self.pushButton_modifyStudent)

        self.pushButton_managecourse = QPushButton(self.centralwidget)
        self.pushButton_managecourse.setObjectName("pushButton_managecourse")
        self.horizontalLayout.addWidget(self.pushButton_managecourse)

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

        self.label_gender = QLabel(self.centralwidget)
        self.label_gender.setObjectName("label_gender")
        self.horizontalLayout_2.addWidget(self.label_gender)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.label_class = QLabel(self.centralwidget)
        self.label_class.setObjectName("label_class")
        self.horizontalLayout_2.addWidget(self.label_class)

        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.pushButton_insertStudent = QPushButton(self.centralwidget)
        self.pushButton_insertStudent.setObjectName("pushButton_insertStudent")
        self.horizontalLayout_2.addWidget(self.pushButton_insertStudent)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1582, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    #名称
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理系统"))
        self.pushButton_findStudent.setText(_translate("MainWindow", "查询学生信息"))
        self.pushButton_deleteStudent.setText('删除学生信息')
        self.pushButton_modifyStudent.setText('修改学生信息')
        self.pushButton_managecourse.setText('管理课程')
        self.pushButton_save.setText('保存数据')
        self.pushButton_modifyStudent.setText('修改学生信息')
        self.label_id.setText(_translate("MainWindow", "学号"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_gender.setText(_translate("MainWindow", "性别"))
        self.label_class.setText(_translate("MainWindow", "班级"))
        self.pushButton_insertStudent.setText(_translate("MainWindow", "添加学生"))
 
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "班级"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("MainWindow", "加权平均分"))
 
 
# 用户操作类（继承主界面UI）
class Index(QMainWindow):
    def __init__(self):
        super(Index, self).__init__()
        self.index_ui = Ui_MainWindow()
        self.index_ui.setupUi(self)
 
        # 设置
        self.index_ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.index_ui.pushButton_insertStudent.clicked.connect(self.insertStudent)  # 新增信息
        self.index_ui.pushButton_findStudent.clicked.connect(self.findStudent)  # 查询信息
        self.index_ui.pushButton_deleteStudent.clicked.connect(self.deleteStudent)  # 删除信息
        self.index_ui.pushButton_modifyStudent.clicked.connect(self.modifyStudent)  # 修改信息
        self.index_ui.pushButton_save.clicked.connect(self.saveData)  # 数据保存
        # self.index_ui.pushButton_managecourse.clicked.connect(self.addCourse)  #管理课程

    #管理课程窗口显示
    def manageCourse(self):
        self.manageCoursewindows = QDialog(self)
        self.manageCourse_ui = manageCourse.Ui_Form()
        self.find_ui.setupUi(self.manageCoursewindows)
        self.find_ui.pushButton.clicked.connect(self.addCourseAction)
        self.find_ui.pushButton1.clicked.connect(self.deleteCourseAction)
        self.findwindows.show()




 
    # 查询学生窗口显示
    def findStudent(self):
        self.findwindows = QDialog(self)
        self.find_ui = findStudent.Ui_Form()
        self.find_ui.setupUi(self.findwindows)
        self.find_ui.pushButton.clicked.connect(self.findAction)
        self.findwindows.show()
 
    # 查询学生操作模块
    def findAction(self):     
        self.find_ui.listWidget.clear()
        lis = []
        for i in range(self.index_ui.tableWidget.rowCount()):
            if self.index_ui.tableWidget.item(i, 0):
                if self.index_ui.tableWidget.item(i, 0).text() == self.find_ui.lineEdit.text():
                    lis.append([self.index_ui.tableWidget.item(i, _).text() for _ in range(7)])
        if lis == []:
            QMessageBox.critical(self, '警告', '查无此人！')
 
        for i in range(len(lis)):
            self.find_ui.listWidget.addItem(
                f'学号:{lis[i][0]}\t姓名:{lis[i][1]}\t数学:{lis[i][2]}\t英语:{lis[i][3]}\t编程:{lis[i][4]}\t总分:{lis[i][5]}\t平均分:{lis[i][6]}')
 
   
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", '', 'json(*.json)')
        save_path = fileName2
        if save_path != '':
            items = []
            for i in range(self.index_ui.tableWidget.rowCount()):
                lis = []
                for g in range(self.index_ui.tableWidget.columnCount()):  # 此处是7行
                    if self.index_ui.tableWidget.item(i, g):
                        lis.append(self.index_ui.tableWidget.item(i, g).text())
                items.append(lis)
            with open(file=save_path, mode='w+', encoding='utf8') as file:
                file.write(json.dumps({"class": items}))
 
    # 保存默认文件信息
    def saveData(self):
        items = []
        for i in range(self.index_ui.tableWidget.rowCount()):
            lis = []
            for g in range(self.index_ui.tableWidget.columnCount()):  # 此处是7行
                if self.index_ui.tableWidget.item(i, g):
                    lis.append(self.index_ui.tableWidget.item(i, g).text())
            items.append(lis)
        with open(file='stuMsg.json', mode='w+', encoding='utf8') as file:
            file.write(json.dumps({"class": items}))
            QMessageBox.information(self, '通知', '数据保存成功')
 
    # 打开默认文件信息
    def openDefaultData(self):
        with open(file='stuMsg.json', mode='r', encoding='utf8') as file:
            items = json.load(file)['class']
            self.index_ui.tableWidget.clear()
            self.freshTable(items)
 
    # 增加学生信息模块
    def insertStudent(self):
        
        # try:
        #     math = float(self.index_ui.lineEdit_3.text())
        #     english = float(self.index_ui.lineEdit_4.text())
        #     python = float(self.index_ui.lineEdit_5.text())
        # except ValueError:
        #     QMessageBox.critical(self, '警告', '成绩请输入数字')
        #     return

        try:
            id = self.index_ui.lineEdit.text()
            name = self.index_ui.lineEdit_2.text()
            gender = self.index_ui.lineEdit_3.text()
            class1 = self.index_ui.lineEdit_4.text()
            # if math == '' or english == '' or python == '' or id == '' or name == '':
            #     QMessageBox.critical(self, '警告', '输入项不能为空')
            #     return

            # if math > 100 or math < 0 or english > 100 or english < 0 or python > 100 or python < 0:
            #     QMessageBox.critical(self, '警告', '成绩输入有误')
            #     return

            # sum = round(math + english + python, 2)
            # average = round(sum / 3, 2)

            student_data = (id, name, gender,class1)
            sql_insert = "INSERT INTO student (id, name, gender,class1) VALUES (%s, %s, %s, %s)"

            try:
                cur.execute(sql_insert, student_data)
                conn.commit()
                items = [student_data]
                self.freshTable(items)

                self.index_ui.lineEdit.clear()
                self.index_ui.lineEdit_2.clear()
                self.index_ui.lineEdit_3.clear()
                self.index_ui.lineEdit_4.clear()
                
                
                QMessageBox.information(self, '成功', '学生信息添加成功')
            except pymysql.Error as e:
                conn.rollback()  # Rollback the changes in case of an error
                QMessageBox.critical(self, '数据库错误', f"数据库操作失败: {e}")
        except Exception as ex:
                QMessageBox.information(self, '', f"失败")

    # 删除学生信息模块
    def deleteStudent(self):
        selected_row = self.index_ui.tableWidget.currentRow()
        if selected_row >= 0:
            student_id = self.index_ui.tableWidget.item(selected_row, 0).text()
            try:
                # 删除数据库中对应的学生记录
                sql_delete = "DELETE FROM student WHERE id=%s"
                cur.execute(sql_delete, (student_id,))
                conn.commit()

                # 从表格中删除选中的行
                self.index_ui.tableWidget.removeRow(selected_row)
                self.create_piechart()

            except pymysql.Error as e:
                conn.rollback()  # Rollback the changes in case of an error
                QMessageBox.critical(self, '数据库错误', f"数据库操作失败: {e}")
            except Exception as ex:
                QMessageBox.information(self, '', f"成功")

    # 修改学生信息窗口显示
    def modifyStudent(self):
        self.findwindows = QDialog(self)
        self.find_ui = modifyStudent.Ui_Form()
        self.find_ui.setupUi(self.findwindows)
        self.find_ui.pushButton.clicked.connect(self.findAction)
        self.findwindows.show()
 
    # 修改学生信息模块
    def sureModify(self):
        self.find_ui.listWidget.clear()
        lis = []
        for i in range(self.index_ui.tableWidget.rowCount()):
            if self.index_ui.tableWidget.item(i, 1):
                if self.index_ui.tableWidget.item(i, 1).text() == self.find_ui.lineEdit.text():
                    lis.append([self.index_ui.tableWidget.item(i, _).text() for _ in range(7)])
        if lis == []:
            QMessageBox.critical(self, '警告', '查无此人！')
        try:
            math = float(self.modify_ui.lineEdit_3.text())
            english = float(self.modify_ui.lineEdit_4.text())
            python = float(self.modify_ui.lineEdit_5.text())
        except:
            QMessageBox.critical(self, '警告', '成绩请输入数字')
        try:
            id = self.modify_ui.lineEdit.text()
            name = self.modify_ui.lineEdit_2.text()
 
            if math == '' or english == '' or python == '' or id == '' or name == '':
                QMessageBox.critical(self, '警告', '输入项不能为空')
                exit()
            if math > 100 or math < 0 or english > 100 or english < 0 or python > 100 or python < 0:
                QMessageBox.critical(self, '警告', '成绩请大于0小于100')
                exit()
            sum = round(math + english + python, 2)
            average = round(sum / 3, 2)
            items = [[id,
                      name,
                      math,
                      english,
                      python,
                      sum,
                      average
                      ]]
            for i in range(7):
                newItem = QTableWidgetItem(str(items[0][i]))
                self.index_ui.tableWidget.setItem(self.index_ui.tableWidget.currentRow(), i, newItem)
            self.create_piechart()
            update_query = "UPDATE student SET id = %s,math = %s, english = %s python = %s,sum=%s,average=%s WHERE name = %s"
            cur.execute(update_query, (id,math,english,python,sum,average))
        except:
            pass
 
    # 主界面table刷新
    def freshTable(self, items):
        for i in range(len(items)):
            item = items[i]
            row = self.index_ui.tableWidget.rowCount()
            self.index_ui.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.index_ui.tableWidget.setItem(row, j, item)
        self.create_piechart()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Index()
    main.show()
    sys.exit(app.exec_())
 