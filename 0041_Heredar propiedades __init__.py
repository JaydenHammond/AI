# Esta es la superclase
class Usuarios:
    def __init__(self, nombre, apellidos): 
        self.nombre = nombre
        self.apellidos = apellidos  

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Esta es la subclase
class UsuariosPremium(Usuarios):
    def __init__(self, nombre, apellidos, email):
        super().__init__(nombre, apellidos) 
        self.email = email

    def imprime_datos(self):
        super().imprime_datos()  
        print('Email:', self.email)  

usuario_premium = UsuariosPremium('Jayden', 'Caballero', 'a22310235@ceti.mx')
usuario_premium.imprime_datos()
