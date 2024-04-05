# Importar la clase Pizza desde el modulo pizza.py
from pizza import Pizza

""" 
a. Valores de atributos de clase
"""
# Obtener los valores de atributos de clase
tamaño, precio = Pizza.tamaño, Pizza.precio
print(f"El tamaño de la pizza es: {tamaño} y su precio es: ${precio}")

""" 
b. Uso del método Pizza.validar()
"""
# Validar un ingrediente usando el metodo Pizza.validar()
texto = 'Salsa de tomate'
lista = ['Salsa de tomate', 'Salsa Bbq']
test = Pizza.validar(texto, lista)
if test:
    print(f"El ingrediente, {texto}, está dentro de la lista de ingredientes")
else:
    print("Ingrediente no válido")

""" 
c. Solicitar ingredientes y tipo de masa al usuario
"""
# Instanciar la clase Pizza
pedido = Pizza()
# Solicitar al usuario ingresar/escribir su eleccion de ingredientes y tipo de masa
pedido.realizar_pedido()

"""
d. Imprimir la selección del usuario
"""
print(f'''
Su pedido es el siguiente:
Proteína: {pedido.ingrediente_proteico}
Vegetales: {pedido.ingrediente_vegetal1}, {pedido.ingrediente_vegetal2}
Tipo de masa: {pedido.tipo_masa}
''')

""" 
e. Verificar si el pedido de pizza es valido
"""
if pedido.es_valida:
    print("Su pedido es válido")
else:
    print("Su pedido no es válido")
