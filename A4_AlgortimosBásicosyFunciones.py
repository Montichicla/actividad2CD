import time

#Algoritmo de aproximación de soluciones:
def busqueda_aproximacion(num):
    epsilon = 0.01      #Se declara el valor de epsilon
    paso = epsilon ** 2 #lo que va a ir aumentando nuestro valor en cada ciclo while
    valor = 0.0
    while abs(valor**2 - num) >= epsilon and valor <= num: #abs es la función para -valor absoluto-
        valor += paso #valor va a ir aumentando el valor de paso
    if abs(valor**2 - num) >= epsilon:
        return None
    else:
        return valor

#Algoritmo de búsqueda binaria.
def busqueda_binaria(num):
    epsilon = 0.01
    inf = 0.0
    sup = max(1.0, num)
    valor = (sup+inf)/2

    while abs(valor**2-num) >=epsilon:
        if valor**2 < num:
            inf = valor
        else:
            sup = valor
        valor = (sup+inf)/2
    return valor

#Algoritmo de búsqueda exhaustiva:
def busqueda_exhaustiva(num):
    valor = 0 #Se inicializa variable  en 0
    while valor **2 < num:
        valor += 1
    if valor **2 == num:
        return valor
    else:
        return None
    
def menu():
    num = float(input('Escribe un número para calcular su raíz cuadrada: '))
    print('Selecciona un algoritmo para calcular la raíz cuadrada: ')
    print('1. Búsqueda por aproximación.')
    print('2. Búsqueda binaria.')
    print ('3. Búsqueda exhaustiva.')

    opcion = int(input('Ingresa el número correspondiente al algoritmo deseado: '))
    
    inicio = time.time()

    if opcion ==1:
        resultadopor = busqueda_aproximacion(num)
    elif opcion == 2:
        resultadopor = busqueda_binaria(num)
    elif opcion == 3:
        resultadopor = busqueda_exhaustiva(num)
    else: 
        print('Opción no válida')
        return
    
    if resultadopor is not None:
        print(f'La raíz cuadrada de {num} es {resultadopor: .5f}')
    else:
        print(f'No se encontró la raíz cuadrada de {num}')
    
    fin = time.time()
    print(f'Tiempo de ejecución: {fin-inicio}')

if __name__ == '__main__':
    menu()




