import sqlite3,openpyxl
from xlsxwriter.workbook import Workbook

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QCoreApplication, QRect
from DataBaseWidget import Ui_MainWindow

import os
import data

class imports(QtWidgets.QMainWindow, Ui_MainWindow):
    def __del__(self):
        pass
    
    def __init__(self, parent=None) -> None:
        super(imports, self).__init__(parent)
        self.setupUi(self)
        pass
    
    def freshTableList(self):
        self.set_Table.clear()
        self.set_Table.addItems(data.table_list)
        self.set_Table.setCurrentIndex(data.table_index)
    
    def dial(self,text,catagory='Notice'):#区分Error、Warning、Notice
        if data.nolog==1:
            pass
        else:
            data.log_counts += 1
            if catagory == "Error":
                str=f'''<p style="color:rgb(255,0,0)">[{data.log_counts}] {text}</p>'''
            elif catagory == 'Warning':
                str=f'''<p style="color:rgb(200,180,0)">[{data.log_counts}] {text}</p>'''
            else:
                str=f'''<p style="color:rgb(0,0,0)">[{data.log_counts}] {text}</p>'''
            self.dialogue.append(str)
            
    def record(self,text):
        data.code_counts += 1
        str=f'''[{data.code_counts}] {text}'''
        self.coding.append(str)