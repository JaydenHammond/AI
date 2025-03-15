#Al siguiente código añádele un par de rangos de edad.
#Uno de 18 años hasta 45 y otro de más de 100 años hasta 120
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 17:
	print('Eres menor de edad.')
elif edad > 18 and edad <= 32:
	print('Eres mayor de edad.')
elif edad > 33 and edad <= 50:
	print('Eres mayor de edad, pero ya no tan joven.')
elif edad > 50 and edad <= 999:
	print('Eres muy mayor.')
else:
	print('Edad no válida.')
