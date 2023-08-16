from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QDialog
from PyQt5.QtCore import QCoreApplication

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)  # Adjust the size according to your needs
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_id = QLabel(Form)
        self.label_id.setObjectName("label_id")
        self.verticalLayout.addWidget(self.label_id)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label_name = QLabel(Form)
        self.label_name.setObjectName("label_name")
        self.verticalLayout.addWidget(self.label_name)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_math = QLabel(Form)
        self.label_math.setObjectName("label_math")
        self.verticalLayout.addWidget(self.label_math)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.label_english = QLabel(Form)
        self.label_english.setObjectName("label_english")
        self.verticalLayout.addWidget(self.label_english)
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)

        self.label_python = QLabel(Form)
        self.label_python.setObjectName("label_python")
        self.verticalLayout.addWidget(self.label_python)
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.clearList)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "修改学生信息"))
        self.pushButton.setText(_translate("Form", "修改"))
        self.label_id.setText(_translate("MainWindow", "学号"))
        self.label_name.setText(_translate("MainWindow", "姓名"))
        self.label_math.setText(_translate("MainWindow", "数学"))
        self.label_english.setText(_translate("MainWindow", "英语"))
        self.label_python.setText(_translate("MainWindow", "编程"))
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
