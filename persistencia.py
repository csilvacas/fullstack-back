""" Función guardar pedido """
def guardar_pedido(nombre, apellidos):
    """ Escribir datos en fichero pedidos.txt"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()
