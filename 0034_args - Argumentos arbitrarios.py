#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
print("cuatro argumentos")
colores('lila', 'negro', 'rojo')
print("tres argumentos")
colores('rosa')
print("un argumentos")
colores('marrón', 'naranja')
print("dos argumentos")

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[0], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
colores('rojo', 'amarillo')

##Crea una función que realice la suma de cinco números utilizando solo
##*args. Debes imprimir el resultado en la consola. La suma no se realizará
##directamente sobre el print().
def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)
suma(5, 7, 45, 8657, 3, 4)
