from imports import *

class Fstream(imports):
    def __init__(self, parent=None) -> None:
        # super(imports, self).__init__(parent)
        pass
    
    def DB_Load(self):
        if not os.path.exists("motor.db"):
            db = sqlite3.connect("motor.db")
            db.close()
        else:
            db = sqlite3.connect("motor.db")
            cur = db.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
            fetch = cur.fetchall()
            data.table_list.clear()
            data.table_len.clear()
            if len(fetch)!=0:
                data.table_empty = False
                for i in range(0,len(fetch)):
                    data.table_list.append(fetch[i][0])
                for i in range(0,len(data.table_list)):
                    cur.execute("SELECT num FROM "+data.table_list[i]+" ORDER BY num DESC LIMIT 0,1")
                    try:
                        fetch = cur.fetchall()
                        data.table_len.append(fetch[0][0])
                    except:
                        data.table_len.append(0)
                cur.execute("SELECT DISTINCT company FROM "+data.table_list[data.table_index])
                fetch = cur.fetchall()
                data.company_list = ['whole']
                data.company_index = 0
                for i in range(0,len(fetch)):
                    data.company_list.append(fetch[i][0])
                cur.execute("SELECT DISTINCT type FROM "+data.table_list[data.table_index])
                fetch = cur.fetchall()
                data.type_list = ['whole']
                data.type_index = 0
                for i in range(0,len(fetch)):
                    data.type_list.append(fetch[i][0])
                cur.execute("SELECT DISTINCT speed FROM "+data.table_list[data.table_index])
                fetch = cur.fetchall()
                data.speed_list = ['whole']
                data.speed_index = 0
                for i in range(0,len(fetch)):
                    data.speed_list.append(fetch[i][0])
                cur.execute("SELECT DISTINCT frequency FROM "+data.table_list[data.table_index])
                fetch = cur.fetchall()
                data.frequency_list = ['whole']
                data.frequency_index = 0
                for i in range(0,len(fetch)):
                    data.frequency_list.append(fetch[i][0])
            else:
                data.table_empty = True
            db.close()
    
    def DB_Read(self,index):
        if data.table_empty:
            self.dial("当前数据库中无表格！",catagory="Error")
            return
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        sql = "SELECT * FROM "+data.table_list[index]
        where = 1
        for i in range(0,7):
            if data.set_boundary[i]:
                if where:
                    where = 0
                    sql = sql+" WHERE"
                else:
                    sql = sql+" AND"
                sql = sql+" ("+data.header_boundary[i]+" between "+data.boundary[i*2]+" and "+data.boundary[i*2+1]+")"
        if data.company_index!=0:
            if where:
                where = 0
                sql = sql+" WHERE"
            else:
                sql = sql+" AND"
            sql = sql+" (company=\""+data.company_list[data.company_index]+"\")"
        if data.type_index!=0:
            if where:
                where = 0
                sql = sql+" WHERE"
            else:
                sql = sql+" AND"
            sql = sql+" (type=\""+data.type_list[data.type_index]+"\")"
        if data.speed_index!=0:
            if where:
                where = 0
                sql = sql+" WHERE"
            else:
                sql = sql+" AND"
            sql = sql+" (speed=\""+data.speed_list[data.speed_index]+"\")"
        if data.frequency_index!=0:
            if where:
                where = 0
                sql = sql+" WHERE"
            else:
                sql = sql+" AND"
            sql = sql+" (frequency=\""+data.frequency_list[data.frequency_index]+"\")"
            
        for i in range(0,7):
            if data.sort[i]==1:
                sql = sql+" ORDER BY "+data.header_boundary[i]
            elif data.sort[i]==2:
                sql = sql+" ORDER BY "+data.header_boundary[i]+" DESC"
            else:
                pass
        
        cur.execute(sql)
        self.record(sql)
        data.content = cur.fetchall()
        db.close()
    
    def DB_NewTable(self,name):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        sql = 'CREATE TABLE '+name+"(num int,company text,id text,type text,size text,power real,voltage real,current real,speed text,efficiency real,powerfactor real,frequency text,torque real,mass text,pole text)"
        cur.execute(sql)
        self.record(sql)
        data.table_index = len(data.table_list)
        db.commit()
        db.close()
    
    def DB_DropTable(self,index):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        sql = 'DROP TABLE '+data.table_list[index]
        cur.execute(sql)
        self.record(sql)
        if index==data.table_index:
            data.table_index = index - 1
        elif index<data.table_index:
            data.table_index = data.table_index - 1
        elif index>data.table_index:
            pass
        db.commit()
        db.close()
    
    def DB_AddItem(self,cargo):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        name = data.table_list[data.table_index]
        sql = f'''INSERT INTO {name}(num,company,id,type,size,power,voltage,current,speed,efficiency,powerfactor,frequency,torque,mass,pole) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        cargo.insert(0,data.table_len[data.table_index]+1)
        cur.execute(sql,cargo)
        db.commit()
        db.close()
    
    def DB_DelItem(self,index):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        name = data.table_list[data.table_index]
        sql = f'''DELETE FROM {name} WHERE (num={index})'''
        cur.execute(sql)
        self.record(sql)
        db.commit()
        db.close()
    
    
    def DB_SearchItem(self,index):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        name = data.table_list[data.table_index]
        sql = f'''SELECT * FROM {name} WHERE (num={index})'''
        cur.execute(sql)
        self.record(sql)
        data.content = cur.fetchall()
        db.close()
    
    def DB_ModifyItem(self,cargo):
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        name = data.table_list[data.table_index]
        print(cargo)
        sql = f'''UPDATE {name} SET (company="%s",id="%s",type="%s",size="%s",power="%f",voltage="%f",current="%f",speed="%s",efficiency="%f",powerfactor="%f",frequency="%s",torque="%f",mass="%s",pole="%s") WHERE (num="%d")'''
        cur.execute(sql,cargo)
        db.commit()
        db.close()
    
    def DB_Import(self):
        temp = QtWidgets.QFileDialog.getOpenFileName(self, "选取xlsx文件", r"name.xlsx","Excel File(*.xlsx;*.xls)")
        if temp[0] == '':
            self.dial("导入表格文件失败！",catagory="Error")
            return
        self.dial("导入表格文件："+temp[0],catagory="Notice")
        path = temp[0]
        name = temp[0].split('/')[-1].split('.')[0]
        file = openpyxl.load_workbook(path)
        text = file.active
        
        db = sqlite3.connect("motor.db")
        cur = db.cursor()
        sql = "CREATE TABLE "+name+"(num int,company text,id text,type text,size text,power real,voltage real,current real,speed text,efficiency real,powerfactor real,frequency text,torque real,mass text,pole text)"
        try:
            cur.execute(sql)
            self.record(sql)
            data.table_list.append(name)
            data.table_index = len(data.table_list) - 1
            data.table_len.append(0)
        except:
            pass
        sql = f'''INSERT INTO {name}(num,company,id,type,size,power,voltage,current,speed,efficiency,powerfactor,frequency,torque,mass,pole) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        for row in text.iter_rows(min_row=2,max_col=len(data.visible)-1,max_row=text.max_row):
            cargo = [cell.value for cell in row]
            if cargo[0]!=None:
                data.table_len[data.table_index] += 1
                cargo.insert(0,data.table_len[data.table_index])
                cur.execute(sql,cargo)
        db.commit()
        db.close()
    
    def DB_Export(self, index):
        if not index==-1:
            path = data.table_list[index]+".xlsx"
            book = Workbook(path)
            sheet = book.add_worksheet()
            self.DB_Read(index)
            for i, lines in enumerate(data.content):
                for j, value in enumerate(lines):
                    sheet.write(i, j, value)
            book.close()
        else:
            book = Workbook("motor.xlsx")
            for name in data.table_list:
                sheet = book.add_worksheet(name=name)
                self.DB_Read(data.table_list.index(name))
                for i, lines in enumerate(data.content):
                    for j, value in enumerate(lines):
                        sheet.write(i, j, value)
            book.close()
        self.dial("导出完毕！",catagory="Notice")