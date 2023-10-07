#primero se define una lista que tendrá nombres
nombres = ['María', 'Juan', 'Carlos', 'Laura']

#Iterador
print(iter(nombres))

numeros = ['1', '2','3', '4']
print (iter(numeros))

numero = ['1']
print (iter(numero))           

iterador = iter(nombres)
print (next(iterador))
print (next(iterador))
print (next(iterador))
print (next(iterador))
print ('\n')

#Usamos for (aquí va a ir imprimiendo las variables en orden, 1 vuelta nombre almacena María, segunda vuelta nombre almacena Juan y así sucesivamente).
for nombre in nombres:
    print (nombre)
print ('\n')

#f-string
for nombre in nombres:
    #esto se imprimirá con cada valor que esté en nombres (ya que está dentro del for)
    print (f'Mi nombre es: {nombre}')
#Esto se imprimirá una sola vez.
print('Mucho gusto en conocerlos.')
print ('\n')

#Range
for valor in range (1,5):
    print (valor)
print ('\n')

#lista numérica usando rango.
numeritos = list(range (1,6))
print (numeritos)
print ('\n')

#Lista numérica pero saltándose números
numeros_pares = list (range(2,11,2))
print(numeros_pares)
print ('\n')

#Ejercicio: crear una lista de potencias cuadradas de números impares utilizando un ciclo for. Del 1 al 21.
lista = []
for potencia in range (1,22,2):
    potencia = potencia**2
    lista.append(potencia)
print (lista)
print ('\n')


animes = ['Naruto', 'Dragon Ball', 'Pokemón', 'One piece']
print (animes[:2])
print (animes[-2:])
print (animes[::2])
print (animes[-2:-4:-1])
print ('\n')

#Copiando lista
animes_2 = animes[:]
animes_2.append ('Demon Slayer')
print (animes)
print (animes_2)
