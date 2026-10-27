"""
Nuevo ejercicio:
Crear una funcion que reciba un diccionario de productos, que tienen precio, unidades disponibles y unidades vendidas
Calcular el valor total de todos los productos (multiplicado por unidades!), identifica los productos agotados, y filtra aquellos que valgan menos de un precio que tu le des
"""
productos = {
    "alicates": {
        "precio": 12.5,
        "stock": 40,
        "unidades_vendidas": 12, 
    },
    "martillos": {
            "precio": 7.5,
            "stock": 32,
            "unidades_vendidas": 7, 
        },
    "llaves_inglesas": {
            "precio": 17,
            "stock": 55,
            "unidades_vendidas": 34, 
        }
}

def total_coste_stock (diccionario):
    coste_total = 0
    for key, item in diccionario.items():
        coste_total += item["precio"]*item["stock"]
    return(coste_total)

def 
    
print(total_coste_stock(productos))    
    