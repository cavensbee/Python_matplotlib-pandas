import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
# plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 100
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData.xlsx')
type_focus = house['Focus'].groupby(house['HouseType']).agg([('户型','count'),('关注人数','sum')])
type_focus_sort = type_focus[type_focus['户型']>50].sort_values(by = '户型')
type_focus_sort.plot(kind = 'barh',title = '户型关注度分布图')
plt.xlabel('关注人数')
plt.ylabel('户型')
plt.show()