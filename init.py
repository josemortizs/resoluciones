from Models.gestorresoluciones import GestorResoluciones
from Models.resolucion import Resolucion


gestor = GestorResoluciones()
gestor.imprimeListadoResoluciones()

resolucion = Resolucion(1280,1024,"PC","SXGA")
gestor.agregaResolucion(resolucion)

print("Resoluciones ahora: ")
gestor.imprimeListadoResoluciones()