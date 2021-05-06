#GRAFICO DE BARRAS
import matplotlib.pyplot as plt
meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septembre','octubre','novimebre','diciembre']
ingresos = [987,567,897,456,999,879,897,956,342,550,342,888]
plt.bar(meses,ingresos,width=0.6,color='r')
plt.title('ingresos anuales de trabajador independiente')
plt.xlabel('meses')
plt.ylabel('ingresos X1000 en pesos')
plt.show(


#GRAFICO TORTA
import matplotlib.pyplot as plt
pielabels =['bogota', 'medellin ','cali', 'cartagena de indias']
sizes = [30,25,15,10]
explode = [0,0,0.1,0]
plt.pie(sizes,labels = pielabels)
###########
plt.title('ciudades mas grandes de colombia')
plt.show()


#PD

import pandas as pd
ecgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData)
muestras = list(ecgData['muestra'].values())
voltaje = list(ecgData['valor'].values())
import matplotlib.pyplot as plt
plt.plot(muestras,voltaje)
plt.title("fotoplestimogrsfia")
plt.xlabel("tiempo en segundos")
plt.ylabel("voltaje en mv")
plt.show()
