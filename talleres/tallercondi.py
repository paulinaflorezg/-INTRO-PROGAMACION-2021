preguntaNumeroA = 'Ingrese el número entero A : '
preguntaNumeroB = 'Ingrese el número  entero b : '
mensajeMayor = 'El numero {} es mayor que el numero {} entonces {} > {}'
mensajeIguales = 'El numero {} es iguales que el numero {} entonces {} == {}'
numeroA = int (input (preguntaNumeroA))
numeroB = int (input (preguntaNumeroB))
if (numeroA > numeroB) :
     print (mensajeMayor.format('A','B',numeroA, numeroB)) 
elif (numeroB > numeroA) :
     print (mensajeMayor.format('B','A',numeroB, numeroA)) 
else :
      print (mensajeIguales.format('A','B',numeroA, numeroB))

preguntaEdad = 'Ingrese por favor su edad: '
mensajeClasificacion = 'Usted es un {}'
edad = int (input(preguntaEdad))
if (edad< 18) :
  print (mensajeClasificacion.format('menor de edad')) 
elif (edad >= 18 and edad <25) :
  print (mensajeClasificacion.format('Joven'))  
elif (edad >= 25 and edad <61) :
  print (mensajeClasificacion.format('Adulto'))  
else :
  print (mensajeClasificacion.format('Adulto Mayor')) 

preguntaActual = 'Ingrese el año actual : '
preguntaOtro = 'Ingrese un año cualquiera : '

mensaje = '{} {} años'
mensajeIguales = 'los años ingresados son iguales'
currentYear = int (input(preguntaActual))
randomYear = int (input(preguntaOtro))

if (currentYear>randomYear):
  resta = currentYear - randomYear
  print (mensaje.format('han pasado', resta))
elif (randomYear > currentYear) :
  resta = randomYear - currentYear
  print (mensaje.format('Faltan', resta))
else :
  print(mensajeIguales)



preguntaMedida = 'ingrese una medida en centimetros : '
preguntaUnidad = ''' ingrese en que unidades desea transformar :
  K - Kilometros
 M - Metros 
   mm -milimetros
'''

medida = float(input(preguntaMedida))
unidad = input(preguntaUnidad)

metros = medida *10**-2
kilometros = medida *10**-5
milimetros = medida *10
if (unidad == 'K'):
  print (kilometros)
elif (unidad == 'M'):
  print (metros)
elif (unidad == 'mm'):
  print (milimetros)