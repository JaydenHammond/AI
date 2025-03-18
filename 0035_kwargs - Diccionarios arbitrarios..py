##Cuando queremos utilizar argumentos arbitrarios en diccionarios,
##*args no nos va a servir, ya que los diccionarios constan de dos partes,
##las claves y los valores. En este caso, necesitas usar **kwargs.

def colores (**kwargs):
	print("Megusta el color " + kwargs['color1'] + '.')
colores(color1='Amarillo', color2='Negro')
