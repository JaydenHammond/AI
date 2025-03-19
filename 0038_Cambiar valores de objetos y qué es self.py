class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos 

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Crear instancias de Usuario correctamente
usuario22310235 = Usuario('Jayden', 'Caballero')
usuario23110292 = Usuario('Jared', 'Franquez')

# No sobrescribimos el objeto con una cadena
usuario23110292 = Usuario('Fred', 'Robins')

# Imprimir datos correctamente
usuario22310235.imprime_datos()
usuario23110292.imprime_datos()
