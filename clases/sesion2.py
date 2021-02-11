pruebaV = True
pruebaF = False
print (pruebaF)
print (pruebaV)
pruebaV = pruebaF
edad =19
estatura = 1.65
peso = 60
nombre = "Paulina florez garcia"
print ("#"*15,"Mayor Edad","#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*15,"Bajo la Estatura promedio","#"*15)
isMayorEstatura = estatura < 1.65
print (isMayorEstatura)
print ("#"*15,"Peso diferente 60","#"*15)
isPesoDiferente = peso != 60
print (isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "florez"
isApellido = apellido in nombre
print ("#"*15,"Esta apellido en el nombre", "#"*15)
print (isApellido)



