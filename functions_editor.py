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
                newItem = QTableWidgetItem(str(lines[i]))
                newItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.Monitor.setItem(row_count,col_count,newItem)
                col_count += 1
            row_count += 1
            col_count = 0
            if row_count==self.Monitor.rowCount():
                self.Monitor.insertRow(row_count)
        self.Monitor.removeRow(row_count)
    
    def opt_New(self):
        table_name = self.input_new_edit.text()
        self.DB_New(table_name)
        self.set_Table.addItem(table_name)
        self.set_Table.setCurrentIndex(data.table_index)
        self.pushButton_new.setVisible(True)
    
    
    def opt_Import(self):
        self.DB_Import()
        self.DB_Load()
        self.freshTableList()
        self.display_edit()
        
    def opt_Export(self):
        self.DB_Export()
    
    def init_Editor(self):
        pass
        
    def signals_Editor(self):
        self.pushButton_new.clicked.connect(lambda: self.pushButton_new.setVisible(False))
        self.input_new_done.clicked.connect(self.opt_New)
        
        # self.pushButton_cls.clicked.connect(self.opt_Cls)
        # self.pushButton_add.clicked.connect(self.opt_Add)
        # self.pushButton_del.clicked.connect(self.opt_Del)
        self.pushButton_imp.clicked.connect(self.opt_Import)
        self.pushButton_exp.clicked.connect(self.opt_Export)
        
        # self.input_cls_yes.clicked.connect(self.opt_Cls)
        # self.input_cls_no.clicked.connect(self.opt_Cls)
        
        