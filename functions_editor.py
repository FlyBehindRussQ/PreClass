from fstream import *

class Editor(Fstream):
    def __init__(self, parent=None) -> None:
        # super().__init__(parent)
        pass
    
    def display_edit(self):
        self.Monitor.clearContents()
        self.Monitor.setRowCount(1)
        self.DB_Read(data.table_index)
        
        col_count = 0
        _translate = QCoreApplication.translate
        for i in range(0,len(data.visible)):
            item = self.Monitor.horizontalHeaderItem(col_count)
            item.setText(_translate("MainWindow", data.header[i]))
            col_count += 1
        
        row_count = 0
        col_count = 0
        for lines in data.content:
            for i in range(0,len(data.visible)):
                newItem = QtWidgets.QTableWidgetItem(str(lines[i]))
                newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.Monitor.setItem(row_count,col_count,newItem)
                col_count += 1
            row_count += 1
            col_count = 0
            if row_count==self.Monitor.rowCount():
                self.Monitor.insertRow(row_count)
        self.Monitor.removeRow(row_count)
    
    
    def data_Import(self):
        self.DB_Import()
        self.DB_Load()
        self.freshTableList()
        self.display_edit()
        
        
    def data_Export(self):
        self.DB_Export()
        
        
    def opt_New(self):
        Widget = QtWidgets.QDialog(self)
        Widget.resize(260, 105)
        Widget.setWindowTitle("创建新表格")
        font = QFont()
        font.setPointSize(15)
        self.NewTableWidget = QtWidgets.QWidget(Widget)
        self.input_new_text = QtWidgets.QLabel(self.NewTableWidget)
        self.input_new_text.setGeometry(QRect(10, 10, 100, 40))
        self.input_new_text.setFont(font)
        self.input_new_text.setText("表格名称：")
        self.input_new_edit = QtWidgets.QLineEdit(self.NewTableWidget)
        self.input_new_edit.setAlignment(Qt.AlignRight)
        self.input_new_edit.setGeometry(QRect(100, 10, 150, 40))
        self.input_new_edit.setFont(font)
        self.input_new_edit.setText("表格"+str(len(data.table_list)+1))
        self.input_new_done = QtWidgets.QPushButton(self.NewTableWidget)
        self.input_new_done.setGeometry(QRect(20, 55, 220, 40))
        self.input_new_done.setFont(font)
        self.input_new_done.setText("创建新表格")
        self.input_new_done.clicked.connect(self.data_New)
        self.input_new_done.clicked.connect(Widget.close)
        Widget.exec_()
        
    
    def data_New(self):
        table_name = self.input_new_edit.text()
        self.DB_New(table_name)
        self.freshTableList()
        self.display_edit()
        
    
    def opt_Drp(self):
        Widget = QtWidgets.QDialog(self)
        Widget.resize(260, 105)
        Widget.setWindowTitle("删除表格")
        font = QFont()
        font.setPointSize(15)
        self.DrpTableWidget = QtWidgets.QWidget(Widget)
        self.input_drp_text = QtWidgets.QLabel(self.DrpTableWidget)
        self.input_drp_text.setGeometry(QRect(10, 10, 100, 40))
        self.input_drp_text.setFont(font)
        self.input_drp_text.setText("表格名称：")
        self.input_drp_edit = QtWidgets.QComboBox(self.DrpTableWidget)
        self.input_drp_edit.setGeometry(QRect(100, 10, 150, 40))
        self.input_drp_edit.setFont(font)
        self.input_drp_edit.addItems(data.table_list)
        self.input_drp_edit.setCurrentIndex(data.table_index)
        self.input_drp_done = QtWidgets.QPushButton(self.DrpTableWidget)
        self.input_drp_done.setGeometry(QRect(20, 55, 220, 40))
        self.input_drp_done.setFont(font)
        self.input_drp_done.setText("确认删除表格")
        self.input_drp_done.clicked.connect(self.data_Drp)
        self.input_drp_done.clicked.connect(Widget.close)
        Widget.exec_()
        
    
    def data_Drp(self):
        index = self.input_drp_edit.currentIndex()
        self.DB_Drp(index)
        self.freshTableList()
        self.display_edit()
    
    
    def opt_Add(self):
        Widget = QtWidgets.QDialog(self)
        Widget.resize(480, 420)
        Widget.setWindowTitle("新增数据项")
        font = QFont()
        font.setPointSize(15)
        self.AddItemWidget = QtWidgets.QWidget(Widget)
        self.input_company_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_company_text.setGeometry(QRect(10, 10, 60, 40))
        self.input_company_text.setFont(font)
        self.input_company_text.setText("企业")
        self.input_company_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_company_edit.setGeometry(QRect(70, 10, 150, 40))
        self.input_company_edit.setFont(font)
        self.input_company_edit.setText("")
        self.input_id_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_id_text.setGeometry(QRect(250, 10, 60, 40))
        self.input_id_text.setFont(font)
        self.input_id_text.setText("型号")
        self.input_id_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_id_edit.setGeometry(QRect(310, 10, 150, 40))
        self.input_id_edit.setFont(font)
        self.input_id_edit.setText("")
        self.input_type_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_type_text.setGeometry(QRect(10, 60, 60, 40))
        self.input_type_text.setFont(font)
        self.input_type_text.setText("类型")
        self.input_type_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_type_edit.setGeometry(QRect(70, 60, 150, 40))
        self.input_type_edit.setFont(font)
        self.input_type_edit.setText("同步磁阻电机")
        self.input_size_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_size_text.setGeometry(QRect(250, 60, 60, 40))
        self.input_size_text.setFont(font)
        self.input_size_text.setText("机座号")
        self.input_size_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_size_edit.setGeometry(QRect(310, 60, 150, 40))
        self.input_size_edit.setFont(font)
        self.input_size_edit.setText("")
        self.input_power_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_power_text.setGeometry(QRect(10, 110, 60, 40))
        self.input_power_text.setFont(font)
        self.input_power_text.setText("功率")
        self.input_power_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_power_edit.setGeometry(QRect(70, 110, 150, 40))
        self.input_power_edit.setFont(font)
        self.input_power_edit.setText("0")
        self.input_voltage_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_voltage_text.setGeometry(QRect(250, 110, 60, 40))
        self.input_voltage_text.setFont(font)
        self.input_voltage_text.setText("电压")
        self.input_voltage_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_voltage_edit.setGeometry(QRect(310, 110, 150, 40))
        self.input_voltage_edit.setFont(font)
        self.input_voltage_edit.setText("0")
        self.input_current_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_current_text.setGeometry(QRect(10, 160, 60, 40))
        self.input_current_text.setFont(font)
        self.input_current_text.setText("电流")
        self.input_current_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_current_edit.setGeometry(QRect(70, 160, 150, 40))
        self.input_current_edit.setFont(font)
        self.input_current_edit.setText("0")
        self.input_speed_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_speed_text.setGeometry(QRect(250, 160, 60, 40))
        self.input_speed_text.setFont(font)
        self.input_speed_text.setText("转速")
        self.input_speed_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_speed_edit.setGeometry(QRect(310, 160, 150, 40))
        self.input_speed_edit.setFont(font)
        self.input_speed_edit.setText("0")
        self.input_efficiency_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_efficiency_text.setGeometry(QRect(10, 210, 60, 40))
        self.input_efficiency_text.setFont(font)
        self.input_efficiency_text.setText("效率")
        self.input_efficiency_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_efficiency_edit.setGeometry(QRect(70, 210, 150, 40))
        self.input_efficiency_edit.setFont(font)
        self.input_efficiency_edit.setText("0")
        self.input_powerfactor_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_powerfactor_text.setGeometry(QRect(250, 210, 60, 40))
        self.input_powerfactor_text.setFont(font)
        self.input_powerfactor_text.setText("功率\n因数")
        self.input_powerfactor_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_powerfactor_edit.setGeometry(QRect(310, 210, 150, 40))
        self.input_powerfactor_edit.setFont(font)
        self.input_powerfactor_edit.setText("0")
        self.input_frequency_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_frequency_text.setGeometry(QRect(10, 260, 60, 40))
        self.input_frequency_text.setFont(font)
        self.input_frequency_text.setText("频率")
        self.input_frequency_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_frequency_edit.setGeometry(QRect(70, 260, 150, 40))
        self.input_frequency_edit.setFont(font)
        self.input_frequency_edit.setText("0")
        self.input_torque_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_torque_text.setGeometry(QRect(250, 260, 60, 40))
        self.input_torque_text.setFont(font)
        self.input_torque_text.setText("转矩")
        self.input_torque_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_torque_edit.setGeometry(QRect(310, 260, 150, 40))
        self.input_torque_edit.setFont(font)
        self.input_torque_edit.setText("0")
        self.input_mass_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_mass_text.setGeometry(QRect(10, 310, 60, 40))
        self.input_mass_text.setFont(font)
        self.input_mass_text.setText("重量")
        self.input_mass_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_mass_edit.setGeometry(QRect(70, 310, 150, 40))
        self.input_mass_edit.setFont(font)
        self.input_mass_edit.setText("None")
        self.input_pole_text = QtWidgets.QLabel(self.AddItemWidget)
        self.input_pole_text.setGeometry(QRect(250, 310, 60, 40))
        self.input_pole_text.setFont(font)
        self.input_pole_text.setText("极数")
        self.input_pole_edit = QtWidgets.QLineEdit(self.AddItemWidget)
        self.input_pole_edit.setGeometry(QRect(310, 310, 150, 40))
        self.input_pole_edit.setFont(font)
        self.input_pole_edit.setText("None")
        
        self.input_add_done = QtWidgets.QPushButton(self.AddItemWidget)
        self.input_add_done.setGeometry(QRect(90, 360, 300, 40))
        self.input_add_done.setFont(font)
        self.input_add_done.setText("确认新增数据项")
        self.input_add_done.clicked.connect(self.data_Add)
        self.input_add_done.clicked.connect(Widget.close)
        Widget.exec_()
    
    
    def data_Add(self):
        cargo = []
        cargo.append(self.input_company_edit.text())
        cargo.append(self.input_id_edit.text())
        cargo.append(self.input_type_edit.text())
        cargo.append(self.input_size_edit.text())
        cargo.append(float(self.input_power_edit.text()))
        cargo.append(float(self.input_voltage_edit.text()))
        cargo.append(float(self.input_current_edit.text()))
        cargo.append(self.input_speed_edit.text())
        cargo.append(float(self.input_efficiency_edit.text()))
        cargo.append(float(self.input_powerfactor_edit.text()))
        cargo.append(self.input_frequency_edit.text())
        cargo.append(float(self.input_torque_edit.text()))
        cargo.append(self.input_mass_edit.text())
        cargo.append(self.input_pole_edit.text())
        self.DB_Add(cargo)
        
            
    def opt_Del(self):
        Widget = QtWidgets.QDialog(self)
        Widget.resize(260, 105)
        Widget.setWindowTitle("删除项")
        font = QFont()
        font.setPointSize(15)
        self.DelItemWidget = QtWidgets.QWidget(Widget)
        self.input_del_text = QtWidgets.QLabel(self.DelItemWidget)
        self.input_del_text.setGeometry(QRect(10, 10, 100, 40))
        self.input_del_text.setFont(font)
        self.input_del_text.setText("项序号：")
        self.input_del_edit = QtWidgets.QLineEdit(self.DelItemWidget)
        self.input_del_edit.setAlignment(Qt.AlignRight)
        self.input_del_edit.setGeometry(QRect(100, 10, 150, 40))
        self.input_del_edit.setFont(font)
        self.input_del_edit.setText("0")
        self.input_del_done = QtWidgets.QPushButton(self.DelItemWidget)
        self.input_del_done.setGeometry(QRect(20, 55, 220, 40))
        self.input_del_done.setFont(font)
        self.input_del_done.setText("确认删除项")
        self.input_del_done.clicked.connect(self.data_Del)
        self.input_del_done.clicked.connect(Widget.close)
        Widget.exec_()
    
    
    def data_Del(self):
        pass
    
    
    def init_Editor(self):
        pass
        
    def signals_Editor(self):
        self.pushButton_imp.clicked.connect(self.data_Import)
        self.pushButton_exp.clicked.connect(self.data_Export)
        
        self.pushButton_new.clicked.connect(self.opt_New)
        self.pushButton_drp.clicked.connect(self.opt_Drp)
        self.pushButton_add.clicked.connect(self.opt_Add)
        self.pushButton_del.clicked.connect(self.opt_Del)
        
        