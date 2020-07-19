#!/usr/bin/env python
# coding: utf-8

import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
#读取数据
datafile = u'bar1.xlsx'
data = pd.read_excel(datafile)
datafile2 = u'CoordinationCR1.xlsx'
data2 = pd.read_excel(datafile2)
datafile3 = u'CoordinationCR2.xlsx'
data3 = pd.read_excel(datafile3)
datafile4 = u'CoordinationCR3.xlsx'
data4 = pd.read_excel(datafile4)
datafile5 = u'CoordinationCR4.xlsx'
data5 = pd.read_excel(datafile5)


############################################################################
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
x_major_locator=MultipleLocator(1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(0.2)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(-0.5,11)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(0,1)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
ax.set_ylabel('Spatial Coordination Degree',fontsize='8')
ax.set_xlabel('Urban Agglomeration',fontsize='8')
##########################################################################

x = list(range(len(data['Urban Agglomeration'])))
total_width, n = 1.2, 7
width = total_width / n
plt.bar(x, data['year2014'], width=width, label='2014', tick_label=data['Urban Agglomeration'], fc='mistyrose')
#设置数字标签
for a1,b in zip(x,data['year2014']):
        plt.text(a1, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, data['year2015'], width=width, label='2015', fc='salmon')
#设置数字标签
for a1,b in zip(x,data['year2015']):
        plt.text(a1, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, data['year2016'], width=width, label='2016', fc='tomato')
#设置数字标签
for a1,b in zip(x,data['year2016']):
        plt.text(a1, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, data['year2017'], width=width, label='2017', fc='darksalmon')
#设置数字标签
for a1,b in zip(x,data['year2017']):
        plt.text(a1, b, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
plt.xticks(rotation=18, fontsize=6)

plt.legend(loc='upper right',fontsize='xx-small')
##########################################################################

ax2 = ax.twinx()  # 这个很重要噢

ax2.set_ylim([0,1])
ax2.set_ylabel('Coordination Concerntration Rate',fontsize='8')


#画折线图
a = np.array(data2.iloc[:,1:])
for i in range(11):
    plt.plot(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i],"b.-")
#设置数字标签
    for a1,b in zip(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i]):
        plt.text(a1, b+0.01, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
        
                #画折线图
a = np.array(data3.iloc[:,1:])
for i in range(11):
    plt.plot(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i],"b.-")
#设置数字标签
    for a1,b in zip(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i]):
        plt.text(a1, b+0.01, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
        
                #画折线图
a = np.array(data4.iloc[:,1:])
for i in range(11):
    plt.plot(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i],"b.-")
#设置数字标签
    for a1,b in zip(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i]):
        plt.text(a1, b+0.01, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)
        
                #画折线图
a = np.array(data5.iloc[:,1:])
for i in range(11):
    plt.plot(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i],"b.-")
#设置数字标签
    for a1,b in zip(np.arange(i+-0.2,i+0.3,0.15)+0.2,a[i]):
        plt.text(a1, b+0.01, '%.2f' % b, ha='center', va= 'bottom',fontsize=3)

plt.savefig('bar2.pdf',dpi=600,format='pdf')
plt.savefig('bar2.jpg',dpi=600,format='jpg')
plt.show()#显示图像

