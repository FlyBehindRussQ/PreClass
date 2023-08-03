ui = None
content = None

##########################
###       Common       ###
##########################
mode = 0

nolog = 0
log_counts = 0
code_counts = 0

table_len = []
table_list = []
table_index = 0

##########################
###       Viewer       ###
##########################
visible = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
header = ['序号','企业','型号','类型','机座号','功率','电压','电流','转速','效率','功率因数','频率','转矩','重量','极数']

sort = [0,0,0,0,0,0,0]
set_boundary = [0,0,0,0,0,0,0]
boundary = ['0','99999999','0','99999999','0','99999999','0','99999999','0','99999999','0','99999999','0','99999999']
header_boundary = ['power','voltage','current','speed','efficiency','powerfactor','torque']

company_list = []
company_index = 0
type_list = []
type_index = 0
frequency_list = []
frequency_index = 0
speed_list = []
speed_index = 0

##########################
###       Editor       ###
##########################

new_table = ""