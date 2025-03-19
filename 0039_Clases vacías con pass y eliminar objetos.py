class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario22310235 = Usuario('Jayden', 'Caballero')
usuario23110292 = Usuario('Jared', 'Franquez')

# Eliminar el usuario23110292 (Jared Franquez)
del usuario23110292

usuario22310235.imprime_datos()

