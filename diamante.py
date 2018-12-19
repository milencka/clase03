class A:
    def llamada(self):
        print('llamada A')

class B(A):
    def llamada(self):
        print('llamada B')
        super().llamada()

class C(A):
    def llamada(self):
        print('llamada C')
        super().llamada()

#class D(B, C): #Python lee de izq a derecha por lo q tomara 1ro superclase B luego C, por lo tanto es distinto (C,B)
 #   pass       #Para probar comentar los super()

class D(B, C):
    def llamada(self):
        print('llamada D')
        super().llamada()
        #B.llamada(self)
        #C.llamada(self)

d = D()
d.llamada()