import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 读取数据
with pd.ExcelFile('/Users/mengfanyu/Desktop/Temperature.xlsx') as xls:  # 将包含多个工作表的excel读取为一个文件夹
    df1 = pd.read_excel(xls, 'Sheet1')  # 读取单个工作表
data = np.array(df1)
jingdu = data[0,1:]
weidu = data[1:,0]
value = data[1:,1:]
X, Y = np.meshgrid(jingdu,weidu)
# 填充等高线以及色柱
CS=plt.contourf(Y, X,value,levels=30,alpha=1,cmap='jet')
plt.colorbar()
# 添加标题
plt.title("MCD_v6.1_Temperature_ls_99.9")
#添加横纵坐标
plt.xlabel("Latitude")
plt.ylabel("Longitude")
# 显示图表
plt.show()