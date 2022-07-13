import pandas as pd
import sklearn.metrics as sm
from sklearn.ensemble import RandomForestClassifier
import sklearn.utils as su  # 打乱数据
import pickle
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
import csv 
import numpy as np
import re
from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data,wine.target,test_size=0.3)
path = './result.CSV'
# 读取数据
# print(wine.data)
# print(wine.target)
data = []
# 整行读入，节省内存
with open(path, 'r',encoding='utf-8',errors='ignore') as f:
    for line in f:
        # print(line.split(','))
        data.append(line.split(','))
# print(data[:10])       
data =  np.array(data)
# print(data)
# data = pd.read_csv(path, sep=',', header=None)

X_data=data
# print (X_data)
# 划分测试集和训练集
data_headers = X_data[1,1:5]
# print(data_headers)
print('正在训练模型')
x = X_data[1:,1:5]

# print(x)
y = X_data[1:,5]
print(y)
# print(y)
# finalY = []
# for item in y:
#     finalY.append([item])
# finalY = pd.DataFrame(finalY).values
# print(len(finalY))
# for item in y :
#     finalY.append(re.findall(r"\d+\.?\d*",item)[0])
# print(finalY)
x, y = su.shuffle(x, y, random_state=7)  # 打乱样本
X_normalized = preprocessing.normalize(x, norm='l2')
# Y_normalized = preprocessing.normalize(y, norm='l2')
Y_normalized = y
train_size = int(len(x) * 0.9)
# print(y.info())
# train_size以内的做训练集，train_size以外的做测试集
train_x, test_x, train_y, test_y = X_normalized[:train_size], X_normalized[train_size:], Y_normalized[:train_size], Y_normalized[train_size:]
# print(x)
# print(train_y)
train_y = list(map(float,train_y))
# print(train_x)
train_y = np.array(train_y)
print(train_y)
# 训练模型
# model = RandomForestClassifier(n_estimators=25)

# model.fit(train_x, train_y)


#存储模型
# f = open('rfc.pickle','wb')
# pickle.dump(model,f)
# f.close()
#加载模型
f = open('rfc.pickle','rb')
model = pickle.load(f)
f.close()
# 模型测试
# score = model.score(test_x, test_y)
# # 计算总的精度
# print('score',score)
# result = model.predict(test_x)
# plt.figure()
# # plt.plot(np.arange(len(result)), test_y, "go-", label="True value")
# plt.plot(np.arange(len(result)), result, "ro-", label="Predict value")
# plt.title(f"RandomForest---score:{score}")
# plt.legend(loc="best")
# plt.show()

# pred_test_y = model.predict(test_x)
# 模型评估
# print(test_y)
# print('aaaaa', pred_test_y)
# print('模型的r2_score得分：', r2_score(test_y, pred_test_y))


#####【TIME WARNING: 30 seconds】#####
scorel = []
for i in range(0,200,10):
	# 令 n_estimators = 1,11,21,31...,191 
    rfc = RandomForestClassifier(n_estimators=i+1,
                                 n_jobs=-1,
                                 random_state=90)
    score = cross_val_score(rfc,train_x,train_y.astype(str),cv=10).mean() #交叉验证
    scorel.append(score) #将每次n_estimators不同的交叉验证的准确度放入scorel列表
    
#打印最高的交叉验证准确度及其索引
#list.index([object]) 返回这个object在列表list中的索引
print(max(scorel),(scorel.index(max(scorel))*10)+1) 

plt.figure(figsize=[20,5])
plt.plot(range(1,201,10),scorel)
plt.show()

# 绘制学习曲线
# train_sizes = np.linspace(0.1, 1, 10)
# _, train_scores, test_scores = learning_curve(model, train_x, train_y.astype(str), train_sizes=train_sizes, cv=5)
# print(test_scores)
# print(np.mean(test_scores,axis=1))
