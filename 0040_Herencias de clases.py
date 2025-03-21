# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos): 
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios):
    pass  # Hereda todo de Usuarios

usuario_normal = UsuariosPremium('Jayden', 'Caballero')
usuario_premium = Usuarios('Jared', 'Franquez')

usuario_normal.imprime_datos()
usuario_premium.imprime_datos()
