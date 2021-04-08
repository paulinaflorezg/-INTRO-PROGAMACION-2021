#PREGUNTA 1
numeroA = 160
numeroB = 4
numeroC = 2
sumar = numeroA + numeroB + numeroC
print("el resultado de la suma es" , sumar)
print (f"la suma dio ¨{sumar} exitosamente")
restar = numeroA - numeroB -numeroC
print(f"la resta dio {restar} exitosamente")
multiplicar = numeroA * numeroB * numeroC
print (f"la multiplicacion dio {multiplicar}exitosamente")
dividir = numeroA / numeroB / numeroC
print (f"la dividicion dio {dividir} exitosamente")
exponente = numeroA**numeroB**numeroC
print (f"la operacion exponencial dio {exponente}exitosamente")

#PREGUNTA 2
def mostrarlista (lista):
    for elemento in lista:
        print (elemento)
diadenacimiento = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
lugardenacimiento = ['Medellin','Bogota','Cali','Cartagena','barrabquilla','bucaramanga','manizales']
horadenacimiento = [1,2,3,4,5,6,7]
mostrarlista(diadenacimiento)
mostrarlista(lugardenacimiento)
mostrarlista(horadenacimiento)

#PREGUNTA3
def areatriangulo (base,altura):
    return base*(altura/2)
area= areatriangulo(8,2)
print(area)

#PREGUNTA 4
def infoLista (Lista):
    mayor = max (Lista)
    menor = min (Lista)
    acumulador = 0
    for elemento in Lista: 
        acumulador += elemento
    tamañolista = len (Lista)
    promedio = acumulador / tamañolista
    print (f'el numero mas grande de la lista es el {mayor},el numero mas pequeño de la lista es el {menor},y el promedio es :{promedio}')
numeroenteros = [2,4,6,8,10,12,14,16,18,20,40,60,80]
infoLista(numeroenteros)
#PREGUNTA 5
def seriefibonacci (dato):
    dato1 = 0
    dato2 = 1
    for elemento in range(dato-1):
        secuencia = dato1+dato2
        dato1 = dato2
        dato2 = secuencia
    return(dato1)
posicion = seriefibonacci(3)
print(posicion)
