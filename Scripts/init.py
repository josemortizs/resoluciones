from gestorresoluciones import GestorResoluciones
from resolucion import Resolucion


gestor = GestorResoluciones()
gestor.imprimeListadoResoluciones()

resolucion = Resolucion(128,102,"qa1","qa1")
gestor.agregaResolucion(resolucion)

print("Resoluciones ahora: ")
gestor.imprimeListadoResoluciones()