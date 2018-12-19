class ClaseEjemplo:
    def publico(self):#se puede usar
        print('Soy publico')

    def __private(self):#no se puede usar, se usa para detallar algun algoritmo interno propio
        print('Soy privado')

ejemplo = ClaseEjemplo()
ejemplo.publico()
ejemplo.__private()
