import pandas as pd
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
import numpy as np
# CARGAR INFO DE CAR.DATA
try:
    data = pd.read_csv('AI DESDE 0/metodo 1/car.csv', header = None)
except:
    data = pd.read_csv('car.csv', header = None)
#LE INDICAMOS LAS CABECERAS QUE TIENE.
data.columns=['price','maintenance','n_doors','capacity','size_lug','safety','class']

data.price.replace(('vhigh','high','med','low'),(4,3,2,1), inplace = True)
data.maintenance.replace(('vhigh','high','med','low'),(4,3,2,1), inplace = True)
data.n_doors.replace(('2','3','4','5more'),(1,2,3,4), inplace = True)
data.capacity.replace(('2','4','more'),(1,2,3), inplace = True)
data.size_lug.replace(('small','med','big'),(1,2,3), inplace = True)
data.safety.replace(('low','med','high'),(1,2,3), inplace = True)
data['class'].replace(('unacc','acc','good','vgood'),(1,2,3,4),inplace=True)

# RECOMENDACIÓN DE DIVISIÓN DE DATOS
# 80% Aprendizaje
# 20% Pruebas

dataset = data.values
X = dataset[:, 0:6]
Y = np.asarray(dataset[0:,6], dtype='S6')

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.2,random_state=0)

tr = tree.DecisionTreeClassifier(max_depth=10)
tr.fit(X_Train,Y_Train)
y_pred = tr.predict(X_Test)
print(y_pred)

score = tr.score(X_Test,Y_Test)

print('PRECISIÓN: %0.4f' %(score))