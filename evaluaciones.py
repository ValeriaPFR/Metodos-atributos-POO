# Importar la clase Pizza desde el modulo pizza.py
from pizza import Pizza
import ingredientes 

""" 
a. Valores de atributos de clase
"""
# Obtener los valores de atributos de clase
tamanio, precio = Pizza.tamanio, Pizza.precio
print(f"El tamaño de la pizza es: {tamanio} y su precio es: ${precio}")

""" 
b. Uso del método Pizza.validar()
"""
# Validar un ingrediente usando el metodo Pizza.validar()
texto = 'Salsa de tomate'
lista = ['Salsa de tomate', 'Salsa BBQ']
test = Pizza.validar(texto, lista)
if test:
    print(f"El ingrediente, {texto}, está dentro de las opciones de ingredientes")
else:
    print("Lo sentimos, ingrediente no disponible")

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
Proteína:
{ingredientes.proteicos[pedido.ingrediente_proteico-1]}
Vegetales: 
{ingredientes.vegetales[pedido.ingrediente_vegetal1-1]},
{ingredientes.vegetales[pedido.ingrediente_vegetal2-1]}
Tipo de masa: 
{ingredientes.masas[pedido.tipo_masa-1]}
''')

""" 
e. Verificar si el pedido de pizza es valido
"""
if pedido.es_valida:
    print("Su pedido es válido. QUE DISFRUTE SU PIZZA :)")
else:
    print("Su pedido no es válido :( \n. Intente con otra combinación de ingredientes")
