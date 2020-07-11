class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)


c = Cola()
c.encolar('Sofia')
c.encolar('Miguel')
c.encolar('Luis')
c.encolar('Pedro')

print(c.desencolar())
print(c.desencolar())

print(c.tamano())
