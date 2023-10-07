nombre = input('Cual es tu nombre?\n')
print( nombre.upper(), 'tiene ',len(nombre), ' letras')


fecha= input('Cual es tu fecha de nacimiento? dd/mm/aaaa ')
print('Día:', fecha[0:2],'\n' 'Mes: ',fecha[3:5],'\n' 'Año: ',fecha[6:10],'\n' )

email = input('Cual es tu correo electrónico? ')
print(email[:email.find('@')]+'@uaq.edu.mx')


