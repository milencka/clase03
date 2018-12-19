class Empleado:
    def __init__(self):
        self.nombre = 'Nombre'
        self.departamento ='Departamento'


class Gestor(Empleado):
    def __init__(self):
        super(Gestor,self).__init__()
        self.informes = 'Informes'


class Trabajador(Empleado):
    def __init__(self):
        super(Trabajador,self).__init__()
        self.proyectos = 'Proyectos'


class Comercial(Trabajador):
    def __init__(self):
        super(Comercial,self).__init__()
        self.participacion = 'Participacion'


class Ingeniero(Trabajador):
    def __init__(self):
        super(Ingeniero,self).__init__()
        self.area = 'Area'
