# El diccionario, define una relación uno a uno entre claves y valores.
diccionario = {
    "clave1": 234,
    "clave2": True,
    "clave3": "Valor 1",
    "clave4": [1, 2, 3, 4]
}

print(diccionario, type(diccionario))


versiones = dict(python=3.7, clave1=2.13, clave2=5.1, clave3=2.1)
print(versiones)

print(diccionario['clave4'])
