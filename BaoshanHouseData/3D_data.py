import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
fig = plt.figure()
ax = fig.gca(projection = '3d')

house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
comp_focus = house['Focus'].groupby(house['CompName']).agg([('小区','count'),('关注人数','sum')])
comp_fsum = comp_focus[comp_focus['小区']>20].sort_values(by = '小区')
x = list(range(0,len(comp_fsum.index)))
y = list(comp_fsum['小区'])
z = list(comp_fsum['关注人数'])
scale_x = x
index_x = list(comp_fsum.index)
ax.plot(x,y,z)
plt.xticks(scale_x,index_x,rotation = 20)
plt.show()