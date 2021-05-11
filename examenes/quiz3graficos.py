#PUNTO 1
import matplotlib.pyplot as plt
snacks = ['jumbo','palito de queso','galletas oreo','perro','helado']
precio = [2000,4000,3500,5000,4000]
plt.bar(snacks,precio)
#########
plt.title('Snacks favoritos')
plt.xlabel('snacks')
plt.ylabel ('precio')
plt.savefig ('graficos snacksfavoritos.png')
#########
plt.show()

#PUNTO2
cuidad1 = input("Ingresa tu cuidad favorita: ")
poblacion1 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad2 = input("Ingresa tu cuidad favorita: ")
poblacion2 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad3 = input("Ingresa tu cuidad favorita: ")
poblacion3 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad4 = input("Ingresa tu cuidad favorita: ")
poblacion4 = int(input("Ingresa la poblacion de esta cuidad: "))
cuidad5 = input("Ingresa tu cuidad favorita: ")
poblacion5 = int(input("Ingresa la poblacion de esta cuidad: "))

lista_cuidades = [cuidad1, cuidad2, cuidad3, cuidad4, cuidad5]
lista_poblaciones = [poblacion1, poblacion2, poblacion3, poblacion4, poblacion5]

plt.pie(lista_poblaciones,labels=lista_cuidades)
plt.title("grafica de torta")
plt.savefig("torta.png")
plt.show()



#PUNTO 3
print("Definicion ecg: El electrocardiograma es la representación visual de la actividad eléctrica del corazón en función del tiempo, que se obtiene.")
print("Definicion ppg; La fotopletismografía o fotopletismograma es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano.")
import pandas as pd
ecgdata = pd.read_csv("ecg.csv", sep=";")
print(ecgdata)
valor_ecg = ecgdata["valor"]

plt.plot(valor_ecg)
plt.title("Grafica ECG")
plt.xlabel("tiempo")
plt.ylabel("mV")
plt.savefig("ecg.png")
plt.show()

import pandas as pd
ecgdata2 = pd.read_csv("ppg.csv", sep=";")
print(ecgdata2)
valor_ppg = ecgdata2["valor"]

plt.plot(valor_ppg)
plt.title("Grafica PPG")
plt.xlabel("tiempo")
plt.ylabel("volumen")
plt.savefig("ppg.png")
plt.show()



