def decorador(funcion):
    def funcion_envoltura():
        print('antes de la funcion')
        funcion()
        print('Despues de la funcion')

    return funcion_envoltura

#def funcionPrueba():
#    print('Hola funcion')

@decorador
def funcionPrueba():
    print('Hola funcion')

funcionPrueba()
