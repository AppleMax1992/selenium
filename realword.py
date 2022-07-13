
import pickle
from sklearn import preprocessing
import pandas as pd
#加载模型
f = open('rfc.pickle','rb')
model = pickle.load(f)
# f.close()
# 模型测试
path = './real_word.CSV'
# 读取数据
# print(wine.data)
# print(wine.target)
data = []
# 整行读入，节省内存
with open(path, 'r',encoding='utf-8',errors='ignore') as f:
    for line in f:
        # print(line.split(','))
        data.append(line.split(','))
        
data = pd.DataFrame(data[0:33])
# print(data)
# data = pd.read_csv(path, sep=',', header=None)

X_data=data.values
# print (data[0][0])
# 划分测试集和训练集
data_headers = X_data[1,1:5]
# print(data_headers)
print('正在训练模型')
x = X_data[1:,1:5]
# real_x = [[42529.42,44294.99,76,2297222]]
# print(x)
# 模型很不错
# for item in x:
#   # print('=====',item)
#   X_normalized = preprocessing.normalize([item], norm='l2')
#   # print(X_normalized)
#   real_y = model.predict(X_normalized)
#   print(str(real_y[0]).replace('\n', ''))
X_normalized = preprocessing.normalize([[38832.46,43707.63,227,1810456]], norm='l2')
# print(X_normalized)
real_y = model.predict(X_normalized)
print(real_y)