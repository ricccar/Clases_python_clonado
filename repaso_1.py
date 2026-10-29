"""
Crear una función que va a recibir una lista de gastos, donde cada gasto tiene una categoria, un importe y una descripcion
 
La función debe:
 
    Calcular el gasto total
    Identificar la categoría con mas gasto
    Mostrar los gastos superiores a una cantidad
 
la función debe ser un poco inteligente (por ejemplo categorías no distinguen entre mayus y minus, o espacios, etc...)
para el resto de compañeros, podeis hacer el ejercicio, pero os planteo un reto, en vez de darme el ejercicio hecho por chat,
dadme el enlace a github donde tenéis el código subido (en github)
"""

gastos = [{"categoria": "comida", "importe": 12.5, "descripcion": "comida del dia"},
          {"categoria": "transporte", "importe": 20.0, "descripcion": "gasolina"},
          {"categoria": "ocio", "importe": 15.0, "descripcion": "cine"},
          {"categoria": "comida", "importe": 8.0, "descripcion": "almuerzo"}]

def gestor_gastos(lista_gastos, cantidad):
    gasto_total = 0
    categoria_gasto = {}
    gastos_superiores = []
    
    for gasto in lista_gastos:
        gasto_total += gasto["importe"]
        categoria = gasto["categoria"].strip().lower()
        
        if categoria in categoria_gasto:
            categoria_gasto[categoria] += gasto["importe"]
        else:
            categoria_gasto[categoria] = gasto["importe"]
        
        if gasto["importe"] > cantidad:
            gastos_superiores.append(gasto)
    
    categoria_maxima = max(categoria_gasto, key=categoria_gasto.get)
    
    return gasto_total, categoria_maxima, gastos_superiores

print(gestor_gastos(gastos, 14))
