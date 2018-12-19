class Felino:
    def __init__(self):
        print('Se creo un felino')

    def rugido(self):
        print('El felino dio un rugido')

class Mascota:
    def sientate(self):
        print('Sientate')

#Todas las clases descienden de un object q se puede definir asi: Gato(object)
class Gato(Felino, Mascota):
    def __init__(self, energia, hambre):  # CONSTRUCTOR con 2 parametros, este es un metodo constructor
        super(Gato, self).__init__()#Esto es para llamar al metodo de la superclase o clase padre como Felino
        self.energia = energia  # PROPIEDADES --aqui se crea una propiedad
        self.hambre = hambre  # PROPIEDADES
        print('Se creo un gato')

    def __str__(self):
        return 'Hola soy gato'

    def dormir(self): #METODO
        print('Gato durmiendo')

#Para instanciar al objeto
garfield = Gato(10,10)
garfield.dormir()
garfield.rugido()
garfield.sientate()
