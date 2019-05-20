import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
plt.figure(figsize=(18,16))
area_level = [0,50,100,150,200,250]
level_label = ['小于50','50-100','100-150','150-200','200-250']
area_cut = pd.cut(house['Area'],area_level,level_label)
level_num = area_cut.value_counts()
x = list(range(0,len(level_label)))
y = list(level_num)
level_num.plot(kind ='bar',alpha = 0.5)
plt.grid(linestyle = '--')
plt.title('二手房面积分布',fontsize=18)
plt.xticks(fontproperties='songTi',fontsize=18)
plt.yticks(fontproperties='songTi',fontsize=18)
plt.xlabel('面积范围(平米)',fontsize=18)
plt.ylabel('数量(套)',fontsize=18)
plt.legend(('数量',),loc = 0,fontsize=18)
for a,b in zip(x,y):
    plt.text(a,b+0.7,'%.0f' % b,ha = 'center',va = 'bottom',fontsize = 22)
plt.show()