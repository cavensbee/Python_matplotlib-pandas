import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(16,9))
plt.rcParams['figure.dpi'] = 150
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData_BeiFen.xlsx')
reg_price = house.groupby('Region2').mean()['UnitPrice'].round(decimals = 2)
reg_price = pd.DataFrame(reg_price)
reg_uniprice = reg_price.sort_values(by = ['UnitPrice'],ascending=False)
reg_uniprice.plot(kind = 'bar',title = '各个地区的平均房价')
plt.grid(linestyle = '--')
plt.xlabel('地区',fontsize = 18)
plt.ylabel('平均价格',fontsize = 18)
plt.legend(('平均价格',),loc = 0,fontsize = 18)
plt.show()