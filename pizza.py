# Importar variables de ingredientes desde el modulo ingredientes, siguiendo la convencion (al inicio)
from ingredientes import proteina
from ingredientes import vegetal
from ingredientes import masa

# Definir la clase Pizza
class Pizza():
    # Atributos de clase. Caracteristicas de tamanio y precio-ya establecido-
    tamano = "Familiar"
    precio = 10000
    
    # Metodo estatico para validar si un elemento esta o no dentro de la lista
    @staticmethod
    def validar(texto , lista):
        return texto in lista
    
    # Metodo constructor (__init__) de la clase Pizza
    """Nota: El método '__init__' de la clase Pizza es el constructor que inicializa los atributos de instancia 
    representando los ingredientes y tipo de masa. 
    Ademas, establece un atributo 'es_valida' en False para verificar la validez de la pizza."""
    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False
    
    # Metodo para realizar un pedido de pizza en la funcion 'realizar_pedido' que recibe los parámetros de 'self'
    def realizar_pedido(self):
        # Solicitar al usuario ingresar los ingredientes y el tipo de masa
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico (pollo, vacuno, carne): \n").lower()
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal (tomate, aceituna, champinon): \n").lower()
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal (tomate, aceituna, champinon): \n").lower()
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional, delgada): \n").lower()

        # Validacion de ingredientes y tipo de masa
        self.es_valida = (
            self.validar(self.ingrediente_proteico, proteina)
            and self.validar(self.ingrediente_vegetal1, vegetal)
            and self.validar(self.ingrediente_vegetal2, vegetal)
            and self.validar(self.tipo_masa, masa)
        )