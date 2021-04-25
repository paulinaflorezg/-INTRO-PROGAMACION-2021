#CLASE ELEMENTOS DIGITALES
class Torta ():
    def __init__ (self, formaIn, saborIn, alturaIn):
        print ( 'Hola les voy a mostrar mis tortas')
        self.altura = alturaIn
        self.forma = formaIn
        self.sabor = saborIn

    def hablar (self):
        print (f' Esta torta es unica debido a sus caracteristicas ')
    def todosAtributos (self):
        print(f''' esta torta tiene una forma {self.forma} que llama mucho la atencion
                    El sabor es {self.sabor}
                    lo mejor de todo es la altura que es de {self.altura} metros
        ''')


torta1 = Torta('espiral', 'vainilla', 1)
print (torta1.hablar)

torta1.todosAtributos()

print (60*'2')

class Student ():
    def __init__ (self, nombreIn, edadIn, idIn, carreraIn, semestreIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id =idIn
        self.carrera = carreraIn
        self.semestre = semestreIn
        print(f'Hola me llamo {self.nombre} tengo {self.edad} años mi id es {self.id} estudio {self.carrera} y estoy en el semestre {self.semestre}')
    def estudiar (self, materia):
        print(f'Estoy estudiando la materia {materia} hoy')
    def tiempoEstudio (self, tiempoEstudioMateria):
        print(f'Esta materia la veo {tiempoEstudioMateria} semestres')


estudiante = Student('juanita', 25, 657409, 'nutricion', 'quinto')
estudiante.estudiar  ('quimica')
estudiante.tiempoEstudio (5)

print (60*'3')


class Nutri ():
    def __init__ (self, nombreIn, edadIn, uniIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.universidad = uniIn
        print(f'Hola me llamo {self.nombre} tengo {self.edad} años soy su nutricionista y estudie en el {self.universidad}')
    def imc (self, pesoIn, alturaIn):
        imc = pesoIn / (alturaIn)**2
        print(f' mi indice de masa corporal es {imc} kilos')

nutri1 = Nutri( 'valentina', 24, 'UPb')
nutri1.imc (45, 1.55)

print (60*'4')


class Cangu ():
    def __init__ (self, nombreIn, edadIn, idIn):
        self.nombre = nombreIn
        self.edad = edadIn
        self.id = idIn
    def numeroSaltos (self, saltos):
        for i in range (saltos):
            print (f"Hola soy {self.nombre} y he saltado {i+1} veces")

Cangurito = Cangu('lola', 26, 2453885)
Cangurito.numeroSaltos (23)




class Instrumento ():
    def __init__ (self, nombreIn, tipoIn, colorIn):
        self.nombre = nombreIn
        self.tipo = tipoIn
        self.color = colorIn
    def cancion (self, nombreCancion):
        print(f'con el instrumento {self.nombre} de tipo {self.tipo} de color {self.color} vamos a tocar la cancion {nombreCancion}')

Instrumento1 = Instrumento('flauta', 'viento', 'blanco')
Instrumento1.cancion ('estrellita')












