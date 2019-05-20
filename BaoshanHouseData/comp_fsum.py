import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(20,10))
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
comp_focus = house['Focus'].groupby(house['CompName']).agg([('小区','count'),('关注人数','sum')])
comp_fsum = comp_focus[comp_focus['小区']>20].sort_values(by = '小区')
comp_fsum.plot(kind = 'barh',title ='小区和关注人数的分布图')
plt.show()