#PUNTO 1
import matplotlib.pyplot as plt
Listadesnacksfav = []
listadeprecios = []
for i  in range (8):
    elemento = input('ingresa 8 de tus snacks favoritos:')
    Listadesnacksfav.append(elemento)
for i in range (8):

    elemento = float (input('ingresa los precios de tus snacks:'))
    listadeprecios.append(elemento)

#########
plt.bar(Listadesnacksfav,listadeprecios)
plt.title('Snacks favoritos')
plt.xlabel('snacks')
plt.ylabel ('precio')
plt.savefig ('graficos snacksfavoritos.png')
#########
plt.show()