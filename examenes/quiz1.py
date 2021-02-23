#resultados de triglicéridos y Homocisteína
preguntaResultado = "Ingrese sus trigliceridos"
mensajeClasificacion = "Su trigliceridos son "
resultado = int (input(preguntaResultado))
if (resultado< 150) :     
  resultado= "optimo"
  print (mensajeClasificacion,resultado)
elif (resultado >= 150 and resultado <199) :
  resultado= " es sobre el limite óptimo"
  print (mensajeClasificacion,resultado)  
elif (resultado >= 200 and resultado <499) :
  resultado=" es alto"
  print (mensajeClasificacion,resultado)  
else :
  resultado= " es muy alto"
  print (mensajeClasificacion,resultado)

preguntaHomocisteina = "Ingrese sus resultados"
mensajeClasificacion = "Su homocisteina  es "
resultado = int (input(preguntaHomocisteina))
if (resultado< 2) :     
  resultado= "optimo"
  print (mensajeClasificacion,resultado)
elif (resultado >= 2 and resultado <15) :
  resultado= " es sobre el limite óptimo"
  print (mensajeClasificacion,resultado)  
elif (resultado >= 15 and resultado <30) :
  resultado=" es alto"
  print (mensajeClasificacion,resultado)  
else :
  resultado= " es muy alto"
  print (mensajeClasificacion,resultado)







