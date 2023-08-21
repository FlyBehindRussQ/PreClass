import sqlite3,openpyxl

from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QCoreApplication, QRect
from DataBaseWidget import Ui_MainWindow

import os
import data

class Imports(QtWidgets.QMainWindow, Ui_MainWindow):
    def __del__(self):
        pass
    
    def __init__(self, parent=None) -> None:
        super(Imports, self).__init__(parent)
        self.setupUi(self)
        pass
    
    def freshTableList(self):
        if data.table_empty:
            self.set_Table.clear()
            self.set_Table.addItem("NULL")
            self.set_Table.setCurrentIndex(0)
        else:
            self.set_Table.clear()
            self.set_Table.addItems(data.table_list)
            self.set_Table.setCurrentIndex(data.table_index)
    
    def dial(self,text,catagory='Notice'):
        if data.nodial==1:
            pass
        else:
            data.log_counts += 1
            if catagory == "Error":
                str=f'''<p style="color:rgb(255,0,0)">[{data.log_counts}] {text}</p>'''
            elif catagory == 'Warning':
                str=f'''<p style="color:rgb(170,170,50)">[{data.log_counts}] {text}</p>'''
            else:
                str=f'''<p style="color:rgb(0,0,0)">[{data.log_counts}] {text}</p>'''
            self.dialogue.append(str)
            
    def record(self,text,catagory='Notice'):
        if catagory == "Error":
            str=f'''<p style="color:rgb(255,0,0)">[{data.log_counts}] {text}</p>'''
        elif catagory == 'Warning':
            str=f'''<p style="color:rgb(170,170,50)">[{data.log_counts}] {text}</p>'''
        else:
            str=f'''<p style="color:rgb(0,0,0)">[{data.log_counts}] {text}</p>'''
        self.coding.append(str)