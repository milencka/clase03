class OtroEjemplo:
    def __init__(self):
        self.publico = 'Publico'
        self.__privado = 'Privado'

    #Simulando el get y set de java
    def setPrivado(self, valor):
        self.__privado = valor

    def getPrivado(self):
        return self.__privado

x = OtroEjemplo()
print(x.publico)
x.publico = 'Cambie la publica'
print(x.publico)
x.setPrivado('cambie')
print(x.__privado)
