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

plt.axvline(0.4,color = 'black',linestyle = ':',alpha=0.5)
plt.axhline(0.9,color = 'black',linestyle = ':',alpha=0.5)

plt.xlabel(u'Coordination Degree',fontsize=14)#设置x轴，并设定字号大小
plt.ylabel(u'Coupling Degree',fontsize=10)#设置y轴，并设定字号大小

colors = ['white','cornflowerblue','red','pink','lightblue']

size=data['Coupling Coordination Degree'].rank()
n=100
plt.scatter(data['Coordination Degree'],data['Coupling Degree'],s=size*n,alpha=0.6)
#定义一个字典，将颜色跟对应的分类进行绑定
color={1:'red',2:'cornflowerblue',3:'lightblue',4:'pink'}
#增加color的参数，用列表解析式将data分类中的每个数据的数字映射到前面color的颜色中
plt.scatter(data['Coordination Degree'],data['Coupling Degree'],color=[color[i] for i in data['type']],s=size*n,alpha=0.6)


for i in range(9):
    plt.annotate(data['city'][i], xy = (data['Coordination Degree'][i], data['Coupling Degree'][i]), \
                 xytext = (data['Coordination Degree'][i]-0.007, data['Coupling Degree'][i]-0.003))
    # 这里xy是需要标记的坐标，xytext是对应的标签坐标
plt.savefig('bubble9.pdf',dpi=600,format='pdf')

plt.show()#显示图像
