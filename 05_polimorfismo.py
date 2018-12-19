#Mismo metodo diferentes acciones
class Persona:
    def saludo(self):
        print('Hola')
    def comer(self, param1, param2):
        print('comer persona \n')

#class Peruano(Persona):
#    pass #Al panerlo pass es qye no voy a implementar nada solo llamara a los metodos de la clase padre

class Peruano(Persona):
    def saludo(self): #Aqui sobreescribo la funcion 'saludo' de la superclase
        print('Hablaaa')

    def comer(self): #Sobreescribo metodo de la clase padre, pero sin parametros
        print('aca se come rico \n')

class Chileno(Persona):
    def saludo(self):
        print('Hola Gallo')

persona = Persona()
persona.saludo()
persona.comer(1,2)

peruano = Peruano()
peruano.saludo()
#peruano.comer(1,2)
peruano.comer()

chileno=Chileno()
chileno.saludo()
