class Resolucion():
    
    """ **************************************************************** 
    Clase creada para la representación de una resolución de pantalla.

    Contiene las variables ancho y alto (propias de cada pantalla), así 
    como el tipo de pantalla (móvil, pc, tablet...) y un nombre 
    que puede usarse como identificador de cada resolución.
    *************************************************************** """ 

    # Constructor
    def __init__(self, ancho = 320, alto = 568, tipo = 'No especificado', nombre = 'No especificado'):
        self.ancho = ancho
        self.alto = alto
        self.tipo = tipo
        self.nombre = nombre
    

    # Getter
    @property
    def ancho(self):
        return self._ancho
    
    @property
    def alto(self):
        return self._alto
    

    # Setter
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho if (ancho >= 320) else 320
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto if (alto >= 568) else 568
    
    # Sobreescribimos el método __str__
    def __str__(self):
        return "Nombre: {0} - Tipo: {1} - Resolución: {2} x {3}".format(self.nombre, self.tipo, self.ancho, self.alto)
    
    # Sobreescribimos el método __eq__ para poder comparar, correctamente, si dos objetos de la clase Resolucion son iguales
    def __eq__(self, otraResolucion):
        return ((self.ancho == otraResolucion.ancho) and (self.alto == otraResolucion.alto))
    
# ---------------------------------------------------------------------------------------------------------------------------