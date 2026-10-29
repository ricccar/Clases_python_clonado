"""
Segunda parte:
 
Ahora vamos a utilizar orientación a objetos, la lista de gastos debería transformarse en un objeto Gasto,
y deberíamos tener una nueva clase GestorGastos que sustituya nuestra funcion, no solo deberíamos tener info_gasto 
(la funcion que tenemos ahora), sino también deberíamos de poder crear nuevos gastos, eliminarlos, filtrarlos por 
categoría, ...
"""

class Gasto():
    def __init__(self, categoria: str, cantidad: float, descripcion: str):
        self.categoria = categoria
        self.cantidad  = cantidad
        self.descripcion = descripcion

    def imprimir(self):
        print(f"El gasto de la categoría {self.categoria} y con descripción {self.descripcion}, fue de: {self.cantidad}€")


gasto1 = Gasto("Compras", 314.90, "Compra de TV")
gasto1.imprimir()


class GestorGastos():
    def __init__(self, lista_gastos: list=None):
        if lista_gastos is None:
            self.lista_gastos = []
            #historial_gestos = lista_historica
        else:
            self.lista_gastos = lista_gastos
            #historial_gestos = lista_historica
                    
    def agregar_gasto(self, gasto):
        for g in self.lista_gastos:
            if gasto["categoria"] == g["categoria"]:
                self.lista_gastos["cantidad"] += gasto["cantidad"]
            else:
                self.append(gasto)

    def imprimir(self):
        for g in self.lista_gastos:
            print(g)


ricardo = GestorGastos()
ricardo.agregar_gasto("Compras", 314.90,"Compra de TV")
ricardo.agregar_gasto("Compras", 314.90, "Compra de TV")
ricardo.imprimir()
print(type(ricardo))
