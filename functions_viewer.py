from fstream import *

class Viewer(Fstream):
    def __init__(self, parent=None) -> None:
        # super().__init__(parent)
        pass
    
    def display_view(self):
        self.Monitor.clearContents()
        self.Monitor.setRowCount(20)
        self.DB_Read(data.table_index)
        
        col_count = 0
        _translate = QCoreApplication.translate
        for i in range(0,len(data.visible)):
            if data.visible[i]:
                item = self.Monitor.horizontalHeaderItem(col_count)
                item.setText(_translate("MainWindow", data.header[i]))
                col_count += 1
        for i in range(col_count,len(data.visible)):
            item = self.Monitor.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", ''))
            
        row_count = 0
        col_count = 0
        for lines in data.content:
            for i in range(0,len(data.visible)):
                if data.visible[i]:
                    newItem = QtWidgets.QTableWidgetItem(str(lines[i]))
                    newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.Monitor.setItem(row_count,col_count,newItem)
                    col_count += 1
            for i in range(col_count,len(data.visible)):
                newItem = QtWidgets.QTableWidgetItem(0)
                newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.Monitor.setItem(row_count,i,newItem)
            row_count += 1
            col_count = 0
            if row_count==self.Monitor.rowCount():
                self.Monitor.insertRow(row_count)
        self.Monitor.removeRow(row_count)
    
    
    def select_Hide(self,index):
        data.visible[index] = 1 - data.visible[index]
        self.display_view()
    
    
    def select_Sort(self,index):
        _translate = QCoreApplication.translate
        for i in range(0,7):
            if i==index:
                data.sort[i] = (data.sort[i] + 1) % 3
            else:
                data.sort[i] = 0
            text = ["↓","↑","⌀"][data.sort[i]]
            obj = [self.set_Power_3,self.set_Voltage_3,self.set_Current_3,self.set_rpm_3,self.set_Efficiency_3,self.set_PowerFactor_3,self.set_Torque_3][i]
            obj.setText(_translate("MainWindow", text))
            obj.repaint()
        self.display_view()
    
    
    def select_Company(self,params):
        data.company_index = params
        self.display_view()
     
     
    def select_ID(self):
        pass
    
    
    def select_Type(self,params):
        data.type_index = params
        self.display_view()
    
    
    def select_Size(self):
        pass
    
    
    def select_Power(self):
        if self.set_Power_lower.text()!="":
            data.set_boundary[0] = 1
            data.boundary[0] = self.set_Power_lower.text()
        else:
            data.boundary[0] = '0'
        if self.set_Power_upper.text()!="":
            data.set_boundary[0] = 1
            data.boundary[1] = self.set_Power_upper.text()
        else:
            data.boundary[1] = '99999999'
        self.display_view()
    
    
    def select_Voltage(self):
        if self.set_Voltage_lower.text()!="":
            data.set_boundary[1] = 1
            data.boundary[2] = self.set_Voltage_lower.text()
        else:
            data.boundary[2] = '0'
        if self.set_Voltage_upper.text()!="":
            data.set_boundary[1] = 1
            data.boundary[3] = self.set_Voltage_upper.text()
        else:
            data.boundary[3] = '99999999'
        self.display_view()
    
    
    def select_Current(self):
        if self.set_Current_lower.text()!="":
            data.set_boundary[2] = 1
            data.boundary[4] = self.set_Current_lower.text()
        else:
            data.boundary[4] = '0'
        if self.set_Current_upper.text()!="":
            data.set_boundary[2] = 1
            data.boundary[5] = self.set_Current_upper.text()
        else:
            data.boundary[5] = '99999999'
        self.display_view()
    
    
    def select_rpm(self):
        if self.set_rpm_lower.text()!="":
            data.set_boundary[3] = 1
            data.boundary[6] = self.set_rpm_lower.text()
        else:
            data.boundary[6] = '0'
        if self.set_rpm_upper.text()!="":
            data.set_boundary[3] = 1
            data.boundary[7] = self.set_rpm_upper.text()
        else:
            data.boundary[7] = '99999999'
        self.display_view()
    
    
    def select_Speed(self,params):
        data.speed_index = params
        self.display_view()
    
    
    def select_Efficiency(self):
        if self.set_Efficiency_lower.text()!="":
            data.set_boundary[4] = 1
            data.boundary[8] = self.set_Efficiency_lower.text()
        else:
            data.boundary[8] = '0'
        if self.set_Efficiency_upper.text()!="":
            data.set_boundary[4] = 1
            data.boundary[9] = self.set_Efficiency_upper.text()
        else:
            data.boundary[9] = '99999999'
        self.display_view()
    
    
    def select_PowerFactor(self):
        if self.set_PowerFactor_lower.text()!="":
            data.set_boundary[5] = 1
            data.boundary[10] = self.set_PowerFactor_lower.text()
        else:
            data.boundary[10] = '0'
        if self.set_PowerFactor_upper.text()!="":
            data.set_boundary[5] = 1
            data.boundary[11] = self.set_PowerFactor_upper.text()
        else:
            data.boundary[11] = '99999999'
        self.display_view()
    
    
    def select_Frequency(self,params):
        data.frequency_index = params
        self.display_view()
    
    
    def select_Torque(self):
        if self.set_Torque_lower.text()!="":
            data.set_boundary[6] = 1
            data.boundary[12] = self.set_Torque_lower.text()
        else:
            data.boundary[12] = '0'
        if self.set_Torque_upper.text()!="":
            data.set_boundary[6] = 1
            data.boundary[13] = self.set_Torque_upper.text()
        else:
            data.boundary[13] = '99999999'
        self.display_view()
    
    
    def select_Mass(self):
        pass
    
    
    def select_Pole(self):
        pass
    
    
    def reselect_Power(self):
        data.set_boundary[0] = 0
        data.boundary[0] = '0'
        data.boundary[1] = '99999999'
        self.set_Power_lower.clear()
        self.set_Power_upper.clear()
        self.display_view()
    
    
    def reselect_Voltage(self):
        data.set_boundary[1] = 0
        data.boundary[2] = '0'
        data.boundary[3] = '99999999'
        self.set_Voltage_lower.clear()
        self.set_Voltage_upper.clear()
        self.display_view()
    
    
    def reselect_Current(self):
        data.set_boundary[2] = 0
        data.boundary[4] = '0'
        data.boundary[5] = '99999999'
        self.set_Current_lower.clear()
        self.set_Current_upper.clear()
        self.display_view()
    
    
    def reselect_rpm(self):
        data.set_boundary[3] = 0
        data.boundary[6] = '0'
        data.boundary[7] = '99999999'
        self.set_rpm_lower.clear()
        self.set_rpm_upper.clear()
        self.display_view()
    
    
    def reselect_Efficiency(self):
        data.set_boundary[4] = 0
        data.boundary[8] = '0'
        data.boundary[9] = '99999999'
        self.set_Efficiency_lower.clear()
        self.set_Efficiency_upper.clear()
        self.display_view()
    
    
    def reselect_PowerFactor(self):
        data.set_boundary[5] = 0
        data.boundary[10] = '0'
        data.boundary[11] = '99999999'
        self.set_PowerFactor_lower.clear()
        self.set_PowerFactor_upper.clear()
        self.display_view()
    
    
    def reselect_Torque(self):
        data.set_boundary[6] = 0
        data.boundary[12] = '0'
        data.boundary[13] = '99999999'
        self.set_Torque_lower.clear()
        self.set_Torque_upper.clear()
        self.display_view()
    
    
    def reselect_Mass(self):
        pass
    
    
    def init_Viewer(self):
        self.DB_Load()
        self.freshTableList()
        
        data.visible = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.tick_Company.setChecked(True)
        self.tick_ID.setChecked(True)
        self.tick_Type.setChecked(True)
        self.tick_Size.setChecked(True)
        self.tick_Power.setChecked(True)
        self.tick_Voltage.setChecked(True)
        self.tick_Current.setChecked(True)
        self.tick_Speed.setChecked(True)
        self.tick_Efficiency.setChecked(True)
        self.tick_PowerFactor.setChecked(True)
        self.tick_Frequency.setChecked(True)
        self.tick_Torque.setChecked(True)
        self.tick_Mass.setChecked(True)
        self.tick_Pole.setChecked(True)
        
        self.set_Company.clear()
        self.set_Company.addItems(data.company_list)
        self.set_Company.setCurrentIndex(data.company_index)
        self.set_Type.clear()
        self.set_Type.addItems(data.type_list)
        self.set_Type.setCurrentIndex(data.type_index)
        self.set_Frequency.clear()
        self.set_Frequency.addItems(data.frequency_list)
        self.set_Frequency.setCurrentIndex(data.frequency_index)
        self.set_Speed.clear()
        self.set_Speed.addItems(data.speed_list)
        self.set_Speed.setCurrentIndex(data.speed_index)
        
        _translate = QCoreApplication.translate
        for i in range(0,7):
            data.sort[i] = 0
            obj = [self.set_Power_3,self.set_Voltage_3,self.set_Current_3,self.set_rpm_3,self.set_Efficiency_3,self.set_PowerFactor_3,self.set_Torque_3][i]
            obj.setText(_translate("MainWindow", "↓"))
            obj.repaint()
        
        self.set_ID.clear()
        self.set_ID.addItem("暂未开放！")
        self.set_Size.clear()
        self.set_Size.addItem("暂未开放！")
        self.set_Pole.clear()
        self.set_Pole.addItem("暂未开放！")
        self.set_Mass_lower.setText("暂未")
        self.set_Mass_upper.setText("开放")
        self.set_rpm.setVisible(False)
        self.set_rpm_2.setVisible(False)
        self.set_rpm_3.setVisible(False)
        self.set_rpm_lower.setVisible(False)
        self.set_rpm_upper.setVisible(False)
        self.set_PowerFactor_3.setVisible(False)
    
        
    def signals_Viewer(self):
        self.tick_Company.stateChanged.connect(lambda: self.select_Hide(1))
        self.tick_ID.stateChanged.connect(lambda: self.select_Hide(2))
        self.tick_Type.stateChanged.connect(lambda: self.select_Hide(3))
        self.tick_Size.stateChanged.connect(lambda: self.select_Hide(4))
        self.tick_Power.stateChanged.connect(lambda: self.select_Hide(5))
        self.tick_Voltage.stateChanged.connect(lambda: self.select_Hide(6))
        self.tick_Current.stateChanged.connect(lambda: self.select_Hide(7))
        self.tick_Speed.stateChanged.connect(lambda: self.select_Hide(8))
        self.tick_Efficiency.stateChanged.connect(lambda: self.select_Hide(9))
        self.tick_PowerFactor.stateChanged.connect(lambda: self.select_Hide(10))
        self.tick_Frequency.stateChanged.connect(lambda: self.select_Hide(11))
        self.tick_Torque.stateChanged.connect(lambda: self.select_Hide(12))
        self.tick_Mass.stateChanged.connect(lambda: self.select_Hide(13))
        self.tick_Pole.stateChanged.connect(lambda: self.select_Hide(14))
        
        self.set_Power_3.clicked.connect(lambda: self.select_Sort(0))
        self.set_Voltage_3.clicked.connect(lambda: self.select_Sort(1))
        self.set_Current_3.clicked.connect(lambda: self.select_Sort(2))
        # self.set_rpm_3.clicked.connect(lambda: self.select_Sort(3))
        self.set_Efficiency_3.clicked.connect(lambda: self.select_Sort(4))
        # self.set_PowerFactor_3.clicked.connect(lambda: self.select_Sort(5))
        self.set_Torque_3.clicked.connect(lambda: self.select_Sort(6))
        # self.set_Mass_3.clicked.connect(lambda: self.select_Sort(__))
        
        self.set_Company.activated.connect(self.select_Company)
        # self.set_ID.activated.connect(self.select_ID)
        self.set_Type.activated.connect(self.select_Type)
        # self.set_Size.activated.connect(self.select_Size)
        self.set_Power.clicked.connect(self.select_Power)
        self.set_Voltage.clicked.connect(self.select_Voltage)
        self.set_Current.clicked.connect(self.select_Current)
        # self.set_rpm.clicked.connect(self.select_rpm)
        self.set_Speed.activated.connect(self.select_Speed)
        self.set_Efficiency.clicked.connect(self.select_Efficiency)
        self.set_PowerFactor.clicked.connect(self.select_PowerFactor)
        self.set_Frequency.activated.connect(self.select_Frequency)
        self.set_Torque.clicked.connect(self.select_Torque)
        # self.set_Mass.clicked.connect(self.select_Mass)
        # self.set_Pole.activated.connect(self.select_Pole)
        
        self.set_Power_2.clicked.connect(self.reselect_Power)
        self.set_Voltage_2.clicked.connect(self.reselect_Voltage)
        self.set_Current_2.clicked.connect(self.reselect_Current)
        # self.set_rpm_2.clicked.connect(self.reselect_rpm)
        self.set_Efficiency_2.clicked.connect(self.reselect_Efficiency)
        self.set_PowerFactor_2.clicked.connect(self.reselect_PowerFactor)
        self.set_Torque_2.clicked.connect(self.reselect_Torque)
        # self.set_Mass_2.clicked.connect(self.reselect_Mass)
