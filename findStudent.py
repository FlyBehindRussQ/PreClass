from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.label = QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        # self.pushButton1 = QPushButton(Form)
        # self.pushButton1.setObjectName("pushButton1")
        # self.verticalLayout.addWidget(self.pushButton1)
        
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.clearList)
        self.lineEdit.textChanged.connect(self.filterList)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询学生信息"))
        self.label.setText(_translate("Form", "请输入id"))
        # self.pushButton1.setText(_translate("Form","查询"))
        self.pushButton.setText(_translate("Form", "查询"))

    def clearList(self):
        self.listWidget.clear()

    def filterList(self):
        search_text = self.lineEdit.text()
        if search_text:
            count = self.listWidget.count()
            for i in range(count):
                item = self.listWidget.item(i)
                if search_text in item.text():
                    item.setHidden(False)
                else:
                    item.setHidden(True)
        else:
            count = self.listWidget.count()
            for i in range(count):
                self.listWidget.item(i).setHidden(False)
