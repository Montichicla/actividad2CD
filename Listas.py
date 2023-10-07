#Crear listas
marcascoches = ['Ferrari', 'Buggati', 'Ford']
print (marcascoches)
print (marcascoches[0])
print (marcascoches[1])
print (marcascoches[2])
print ('\n')

#Modificar listas
marcascoches[0] = 'Hyundai'
print (marcascoches)
print ('\n')

#Añadir elementos a las listas
marcascoches.append('Toyota')
print (marcascoches)
print ('\n')

#Insertar elementos
marcascoches.insert(2,'Honda')
print (marcascoches)
print ('\n')

#Eliminar con índice
del marcascoches[-1]
print (marcascoches)
print ('\n')

#Eliminar elementos
popped_marca = marcascoches.pop()
print (popped_marca)
print ('\n')

#Eliminar elementos con el índice
primer_marca = marcascoches.pop(0)
print (primer_marca)
print (marcascoches)
print ('\n')

#Remover elementos por medio de su valor
marcascoches.remove('Buggati')
print (marcascoches)
print ('\n')

#Organizar lista temporal
marcascoches.append('Ford')
print (marcascoches)
marcascoches.sort()
print(marcascoches)
numeros = [3,6,8,1,4]
numeros.sort()
print (numeros)

#Longitud de una lista 
print (len(marcascoches))


