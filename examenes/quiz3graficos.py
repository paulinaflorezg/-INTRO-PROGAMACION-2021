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



