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
#PUNTO 2
class Humano ():
    def __init__ (self,nombre,sexo,edad):
        self.nombre = nombre
        self.sexo = sexo 
        self.edad = edad 
    def hablar (self,mensaje):
        print(f'hola mi {self.nombre} es y te quiero preguntar como estas:',mensaje)

class Doctor (Humano):
    def calcularIMC (self,peso,estatura):
        imc = peso/ (estatura**2)
        print(f'Tu IMC ES:',imc)

humano = Humano('paulina','femenino',20)
humano.hablar('muy bien y tu')
doctor = Doctor ('manuela','femenino',30)
doctor.calcularIMC(60,1.65)

#PUNTO 3
isCorrectInfo = False
while (isCorrectInfo  == False):
    try:
        nombreIn = input('ingresa tu nombre')
        assert(nombreIn.isalpha)
        dolares = float(input('por favor ingresa tu monto en dolares'))
        euros = dolares *0.82
        print(f'hola mi nombre es {nombreIn} y tengo esta cantidad de  {euros} euros')
        isCorrectInfo = True
    except AssertionError:
        print ('ingresaste un nombre incorrecto')
    except ValueError:
        print('Tus datos son incorrectos, ingresalos nuevamente')


#PUNTO 4
nombreArchivo = "pacientes.txt"
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo,'w',encoding="UTF-8")
    descripcionArchivo = "pacientes del consultorio de neurologia"
    archivo.writelines(descripcionArchivo)
    archivo.close()

nombrePaciente = input("ingrese el nombre del paciente")
enfermedad = input ("ingrese brevemente una descripcion de la enfermedad")
valordeColsulta = 0

isCorrectInfo = False
while(isCorrectInfo == False):
    try
        valordeColsulta =int(input("ingresa el valor de la consulta"))
        isCorrectInfo = True
    except ValueError:
        print ("ingresaste un dato erroneo")

archivo = open(nombreArchivo,'a',encoding="UTF-8")
archivo.write(f"equipo: {nombrePaciente}\n")
archivo.write(f"descripcion: {enfermedad}\n")
archivo.write(f"precio de la consulta:{valordeColsulta}\n")
archivo.write("====\n")
archivo.close()
