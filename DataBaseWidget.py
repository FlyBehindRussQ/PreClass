# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\#Lightyear#\File\College\资料\电气实践\工程训练营\Code\PreClass\DataBaseWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Monitor = QtWidgets.QTableWidget(self.centralwidget)
        self.Monitor.setGeometry(QtCore.QRect(20, 20, 791, 645))
        self.Monitor.setRowCount(20)
        self.Monitor.setColumnCount(15)
        self.Monitor.setObjectName("Monitor")
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.Monitor.setHorizontalHeaderItem(14, item)
        self.Monitor.horizontalHeader().setVisible(True)
        self.Monitor.verticalHeader().setVisible(False)
        self.logo_text = QtWidgets.QLabel(self.centralwidget)
        self.logo_text.setGeometry(QtCore.QRect(820, 20, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.logo_text.setFont(font)
        self.logo_text.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_text.setObjectName("logo_text")
        self.dialogue = QtWidgets.QTextBrowser(self.centralwidget)
        self.dialogue.setGeometry(QtCore.QRect(20, 670, 1001, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dialogue.setFont(font)
        self.dialogue.setObjectName("dialogue")
        self.pushButton_mode = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mode.setGeometry(QtCore.QRect(1020, 670, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_mode.setFont(font)
        self.pushButton_mode.setObjectName("pushButton_mode")
        self.viewer = QtWidgets.QWidget(self.centralwidget)
        self.viewer.setGeometry(QtCore.QRect(820, 100, 271, 565))
        self.viewer.setObjectName("viewer")
        self.set_Speed = QtWidgets.QComboBox(self.viewer)
        self.set_Speed.setGeometry(QtCore.QRect(100, 290, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Speed.setFont(font)
        self.set_Speed.setObjectName("set_Speed")
        self.label_1 = QtWidgets.QLabel(self.viewer)
        self.label_1.setGeometry(QtCore.QRect(153, 170, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.set_Power_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Power_lower.setGeometry(QtCore.QRect(100, 170, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Power_lower.setFont(font)
        self.set_Power_lower.setObjectName("set_Power_lower")
        self.tick_Size = QtWidgets.QCheckBox(self.viewer)
        self.tick_Size.setGeometry(QtCore.QRect(10, 130, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Size.setFont(font)
        self.tick_Size.setObjectName("tick_Size")
        self.set_Torque_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Torque_2.setGeometry(QtCore.QRect(240, 450, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Torque_2.setFont(font)
        self.set_Torque_2.setObjectName("set_Torque_2")
        self.set_PowerFactor_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_PowerFactor_upper.setGeometry(QtCore.QRect(165, 370, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_PowerFactor_upper.setFont(font)
        self.set_PowerFactor_upper.setObjectName("set_PowerFactor_upper")
        self.set_Frequency = QtWidgets.QComboBox(self.viewer)
        self.set_Frequency.setGeometry(QtCore.QRect(100, 410, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Frequency.setFont(font)
        self.set_Frequency.setObjectName("set_Frequency")
        self.label_2 = QtWidgets.QLabel(self.viewer)
        self.label_2.setGeometry(QtCore.QRect(153, 210, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.viewer)
        self.label_6.setGeometry(QtCore.QRect(153, 370, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tick_Power = QtWidgets.QCheckBox(self.viewer)
        self.tick_Power.setGeometry(QtCore.QRect(10, 170, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Power.setFont(font)
        self.tick_Power.setObjectName("tick_Power")
        self.label_7 = QtWidgets.QLabel(self.viewer)
        self.label_7.setGeometry(QtCore.QRect(153, 490, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.set_Power_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Power_upper.setGeometry(QtCore.QRect(165, 170, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Power_upper.setFont(font)
        self.set_Power_upper.setObjectName("set_Power_upper")
        self.tick_Current = QtWidgets.QCheckBox(self.viewer)
        self.tick_Current.setGeometry(QtCore.QRect(10, 250, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Current.setFont(font)
        self.tick_Current.setObjectName("tick_Current")
        self.set_Efficiency_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Efficiency_2.setGeometry(QtCore.QRect(240, 330, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Efficiency_2.setFont(font)
        self.set_Efficiency_2.setObjectName("set_Efficiency_2")
        self.set_Efficiency_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Efficiency_lower.setGeometry(QtCore.QRect(100, 330, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Efficiency_lower.setFont(font)
        self.set_Efficiency_lower.setObjectName("set_Efficiency_lower")
        self.tick_Pole = QtWidgets.QCheckBox(self.viewer)
        self.tick_Pole.setGeometry(QtCore.QRect(10, 530, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Pole.setFont(font)
        self.tick_Pole.setObjectName("tick_Pole")
        self.set_rpm_2 = QtWidgets.QPushButton(self.viewer)
        self.set_rpm_2.setGeometry(QtCore.QRect(240, 290, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_rpm_2.setFont(font)
        self.set_rpm_2.setObjectName("set_rpm_2")
        self.set_Power_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Power_2.setGeometry(QtCore.QRect(240, 170, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Power_2.setFont(font)
        self.set_Power_2.setObjectName("set_Power_2")
        self.set_Current_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Current_lower.setGeometry(QtCore.QRect(100, 250, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Current_lower.setFont(font)
        self.set_Current_lower.setObjectName("set_Current_lower")
        self.set_PowerFactor = QtWidgets.QPushButton(self.viewer)
        self.set_PowerFactor.setGeometry(QtCore.QRect(220, 370, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_PowerFactor.setFont(font)
        self.set_PowerFactor.setObjectName("set_PowerFactor")
        self.set_Size = QtWidgets.QComboBox(self.viewer)
        self.set_Size.setGeometry(QtCore.QRect(100, 130, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Size.setFont(font)
        self.set_Size.setObjectName("set_Size")
        self.tick_ID = QtWidgets.QCheckBox(self.viewer)
        self.tick_ID.setGeometry(QtCore.QRect(10, 50, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_ID.setFont(font)
        self.tick_ID.setObjectName("tick_ID")
        self.label_5 = QtWidgets.QLabel(self.viewer)
        self.label_5.setGeometry(QtCore.QRect(153, 330, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tick_Torque = QtWidgets.QCheckBox(self.viewer)
        self.tick_Torque.setGeometry(QtCore.QRect(10, 450, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Torque.setFont(font)
        self.tick_Torque.setObjectName("tick_Torque")
        self.tick_Frequency = QtWidgets.QCheckBox(self.viewer)
        self.tick_Frequency.setGeometry(QtCore.QRect(10, 410, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Frequency.setFont(font)
        self.tick_Frequency.setObjectName("tick_Frequency")
        self.set_rpm = QtWidgets.QPushButton(self.viewer)
        self.set_rpm.setGeometry(QtCore.QRect(220, 290, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_rpm.setFont(font)
        self.set_rpm.setObjectName("set_rpm")
        self.tick_Efficiency = QtWidgets.QCheckBox(self.viewer)
        self.tick_Efficiency.setGeometry(QtCore.QRect(10, 330, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Efficiency.setFont(font)
        self.tick_Efficiency.setObjectName("tick_Efficiency")
        self.set_Type = QtWidgets.QComboBox(self.viewer)
        self.set_Type.setGeometry(QtCore.QRect(100, 90, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Type.setFont(font)
        self.set_Type.setObjectName("set_Type")
        self.set_Voltage_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Voltage_lower.setGeometry(QtCore.QRect(100, 210, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Voltage_lower.setFont(font)
        self.set_Voltage_lower.setObjectName("set_Voltage_lower")
        self.set_Torque_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Torque_upper.setGeometry(QtCore.QRect(165, 450, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Torque_upper.setFont(font)
        self.set_Torque_upper.setObjectName("set_Torque_upper")
        self.tick_Speed = QtWidgets.QCheckBox(self.viewer)
        self.tick_Speed.setGeometry(QtCore.QRect(10, 290, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Speed.setFont(font)
        self.tick_Speed.setObjectName("tick_Speed")
        self.set_Current_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Current_upper.setGeometry(QtCore.QRect(165, 250, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Current_upper.setFont(font)
        self.set_Current_upper.setObjectName("set_Current_upper")
        self.set_Mass_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Mass_upper.setGeometry(QtCore.QRect(165, 490, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Mass_upper.setFont(font)
        self.set_Mass_upper.setObjectName("set_Mass_upper")
        self.set_Voltage = QtWidgets.QPushButton(self.viewer)
        self.set_Voltage.setGeometry(QtCore.QRect(220, 210, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Voltage.setFont(font)
        self.set_Voltage.setObjectName("set_Voltage")
        self.set_Torque_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Torque_lower.setGeometry(QtCore.QRect(100, 450, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Torque_lower.setFont(font)
        self.set_Torque_lower.setObjectName("set_Torque_lower")
        self.tick_Mass = QtWidgets.QCheckBox(self.viewer)
        self.tick_Mass.setGeometry(QtCore.QRect(10, 490, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Mass.setFont(font)
        self.tick_Mass.setObjectName("tick_Mass")
        self.set_Current_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Current_2.setGeometry(QtCore.QRect(240, 250, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Current_2.setFont(font)
        self.set_Current_2.setObjectName("set_Current_2")
        self.set_Company = QtWidgets.QComboBox(self.viewer)
        self.set_Company.setGeometry(QtCore.QRect(100, 10, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Company.setFont(font)
        self.set_Company.setObjectName("set_Company")
        self.set_PowerFactor_2 = QtWidgets.QPushButton(self.viewer)
        self.set_PowerFactor_2.setGeometry(QtCore.QRect(240, 370, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_PowerFactor_2.setFont(font)
        self.set_PowerFactor_2.setObjectName("set_PowerFactor_2")
        self.label_8 = QtWidgets.QLabel(self.viewer)
        self.label_8.setGeometry(QtCore.QRect(153, 450, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.set_Mass = QtWidgets.QPushButton(self.viewer)
        self.set_Mass.setGeometry(QtCore.QRect(220, 490, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Mass.setFont(font)
        self.set_Mass.setObjectName("set_Mass")
        self.set_Efficiency = QtWidgets.QPushButton(self.viewer)
        self.set_Efficiency.setGeometry(QtCore.QRect(220, 330, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Efficiency.setFont(font)
        self.set_Efficiency.setObjectName("set_Efficiency")
        self.label_3 = QtWidgets.QLabel(self.viewer)
        self.label_3.setGeometry(QtCore.QRect(153, 250, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.set_Current = QtWidgets.QPushButton(self.viewer)
        self.set_Current.setGeometry(QtCore.QRect(220, 250, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Current.setFont(font)
        self.set_Current.setObjectName("set_Current")
        self.tick_Voltage = QtWidgets.QCheckBox(self.viewer)
        self.tick_Voltage.setGeometry(QtCore.QRect(10, 210, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Voltage.setFont(font)
        self.tick_Voltage.setObjectName("tick_Voltage")
        self.set_rpm_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_rpm_upper.setGeometry(QtCore.QRect(165, 290, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_rpm_upper.setFont(font)
        self.set_rpm_upper.setObjectName("set_rpm_upper")
        self.set_rpm_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_rpm_lower.setGeometry(QtCore.QRect(100, 290, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_rpm_lower.setFont(font)
        self.set_rpm_lower.setObjectName("set_rpm_lower")
        self.set_Voltage_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Voltage_2.setGeometry(QtCore.QRect(240, 210, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Voltage_2.setFont(font)
        self.set_Voltage_2.setObjectName("set_Voltage_2")
        self.set_Power = QtWidgets.QPushButton(self.viewer)
        self.set_Power.setGeometry(QtCore.QRect(220, 170, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Power.setFont(font)
        self.set_Power.setObjectName("set_Power")
        self.set_Voltage_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Voltage_upper.setGeometry(QtCore.QRect(165, 210, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Voltage_upper.setFont(font)
        self.set_Voltage_upper.setObjectName("set_Voltage_upper")
        self.label_4 = QtWidgets.QLabel(self.viewer)
        self.label_4.setGeometry(QtCore.QRect(153, 290, 10, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.set_Mass_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_Mass_lower.setGeometry(QtCore.QRect(100, 490, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Mass_lower.setFont(font)
        self.set_Mass_lower.setObjectName("set_Mass_lower")
        self.tick_PowerFactor = QtWidgets.QCheckBox(self.viewer)
        self.tick_PowerFactor.setGeometry(QtCore.QRect(10, 370, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tick_PowerFactor.setFont(font)
        self.tick_PowerFactor.setObjectName("tick_PowerFactor")
        self.set_Pole = QtWidgets.QComboBox(self.viewer)
        self.set_Pole.setGeometry(QtCore.QRect(100, 530, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Pole.setFont(font)
        self.set_Pole.setObjectName("set_Pole")
        self.set_Torque = QtWidgets.QPushButton(self.viewer)
        self.set_Torque.setGeometry(QtCore.QRect(220, 450, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Torque.setFont(font)
        self.set_Torque.setObjectName("set_Torque")
        self.set_Efficiency_upper = QtWidgets.QLineEdit(self.viewer)
        self.set_Efficiency_upper.setGeometry(QtCore.QRect(165, 330, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_Efficiency_upper.setFont(font)
        self.set_Efficiency_upper.setObjectName("set_Efficiency_upper")
        self.set_PowerFactor_lower = QtWidgets.QLineEdit(self.viewer)
        self.set_PowerFactor_lower.setGeometry(QtCore.QRect(100, 370, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_PowerFactor_lower.setFont(font)
        self.set_PowerFactor_lower.setObjectName("set_PowerFactor_lower")
        self.set_ID = QtWidgets.QComboBox(self.viewer)
        self.set_ID.setGeometry(QtCore.QRect(100, 50, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.set_ID.setFont(font)
        self.set_ID.setObjectName("set_ID")
        self.set_Mass_2 = QtWidgets.QPushButton(self.viewer)
        self.set_Mass_2.setGeometry(QtCore.QRect(240, 490, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Mass_2.setFont(font)
        self.set_Mass_2.setObjectName("set_Mass_2")
        self.tick_Company = QtWidgets.QCheckBox(self.viewer)
        self.tick_Company.setGeometry(QtCore.QRect(10, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Company.setFont(font)
        self.tick_Company.setObjectName("tick_Company")
        self.tick_Type = QtWidgets.QCheckBox(self.viewer)
        self.tick_Type.setGeometry(QtCore.QRect(10, 90, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.tick_Type.setFont(font)
        self.tick_Type.setObjectName("tick_Type")
        self.set_Power_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Power_3.setGeometry(QtCore.QRect(80, 170, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Power_3.setFont(font)
        self.set_Power_3.setObjectName("set_Power_3")
        self.set_Voltage_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Voltage_3.setGeometry(QtCore.QRect(80, 210, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Voltage_3.setFont(font)
        self.set_Voltage_3.setObjectName("set_Voltage_3")
        self.set_Current_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Current_3.setGeometry(QtCore.QRect(80, 250, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Current_3.setFont(font)
        self.set_Current_3.setObjectName("set_Current_3")
        self.set_Efficiency_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Efficiency_3.setGeometry(QtCore.QRect(80, 330, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Efficiency_3.setFont(font)
        self.set_Efficiency_3.setObjectName("set_Efficiency_3")
        self.set_Torque_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Torque_3.setGeometry(QtCore.QRect(80, 450, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Torque_3.setFont(font)
        self.set_Torque_3.setObjectName("set_Torque_3")
        self.set_Mass_3 = QtWidgets.QPushButton(self.viewer)
        self.set_Mass_3.setGeometry(QtCore.QRect(80, 490, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_Mass_3.setFont(font)
        self.set_Mass_3.setObjectName("set_Mass_3")
        self.set_rpm_3 = QtWidgets.QPushButton(self.viewer)
        self.set_rpm_3.setGeometry(QtCore.QRect(80, 290, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_rpm_3.setFont(font)
        self.set_rpm_3.setObjectName("set_rpm_3")
        self.set_PowerFactor_3 = QtWidgets.QPushButton(self.viewer)
        self.set_PowerFactor_3.setGeometry(QtCore.QRect(80, 370, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.set_PowerFactor_3.setFont(font)
        self.set_PowerFactor_3.setObjectName("set_PowerFactor_3")
        self.set_PowerFactor_3.raise_()
        self.label_1.raise_()
        self.set_Power_lower.raise_()
        self.tick_Size.raise_()
        self.set_Torque_2.raise_()
        self.set_PowerFactor_upper.raise_()
        self.set_Frequency.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.tick_Power.raise_()
        self.label_7.raise_()
        self.set_Power_upper.raise_()
        self.tick_Current.raise_()
        self.set_Efficiency_2.raise_()
        self.set_Efficiency_lower.raise_()
        self.tick_Pole.raise_()
        self.set_rpm_2.raise_()
        self.set_Power_2.raise_()
        self.set_Current_lower.raise_()
        self.set_PowerFactor.raise_()
        self.set_Size.raise_()
        self.tick_ID.raise_()
        self.label_5.raise_()
        self.tick_Torque.raise_()
        self.tick_Frequency.raise_()
        self.set_rpm.raise_()
        self.tick_Efficiency.raise_()
        self.set_Type.raise_()
        self.set_Voltage_lower.raise_()
        self.set_Torque_upper.raise_()
        self.tick_Speed.raise_()
        self.set_Current_upper.raise_()
        self.set_Mass_upper.raise_()
        self.set_Voltage.raise_()
        self.set_Torque_lower.raise_()
        self.tick_Mass.raise_()
        self.set_Current_2.raise_()
        self.set_Company.raise_()
        self.set_PowerFactor_2.raise_()
        self.label_8.raise_()
        self.set_Mass.raise_()
        self.set_Efficiency.raise_()
        self.label_3.raise_()
        self.set_Current.raise_()
        self.tick_Voltage.raise_()
        self.set_rpm_upper.raise_()
        self.set_rpm_lower.raise_()
        self.set_Voltage_2.raise_()
        self.set_Power.raise_()
        self.set_Voltage_upper.raise_()
        self.label_4.raise_()
        self.set_Mass_lower.raise_()
        self.tick_PowerFactor.raise_()
        self.set_Pole.raise_()
        self.set_Torque.raise_()
        self.set_Efficiency_upper.raise_()
        self.set_PowerFactor_lower.raise_()
        self.set_ID.raise_()
        self.set_Mass_2.raise_()
        self.tick_Company.raise_()
        self.tick_Type.raise_()
        self.set_Power_3.raise_()
        self.set_Voltage_3.raise_()
        self.set_Current_3.raise_()
        self.set_Efficiency_3.raise_()
        self.set_Torque_3.raise_()
        self.set_Mass_3.raise_()
        self.set_rpm_3.raise_()
        self.set_Speed.raise_()
        self.coding = QtWidgets.QTextBrowser(self.centralwidget)
        self.coding.setGeometry(QtCore.QRect(20, 700, 1001, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.coding.setFont(font)
        self.coding.setObjectName("coding")
        self.editor = QtWidgets.QWidget(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(820, 100, 271, 565))
        self.editor.setObjectName("editor")
        self.pushButton_imp = QtWidgets.QPushButton(self.editor)
        self.pushButton_imp.setGeometry(QtCore.QRect(10, 10, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_imp.setFont(font)
        self.pushButton_imp.setToolTipDuration(1)
        self.pushButton_imp.setObjectName("pushButton_imp")
        self.pushButton_exp = QtWidgets.QPushButton(self.editor)
        self.pushButton_exp.setGeometry(QtCore.QRect(140, 10, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_exp.setFont(font)
        self.pushButton_exp.setToolTipDuration(1)
        self.pushButton_exp.setObjectName("pushButton_exp")
        self.pushButton_new = QtWidgets.QPushButton(self.editor)
        self.pushButton_new.setGeometry(QtCore.QRect(10, 90, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_new.setFont(font)
        self.pushButton_new.setToolTipDuration(1)
        self.pushButton_new.setObjectName("pushButton_new")
        self.pushButton_cls = QtWidgets.QPushButton(self.editor)
        self.pushButton_cls.setGeometry(QtCore.QRect(140, 90, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cls.setFont(font)
        self.pushButton_cls.setToolTipDuration(1)
        self.pushButton_cls.setObjectName("pushButton_cls")
        self.pushButton_add = QtWidgets.QPushButton(self.editor)
        self.pushButton_add.setGeometry(QtCore.QRect(10, 170, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setToolTipDuration(1)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_del = QtWidgets.QPushButton(self.editor)
        self.pushButton_del.setGeometry(QtCore.QRect(140, 170, 121, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.input_new_edit = QtWidgets.QLineEdit(self.editor)
        self.input_new_edit.setGeometry(QtCore.QRect(100, 130, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.input_new_edit.setFont(font)
        self.input_new_edit.setObjectName("input_new_edit")
        self.input_new_done = QtWidgets.QPushButton(self.editor)
        self.input_new_done.setGeometry(QtCore.QRect(240, 130, 20, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.input_new_done.setFont(font)
        self.input_new_done.setObjectName("input_new_done")
        self.input_new_text = QtWidgets.QLabel(self.editor)
        self.input_new_text.setGeometry(QtCore.QRect(10, 130, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.input_new_text.setFont(font)
        self.input_new_text.setObjectName("input_new_text")
        self.set_Table = QtWidgets.QComboBox(self.centralwidget)
        self.set_Table.setGeometry(QtCore.QRect(920, 60, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.set_Table.setFont(font)
        self.set_Table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.set_Table.setObjectName("set_Table")
        self.Table_text = QtWidgets.QLabel(self.centralwidget)
        self.Table_text.setGeometry(QtCore.QRect(830, 60, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Table_text.setFont(font)
        self.Table_text.setObjectName("Table_text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(830, 90, 251, 19))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "区区数据库"))
        item = self.Monitor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.Monitor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "企业"))
        item = self.Monitor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "型号"))
        item = self.Monitor.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "类型"))
        item = self.Monitor.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "机座号"))
        item = self.Monitor.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "功率"))
        item = self.Monitor.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "电压"))
        item = self.Monitor.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "电流"))
        item = self.Monitor.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "转速"))
        item = self.Monitor.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "效率"))
        item = self.Monitor.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "功率因数"))
        item = self.Monitor.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "频率"))
        item = self.Monitor.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "转矩"))
        item = self.Monitor.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "重量"))
        item = self.Monitor.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "极数"))
        self.logo_text.setText(_translate("MainWindow", "MotorDB Viewer"))
        self.pushButton_mode.setText(_translate("MainWindow", "阅览"))
        self.label_1.setText(_translate("MainWindow", "-"))
        self.tick_Size.setText(_translate("MainWindow", "机座号"))
        self.set_Torque_2.setText(_translate("MainWindow", "⌀"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "-"))
        self.tick_Power.setText(_translate("MainWindow", "功率"))
        self.label_7.setText(_translate("MainWindow", "-"))
        self.tick_Current.setText(_translate("MainWindow", "电流"))
        self.set_Efficiency_2.setText(_translate("MainWindow", "⌀"))
        self.tick_Pole.setText(_translate("MainWindow", "极数"))
        self.set_rpm_2.setText(_translate("MainWindow", "⌀"))
        self.set_Power_2.setText(_translate("MainWindow", "⌀"))
        self.set_PowerFactor.setText(_translate("MainWindow", "√"))
        self.tick_ID.setText(_translate("MainWindow", "型号"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.tick_Torque.setText(_translate("MainWindow", "转矩"))
        self.tick_Frequency.setText(_translate("MainWindow", "频率"))
        self.set_rpm.setText(_translate("MainWindow", "√"))
        self.tick_Efficiency.setText(_translate("MainWindow", "效率"))
        self.tick_Speed.setText(_translate("MainWindow", "转速"))
        self.set_Voltage.setText(_translate("MainWindow", "√"))
        self.tick_Mass.setText(_translate("MainWindow", "重量"))
        self.set_Current_2.setText(_translate("MainWindow", "⌀"))
        self.set_PowerFactor_2.setText(_translate("MainWindow", "⌀"))
        self.label_8.setText(_translate("MainWindow", "-"))
        self.set_Mass.setText(_translate("MainWindow", "√"))
        self.set_Efficiency.setText(_translate("MainWindow", "√"))
        self.label_3.setText(_translate("MainWindow", "-"))
        self.set_Current.setText(_translate("MainWindow", "√"))
        self.tick_Voltage.setText(_translate("MainWindow", "电压"))
        self.set_Voltage_2.setText(_translate("MainWindow", "⌀"))
        self.set_Power.setText(_translate("MainWindow", "√"))
        self.label_4.setText(_translate("MainWindow", "-"))
        self.tick_PowerFactor.setText(_translate("MainWindow", "功率因数"))
        self.set_Torque.setText(_translate("MainWindow", "√"))
        self.set_Mass_2.setText(_translate("MainWindow", "⌀"))
        self.tick_Company.setText(_translate("MainWindow", "企业"))
        self.tick_Type.setText(_translate("MainWindow", "类型"))
        self.set_Power_3.setText(_translate("MainWindow", "↓"))
        self.set_Voltage_3.setText(_translate("MainWindow", "↓"))
        self.set_Current_3.setText(_translate("MainWindow", "↓"))
        self.set_Efficiency_3.setText(_translate("MainWindow", "↓"))
        self.set_Torque_3.setText(_translate("MainWindow", "↓"))
        self.set_Mass_3.setText(_translate("MainWindow", "↓"))
        self.set_rpm_3.setText(_translate("MainWindow", "↓"))
        self.set_PowerFactor_3.setText(_translate("MainWindow", "↓"))
        self.pushButton_imp.setText(_translate("MainWindow", "导入"))
        self.pushButton_exp.setText(_translate("MainWindow", "导出"))
        self.pushButton_new.setText(_translate("MainWindow", "新建表"))
        self.pushButton_cls.setText(_translate("MainWindow", "删除表"))
        self.pushButton_add.setText(_translate("MainWindow", "新增项"))
        self.pushButton_del.setText(_translate("MainWindow", "删除项"))
        self.input_new_done.setText(_translate("MainWindow", "√"))
        self.input_new_text.setText(_translate("MainWindow", "表格名称"))
        self.Table_text.setText(_translate("MainWindow", "当前表格"))
