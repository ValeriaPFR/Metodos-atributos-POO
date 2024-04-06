# Importar variables de ingredientes desde el modulo ingredientes, siguiendo la convencion (al inicio)
from ingredientes import proteina, vegetal, masa

# Definir la clase Pizza
class Pizza():
    # Atributos de clase. Caracteristicas de tamanio y precio-ya establecido-
    tamanio = "Familiar"
    precio = 10000
    
    # Metodo estatico para validar si un elemento esta o no dentro de la lista
    @staticmethod
    def validar(texto , lista):
        return texto in lista
    
    # Metodo constructor (__init__) de la clase Pizza
    """Nota: El metodo '__init__' de la clase Pizza es el constructor que inicializa los atributos de instancia 
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
        self.ingrediente_proteico = int(input('''
            Por favor elija proteína (1-2-3):
        1. Pollo
        2. Vacuno
        3. Proteína vegetal
        >>
        '''))
        print("------")
        self.ingrediente_vegetal1 = int(input('''
            Por favor elija primer vegetal (1-2-3):
        1. Tomate
        2. Aceituna
        3. Champiñón
        >>
        '''))
        print("------")
        self.ingrediente_vegetal2 = int(input('''
            Por favor elija segundo vegetal (1-2-3):
            1. Tomate
            2. Aceituna
            3. Champiñón
            >>
            '''))
        print("------")
        
        self.tipo_masa = int(input('''
            Por favor elija grosor de masa (1-2):
            1. Tradicional
            2. Delgada/A la Piedra
            >>
            '''))
        print("------")
        
        # Validacion de ingredientes y tipo de masa
        self.es_valida = (
            self.validar(self.ingrediente_proteico, proteina)
            and self.validar(self.ingrediente_vegetal1, vegetal)
            and self.validar(self.ingrediente_vegetal2, vegetal)
            and self.validar(self.tipo_masa, masa)
        )
if __name__=="__main__":
    pizza=Pizza()
    pizza.realizar_pedido()