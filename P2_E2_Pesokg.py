#Primero se crea la lista donde se almacenarán los pesos
pesos = []

#Se le pide al usuario el peso de 7 estudiantes
for i in range (7):
    peso = float(input(f'Cual es tu peso en kilogramos? {i+1} ' ))
    pesos.append(peso)

#Para ordenar la lista de menor a mayor se usa sort
pesos.sort()

#Imprimimos los pesos de menor a mayor
print('El peso de los estudiantes ordenados de menor a mayor es: ')
for peso in pesos:
    print (peso)
