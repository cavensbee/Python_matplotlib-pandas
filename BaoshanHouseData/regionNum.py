import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(16,12))
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
region_num = house.groupby('Region2').size().sort_values(ascending=False)
x = list(range(0,len(region_num)))
y = list(region_num)
region_num.plot(kind = 'bar',alpha = 0.7)
for a,b in zip(x,y):
    plt.text(a,b+0.5,'%.0f' % b,ha = 'center',va = 'bottom',fontsize = 20)
plt.title('各个区域的房源分布数量',fontsize = 18)
plt.xticks(fontsize=18)
plt.yticks(fontproperties='songTi',fontsize=18)
plt.xlabel('地区',fontsize=18)
plt.ylabel('房源数量',fontsize=18)
plt.grid(linestyle = '--')
plt.show()