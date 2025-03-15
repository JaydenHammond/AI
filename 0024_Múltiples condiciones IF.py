entrada = input('Que gustas comer:\n Pizza\n Hamburguesa\n Nachos\n Un caballo\n').strip().lower()
#el int solo se ocupa si estas expresando un numero
if entrada == 'pizza':
    print('Solo tenemos de queso')
elif entrada == 'hamburguesa':
    print('Lo pediste sin queso')
elif entrada == 'nachos':
    print('Buena opción, pero ya no hay queso')
elif entrada == 'un caballo':
    print('WOW, tienes mucha hambre')
else:
    print('Esa opción no está en el menú')
