class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []


def saludo(nombre):
    print("hola ", nombre)


p = Pila()
print(p.es_vacia())
p.apilar(10)
p.apilar(9)
p.apilar(8)
p.apilar(7)
p.apilar(6)
p.apilar(5)
p.apilar(4)
p.apilar(3)
p.apilar(2)
p.apilar(1)
print(p.es_vacia())


print("HOla")
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
