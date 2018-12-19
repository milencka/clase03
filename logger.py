def log(debug):#si el valor no varia se puede definir como log(debug=True)
    # El nombre de la funcion es el nombre del decorador y recibe la funcion que decora.
    # En este caso logger tiene como funcion registrar los parametros recibidos.
    def _log(f): #SE CAMBIA NOMBRE DE log A _log XQ DEBE SER DISTINTO DEL DECORADOR log(debug)
        # Este wrapper lo usas para atrapar los parametros de la funcion decorada
        def wrap(a,b):
            # esta es la funcionalidad de la decoracion
            if debug:
                print('valor ejemplo de a',a)
                print('valor ejemplo de b', b)
            return f(a,b)
        return wrap
    return _log

#Los decoradores pueden tener parametros
@log(debug=False) #ESTE DECORADOR CON PARAMETROS SE DEBE DEFINIR POR ENCIMA DEL DECORADOR INICIAL
def suma(a,b):
    return a+b

print(suma(1,2))
