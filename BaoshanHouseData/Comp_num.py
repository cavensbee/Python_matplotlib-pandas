import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(18,14))
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
compNum = house.groupby('CompName').size().sort_values(ascending=False)
x = list(range(0,10))
y = list(compNum.head(10))
compNum.head(10).plot(kind = 'bar',title = '各小区房源的数量')
for a,b in zip(x,y):
    plt.text(a,b+0.5,'%.0f' % b,ha = 'center',va = 'bottom',fontsize = 14,color = 'red')
plt.xlabel('小区名称')
plt.ylabel('房源数量')
plt.grid(linestyle = '--')
plt.show()