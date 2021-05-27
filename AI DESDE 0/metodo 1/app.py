# TUTORIAL DE PANDAS. BIBLIOTECA PARA LA MANIPULACION DE DATOS

import pandas as pd
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt

# CARGAR INFO DE CAR.DATA
try:
    data = pd.read_csv('AI DESDE 0/metodo 1/car.csv', header = None)
except:
    data = pd.read_csv('car.csv', header = None)
#LE INDICAMOS LAS CABECERAS QUE TIENE.
data.columns=['Price','Maintenance Cost','Nmber Of Doors','Capacity','Size Of Luggage Boot','Safety','Decision']

# print(data.tail(3))     #MOSTRAR LOS ULTIMOS 3
# print(data.shape)       #MOSTRANDO LA CANTIDAD FILAS Y COLUMNAS.
# print(data.size)        #MOSTRANDO EL TOTAL DE LOS DATOS
# print(data['Price'])  #MOSTRANDO SOLO PRICE
# print(data['Price'][:3])    #MOSTRANDO SOLO 3
# print(data[['Price','Decision']].tail())    #MOSTRAR PRICE Y DECISION.
# print(data['Decision'].value_counts())      #CONTAR LOS REGISTROS QUE SE REPITEN
# print(data['Decision'].value_counts().sort_index(ascending = True)) #CONTAR LOS REGISTROS QUE SE REPITEN Y LO ORDENA ASC
# decision = data['Decision'].value_counts()
# decision.plot(kind='bar')
# 
# data['Price'].unique()
# data['Price'].replace(('vhigh','high','med','low'), (4,3,2,1), inplace= True)
# print(data['Price'].unique())

# price = data['Price'].value_counts()
# colors=['#DD4E01','#CC0101','#FE10D1','#BCC111']

# plt.xlabel('Precio')
# plt.ylabel('Autos')
# plt.title('Precio de los autos')
# price.plot(kind='bar',color=colors)
# plt.show()
# 

data['Safety'].unique()
data['Safety'].value_counts()

labels = ['low','med','high']
size = [576,576,576]
colors = ['cyan','gray','orange']
explode = [0.1,0,0]
plt.pie(size,labels = labels,colors = colors, explode=explode, shadow=True,autopct='%.2f%%')
plt.title('Niveles de seguridad',fontsize=10)
plt.axis('off')
plt.legend(loc='best')
plt.show()