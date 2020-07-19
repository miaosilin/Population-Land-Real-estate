# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:59:28 2019

@author: qw
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签


#读取数据
datafile = u'C:\\Users\\miaosilin\\Desktop\\Population_land_realestate\\PLR_do\\bubble_data\\bubble_data9.xlsx'
data = pd.read_excel(datafile)
 
plt.figure(figsize=(10,5))#设置画布的尺寸
plt.title('Mid-Southern Liaoning Urban Agglomerations')
plt.axvline(0.2,color = 'black',linestyle = ':',alpha=0.5)
plt.axvline(0.4,color = 'black',linestyle = ':',alpha=0.5)
plt.axvline(0.6,color = 'black',linestyle = ':',alpha=0.5)
plt.axvline(0.8,color = 'black',linestyle = ':',alpha=0.5)
plt.axhline(0.2,color = 'black',linestyle = ':',alpha=0.5)
plt.axhline(0.4,color = 'black',linestyle = ':',alpha=0.5)
plt.axhline(0.6,color = 'black',linestyle = ':',alpha=0.5)
plt.axhline(0.8,color = 'black',linestyle = ':',alpha=0.5)

plt.xlabel(u'Coordination Degree',fontsize=14)#设置x轴，并设定字号大小
plt.ylabel(u'Coupling Degree',fontsize=10)#设置y轴，并设定字号大小
############################################################################
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
x_major_locator=MultipleLocator(0.1)
#把x轴的刻度间隔设置为1，并存在变量里
y_major_locator=MultipleLocator(0.1)
#把y轴的刻度间隔设置为10，并存在变量里
ax=plt.gca()
#ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
#把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)
#把y轴的主刻度设置为10的倍数
plt.xlim(0,1)
#把x轴的刻度范围设置为-0.5到11，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(0,1.05)
#把y轴的刻度范围设置为-5到110，同理，-5不会标出来，但是能看到一点空白
##########################################################################
colors = ['white','cornflowerblue','red','pink','lightblue']

size=data['Coupling Coordination Degree'].rank()
n=120
plt.scatter(data['Coordination Degree'],data['Coupling Degree'],s=size*n,alpha=0.6)
#定义一个字典，将颜色跟对应的分类进行绑定
color={1:'red',2:'indianred',3:'lightcoral',4:'rosybrown'}
#增加color的参数，用列表解析式将data分类中的每个数据的数字映射到前面color的颜色中
plt.scatter(data['Coordination Degree'],data['Coupling Degree'],color=[color[i] for i in data['type']],s=size*n,alpha=0.6)


for i in range(9):
    plt.annotate(data['city'][i], xy = (data['Coordination Degree'][i], data['Coupling Degree'][i]), \
                 xytext = (data['Coordination Degree'][i]-0.012, data['Coupling Degree'][i]-0.003))
    # 这里xy是需要标记的坐标，xytext是对应的标签坐标
plt.savefig('bubble9.pdf',dpi=600,format='pdf')
plt.savefig('bubble9.jpg',dpi=600,format='jpg')
plt.show()#显示图像
