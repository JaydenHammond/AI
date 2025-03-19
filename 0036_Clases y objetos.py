class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario22310235 = Usuario()

usuario22310235.nombre = 'Jayden'
usuario22310235.apellidos = 'Caballero'

usuario22310235.imprime_datos()
