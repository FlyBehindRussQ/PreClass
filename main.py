from functions_viewer import *
from functions_editor import *
from fstream import *

class MyMainWindow(Viewer,Editor,Fstream):
    def __init__(self, parent=None) -> None:
        super(Viewer, self).__init__(parent)
        super(Editor, self).__init__(parent)
        super(Fstream, self).__init__(parent)
        self.pushButton_mode.clicked.connect(lambda: self.mode_Changed(1 - data.mode))
        self.set_Table.activated.connect(self.table_Changed)
        self.mode_Changed(0)
        pass
    
    
        
    def table_Changed(self,params):
        data.table_index = params
        if data.mode==0:
            self.display_view()
        elif data.mode==1:
            self.display_edit()
    
    def mode_Changed(self, index):
        data.mode = index
        _translate = QCoreApplication.translate
        text = ["阅览","编辑"][data.mode]
        self.pushButton_mode.setText(_translate("MainWindow", text))
        self.pushButton_mode.repaint()
        text = ["MotorDB Viewer","MotorDB Editor"][data.mode]
        self.logo_text.setText(_translate("MainWindow", text))
        state = [True,False][data.mode]
        self.viewer.setVisible(state)
        self.editor.setVisible(not state)
        
        if data.mode==0:
            self.init_Viewer()
            self.signals_Viewer()
            self.display_view()
        
        if data.mode==1:
            self.init_Editor()
            self.signals_Editor()
            self.display_edit()
    