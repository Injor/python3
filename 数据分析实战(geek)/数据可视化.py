
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
N = 1000
x = np.random.randn(N)
x = np.random.randn(N)
y = np.random.randn(N)
plt.show()
plt.scatter(x,y,marker='x')
plt.show()
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
plt.plot(x,y)
plt.show()
a = np.random.randn(100)
s = pd.Series(a)
plt.hist(s)
plt.show()
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5,4,8,12,7]
plt.bar(x,y)
plt.show()
data = np.random.normal(size=(10,4))
lables = ['A','B','C','D']
plt.boxplot(data,labels=lables)
plt.show()
nums = [25,37,33,37,6]
labels = ['High-school','Bachelor','Master','Ph.d','Other']
plt.pie(x = nums,labels = labels)
plt.show()
from matplotlib.font_manager import FontProperties
labels = np.array([u"推进","KDA",u"生存",u"团战",u"发育",u"输出"])
stats = [83,61,95,67,76,88]
angles = np.linspace(0,2*np.pi,len(labels),endpoint=False)
stats = np.concatenate((stats,[stats[0]]))
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure()
ax = fig.add_subplot(111,polar=True)
ax.plot(angles,stats,'o-',linewidth=2)
ax.fill(angles,stats,alpha=0.25)
plt.show()
import seaborn as sns
iris = sns.load_dataset('iris')
sns.pairplot(iris)
plt.show()
