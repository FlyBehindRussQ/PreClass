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
        MainWindow.resize(1582, 869)
        MainWindow.setMinimumSize(QSize(1582, 869))
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(21, 21, 1550, 801))
        self.widget.setObjectName("widget")
        self.horizontalLayout6 = QHBoxLayout(self.widget)
        self.horizontalLayout6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_save = QPushButton(self.widget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_deleteStudent = QPushButton(self.widget)
        self.pushButton_deleteStudent.setObjectName("pushButton_deleteStudent")
        self.horizontalLayout.addWidget(self.pushButton_deleteStudent)

        self.pushButton_findStudent = QPushButton(self.widget)
        self.pushButton_findStudent.setObjectName("pushButton_findStudent")
        self.horizontalLayout.addWidget(self.pushButton_findStudent)

        self.pushButton_modifyStudent = QPushButton(self.widget)
        self.pushButton_modifyStudent.setObjectName("pushButton_modifyStudent")
        self.horizontalLayout.addWidget(self.pushButton_modifyStudent)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_id = QLabel(self.widget)
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_2.addWidget(self.label_id)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_2.addWidget(self.label_name)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.label_math = QLabel(self.widget)
        self.label_math.setObjectName("label_math")
        self.horizontalLayout_2.addWidget(self.label_math)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)

        self.label_english = QLabel(self.widget)
        self.label_english.setObjectName("label_english")
        self.horizontalLayout_2.addWidget(self.label_english)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.label_python = QLabel(self.widget)
        self.label_python.setObjectName("label_python")
        self.horizontalLayout_2.addWidget(self.label_python)

        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)

        self.pushButton_insertStudent = QPushButton(self.widget)
        self.pushButton_insertStudent.setObjectName("pushButton_insertStudent")
        self.horizontalLayout_2.addWidget(self.pushButton_insertStudent)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)

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
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout6.addLayout(self.verticalLayout)
        self.horizontalLayout5 = QHBoxLayout()
        self.chartview = QChartView()
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.setObjectName("chartview")
        self.horizontalLayout5.addWidget(self.chartview)
        self.horizontalLayout6.addLayout(self.horizontalLayout5)
        self.horizontalLayout6.setStretch(0, 2)
        self.horizontalLayout6.setStretch(1, 1)
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
        self.pushButton_findStudent.setText(_translate("MainWindow", "查询学生信息"))
        self.pushButton_deleteStudent.setText('删除学生信息')
        self.pushButton_modifyStudent.setText('修改学生信息')
        self.pushButton_save.setText('保存数据')
        self.label_id.setText(_translate("MainWindow", "学号"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_math.setText(_translate("MainWindow", "数学"))
        self.label_english.setText(_translate("MainWindow", "英语"))
        self.label_python.setText(_translate("MainWindow", "编程"))
        self.pushButton_insertStudent.setText(_translate("MainWindow", "添加"))
 
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "数学"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "英语"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "编程"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "总分"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "平均分"))
 
 
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
 
        # 初始化
        try:
            self.openDefaultData()
        except:
            pass
 
    # 饼图可视化
    def create_piechart(self):
        notsix = 0
        six = 0
        seven = 0
        eight = 0
        nine = 0
        sum = 0
        series = QPieSeries()
        for i in range(self.index_ui.tableWidget.rowCount()):
            if self.index_ui.tableWidget.item(i, 6):
 
                if float(self.index_ui.tableWidget.item(i, 6).text()) < 60:
                    notsix += 1
                elif float(self.index_ui.tableWidget.item(i, 6).text()) < 70:
                    six += 1
                elif float(self.index_ui.tableWidget.item(i, 6).text()) < 80:
                    seven += 1
                elif float(self.index_ui.tableWidget.item(i, 6).text()) < 90:
                    eight += 1
                elif float(self.index_ui.tableWidget.item(i, 6).text()) <= 100:
                    nine += 1
        if notsix > 0:
            series.append("0-60", notsix)
            series0 = series.slices()[sum]
            series0.setLabelVisible(True)
            sum += 1
        if six > 0:
            series.append("60-70", six)
            series0 = series.slices()[sum]
            series0.setLabelVisible(True)
            sum += 1
        if seven > 0:
            series.append("70-80", seven)
            series0 = series.slices()[sum]
            series0.setLabelVisible(True)
            sum += 1
        if eight > 0:
            series.append("80-90", eight)
            series0 = series.slices()[sum]
            series0.setLabelVisible(True)
            sum += 1
        if nine > 0:
            series.append("90-100", nine)
            series0 = series.slices()[sum]
            series0.setLabelVisible(True)
 
        self.chart = QChart()
        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("学生平均成绩统计")
 
        self.chart.legend().setVisible(True)
 
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.index_ui.chartview.setChart(self.chart)
 
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
        try:
            math = float(self.index_ui.lineEdit_3.text())
            english = float(self.index_ui.lineEdit_4.text())
            python = float(self.index_ui.lineEdit_5.text())
        except:
            QMessageBox.critical(self, '警告', '成绩请输入数字')
        try:
            id = self.index_ui.lineEdit.text()
            name = self.index_ui.lineEdit_2.text()
 
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
            student_data = (id, name, math,english,python,sum,average)
            sql_insert = "INSERT INTO student (id, name, math,english,python,sum,average) VALUES (%s, %s, %s, %s,%s,%s,%s)"
            try:
                cur.execute(sql_insert, student_data)
                conn.commit()
                items = [student_data]
                QMessageBox.information(self, '成功', '学生信息添加成功')
            except pymysql.Error as e:
                conn.rollback()  # Rollback the changes in case of an error
                QMessageBox.critical(self, '数据库错误', f"数据库操作失败: {e}")
            self.freshTable(items)
            self.index_ui.lineEdit.clear()
            self.index_ui.lineEdit_2.clear()
            self.index_ui.lineEdit_3.clear()
            self.index_ui.lineEdit_4.clear()
            self.index_ui.lineEdit_5.clear()
        except:
            pass
 
    # 删除学生信息模块
    def deleteStudent(self):
        # self.index_ui.tableWidget.removeRow(self.index_ui.tableWidget.currentRow())
        # self.create_piechart()
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
        self.modify_windows = QDialog(self)
        self.modify_ui = modifyStudent.Ui_Form()
        self.modify_ui.setupUi(self.modify_windows)
 
        i = self.index_ui.tableWidget.currentRow()
        self.modify_ui.pushButton.clicked.connect(self.sureModify)
        if i >= 0:
            self.modify_ui.lineEdit.setText(self.index_ui.tableWidget.item(i, 0).text())
            self.modify_ui.lineEdit_2.setText(self.index_ui.tableWidget.item(i, 1).text())
            self.modify_ui.lineEdit_3.setText(self.index_ui.tableWidget.item(i, 2).text())
            self.modify_ui.lineEdit_4.setText(self.index_ui.tableWidget.item(i, 3).text())
            self.modify_ui.lineEdit_5.setText(self.index_ui.tableWidget.item(i, 4).text())
            self.modify_windows.show()
        else:
            QMessageBox.critical(self, '警告', '请选择你要修改的学生')

    # 修改学生信息模块
    def sureModify(self):
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
            update_query = "UPDATE student SET name = %s, math = %s, english = %s, python = %s, sum = %s, average = %s WHERE id = %s"

            try:
                student_data = (name, math,english,python,sum,average,id)
                cur.execute(update_query, student_data)
                conn.commit()
                print('修改成功')
                QMessageBox.information(self,'成功','修改成功')    
            except pymysql.Error as e:
                conn.rollback() 
                QMessageBox.critical(self, '数据库错误', f"数据库操作失败: {e}")     
                self.create_piechart()
            
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
 