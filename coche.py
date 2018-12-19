class Vehiculo:
    def __init__(self):
        self.__color = 'Color'
        self.__ruedas = 'Ruedas'
        print('Se creo un vehiculo')

    def setColor(self, valor):
        self.__color = valor
        print('Vehiculo de color: ',valor)

    def getColor(self):
        return self.__color

    def setRuedas(self, valor):
        self.__ruedas=valor
        print('vehiculo con',valor,'ruedas')

    def getRuedas(self):
        return self.__ruedas


class Coche(Vehiculo):
    def __init__(self):
        super(Coche, self).__init__()
        self.__velocidad='Velocidad'
        self.__cilindrada = 'Cilindrada'

    def setVelocidad(self, valor):
        self.__velocidad=valor

    def getVelocidad(self):
        return self.__velocidad

    def setCilindrada(self, valor):
        self.__cilindrada=valor

    def getCilindrada(self):
        return self.__cilindrada

coche=Coche()
coche.setColor('rojo')
coche.setRuedas(4)
