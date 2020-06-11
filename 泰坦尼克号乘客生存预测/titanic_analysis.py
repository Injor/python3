import pandas as pd
import numpy as np
import graphviz
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import  cross_val_score
# 数据加载
train_data = pd.read_csv('./train.csv')
test_data = pd.read_csv('./test.csv')
# 数据探索
print(train_data.info())
print('-'*30)
print(train_data.describe())
print('-'*30)
print(train_data.describe(include=['O']))
print('-'*30)
print(train_data.head())
print('-'*30)
print(train_data.tail())
# 数据清洗
## 使用平均年龄来填充年龄中的nan值
train_data['Age'].fillna(train_data['Age'].mean(),inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
## 使用票价的均值来填充票价中的nan值
test_data['Fare'].fillna(test_data['Age'].mean(),inplace=True)
## 使用登陆最多的港口来填充
print(train_data['Embarked'].value_counts())
train_data['Embarked'].fillna('S',inplace=True)
test_data['Embarked'].fillna('S',inplace=True)
# 特征选择
features = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
##处理符号化的对象
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
print(dvec.feature_names_)
#构造ID3决策数
clf = DecisionTreeClassifier(criterion='entropy')
#决策树训练
clf.fit(train_features,train_labels)
#决策树预测
test_features = dvec.transform(test_features.to_dict(orient='record'))
pred_labels = clf.predict(test_features)
#得到决策树准确率
acc_decision_tree = round(clf.score(train_features,train_labels),6)
print(u'score 准确率为%4lf' % acc_decision_tree)
#K折交叉验证
acc_cross_decision_tree = np.mean(cross_val_score(clf,train_features,train_labels,cv=10))
print(u'score 交叉验证准确率为%4lf' % acc_cross_decision_tree)
#树的可视化
dot_data = export_graphviz(clf,out_file=None)
graph = graphviz.Source(dot_data)
graph.view()
