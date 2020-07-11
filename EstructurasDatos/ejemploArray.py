import numpy as np
print("Array")
arreglo = np.array([1, 2, 3, 4, 5])
print(arreglo)
print("*********************************Matriz********************************************")
matriz = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

print(matriz)
matriz1 = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)

print('5th elemnto de  la 2nd dimención: ', matriz1[1, 4])
print(matriz1)

matriz2 = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ]
)
print("Tercer elemento de la ", matriz2[0, 1, 2])


matriz3 = np.array(
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]
)

print('Utimo elemento de la  2nd dimención: ', matriz3[1, -1])
