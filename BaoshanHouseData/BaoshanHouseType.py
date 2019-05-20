import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
house = pd.read_excel(r'F:\数据分析案例\BaoShanPriceData.xlsx')
housetype = house['HouseType'].value_counts()
plt.figure(figsize=(19,16))
x = list(range(0,10))
y = list(housetype.head(10))
housetype.head(10).plot(kind = 'bar')
plt.title('户型数量分布',fontsize = 18)
plt.legend(('数量',),loc = 0,fontsize = 18)
plt.xticks(fontsize=16)
plt.yticks(fontproperties='songTi',fontsize=16)
plt.xlabel('户型',fontsize = 18)
plt.ylabel('户型数量',fontsize = 18)
for a,b in zip(x,y):
    plt.text(a,b+0.7,'%.0f' % b,ha = 'center',va = 'bottom',fontsize = 16)
plt.grid(linestyle = '--')
# plt.savefig(r'F:\数据分析案例\housetype.jpg')
plt.show()
