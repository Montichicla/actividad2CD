cadena_1='123'
cadena_2='456'

print(cadena_1 * 3)
print(cadena_1 + cadena_2)
print(('Hip '*3) + ' ' + 'Hurra!')
print(f'{"Hip " * 3} Hurra!')
print('Él le dijo: "Hola"')

print('-------------------')
#Formato de cadena o f-string
nombre= 'Juan'
print(f'El nombre del estudiante es: {nombre} y cursa el tercer semestre' )

print('-------------------')
#Funciones con cadenas (nos dará el # de elementos de la cadena)
nombre = 'Maria josé'
print(len(nombre))

print('-------------------')
#Índice
print(nombre[0])
print(nombre[-1])

print(nombre[0:5])
print(nombre[6:10])


print('-------------------')
#input
nombre = input('Cual es tu nombre?\n')
print('Tu nombre es: ', nombre)

print('-------------------')
#Find 
saludo='Bienvenido a la aplicación'
print(saludo.find('la'))
print(saludo.find('la',0,10))