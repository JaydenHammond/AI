#Elimina de la siguiente lista los elementos 'azul' y 'blanco'.
#Solo puedes eliminarlos utilizando el método pop().
#Además, tendrás que guardar esos dos colores en una nueva lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
color_elem1 = colores.pop(1)
color_elem2 = colores.pop(7)

color_elem = [color_elem1, color_elem2]
print("colores eliminados",color_elem)
