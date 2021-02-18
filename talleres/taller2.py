MENSAJE_BIENVENIDA = "Hola como estas? me puedes decir dos numeros"
MENSAJE1 = "Tu numero uno es : "
MENSAJE2 = "Tu numero dos es : "


print (MENSAJE_BIENVENIDA)
NUMERO1= int(input(MENSAJE1))
NUMERO2= int(input(MENSAJE2))

isNumeroMayor = NUMERO1 > NUMERO2
print ("#"*10, "NUMERO1 es mayor que NUMERO2", "#"*10)
print (isNumeroMayor)
isNumeroMenor = NUMERO1  < NUMERO2
print ("#"*10, "NUMERO1 es menor que NUMERO2", "#"*10)
print (isNumeroMenor)

isIgual = NUMERO2 == NUMERO2
print ("#"*10, "NUMERO1 es igual que NUMERO21","#"*10)
print (isIgual)

sumar = NUMERO1 + NUMERO2
print (f"la suma dio {sumar} exitosamente")
#resta
resta = NUMERO1 - NUMERO2
print (f"la resta dio {resta} exitosamente")
#multiplicacion
multiplicar = NUMERO1 * NUMERO2
print (f"la multiplicacion dio {multiplicar} exitosamente")
#division
dividir = NUMERO1 / NUMERO2
print (f"la division dio {dividir} exitosamente")
#exponente
exponente = NUMERO1 ** NUMERO2
print (f"la operacion exponencial dio {exponente} exitosamente ")