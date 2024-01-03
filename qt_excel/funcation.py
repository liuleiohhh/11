import pandas as pd
import xlrd
# df1 = pd.read_excel(r"F:\pycharm_project\Appdev\dem01.xlsx",header=2,sheet_name="Sheet1")
# df2 = pd.read_excel(r"F:\pycharm_project\Appdev\demo2.xlsx",header=2,sheet_name="Sheet1")
#
#
# # 将表2的数据合并到表1中（根据行名和列名）
# df1.set_index("姓名")
# df2.set_index("姓名")
# #
# df1.update(df2)
#
# print(df1)

data = xlrd.open_workbook(r"F:\pycharm_project\Appdev\dem01.xlsx")
print(data)
