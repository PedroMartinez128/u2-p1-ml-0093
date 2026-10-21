import numpy as np

#lista
califas =np.array([60,70,90]) #array es arrglo o formacion
print("-----Ejemplo 1 imprimir califas-----")
print(califas) #Imprime la lista de califas
print(type(califas))#Muestra el tipo de arreglos
print("-----Ejemplo 2 dimensiones de un array-----")
califas =np.array(60)
print(califas)
print("Dimension:",califas.ndim)
print("-----Ejemplo 1 dimensiones de un array-----")
califas =np.array([60,70,90])
print(califas)
print("Dimension:",califas.ndim)
print("-----Ejemplo 2 dimensiones de un array-----")
califas =np.array([
    [60,70,90],
    [50,80,98]
    ])#Un arreglo de 2 dimenciones es como una tabla en Exel
print(califas)
print("Dimension:",califas.ndim)
print("-----Ejemplo 3 dimensiones de un array-----")
califas =np.array([
    [
    [60,70,90],
    [50,80,98]
    ],
    [
    [60,70,90],
    [50,80,98]
    ]
    ])#Un arreglo de 2 dimenciones es como una tabla en Exel
print(califas)
print("Dimension:",califas.ndim)