class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Crear instancias de Usuario con los parámetros correctos
usuario22310235 = Usuario('Jayden', 'Caballero')
usuario23110292 = Usuario('Fred', 'Franquez')

# Imprimir datos
usuario22310235.imprime_datos()
usuario23110292.imprime_datos()
