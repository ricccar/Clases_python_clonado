"""Orientacion a objetos, vamos a pasar esta logica a dos objetos 
Producto e Inventario, en el Inventario deberíamos poder crear y eliminar 
entradas de productos, controlar el stock (filtro para ver que productos hay por debajo de un numero) y
crear una alerta de cuando un producto se ha agotado (habrá que hacer lógica para retirar y 
añadir stock a un producto)
Crear un objeto ordenador, que sirva para crear ordenadores Windows, Linux y macos (que además serán sus propios objetos,
ya que son distintos)
 
cada uno debería tener un sistema distinto de instalación de paquetes (exe para Windows, apt para Linux, homebrew para macos)
el sistema de windows para instalar solo necesita tener un .exe y decirle que si a los permisos, el sistema Linux requiere
que tenga la misma versión que el kernel de Linux, pero no necesita aprobar permisos, y el mac tendrá una clave interna
(un numero) que debe coincidir, 
pero le da igual versión o permisos, solo que la clave interna sea la misma"""

class PC:
    def __init__(self, marca: str, modelo: str, memoria: int):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.programas = []
        
    def __str__(self):
        return f"La lista de programas instalados es: {self.programas}."


class PC_Windows(PC):
    def __init__(self, marca, modelo, memoria):
        super().__init__(marca, modelo, memoria)
        self.sistema="Windows"
    def instalador(self, nombre: str):
        permisos = input ("¿Quieres permitir instalar este programa?: S/N")
        if nombre[-3:]=="exe" and permisos.lower() == "s":
            print("El programa se puede instalar en el equipo.")
            self.programas.append(nombre)
        else:
            print("El programa no es compatible con Windows.")
        
        
                        
        
class PC_Linux(PC):
    def __init__(self, marca, modelo, memoria, kernell):
        super().__init__(marca, modelo, memoria)
        self.sistema="Linux"
        self.kernell=kernell
    def instalador(self, nombre: str):
        if nombre.split("_")[1]==self.kernell:
            print("El programa se puede instalar en el equipo.")
            self.programas.append(nombre)
        else:
            print("El programa no es compatible con Linux.")
        

class PC_Mac(PC):
    def __init__(self, marca, modelo, memoria, clave_interna):
        super().__init__(marca, modelo, memoria)
        self.sistema="MAC"       
        self.clave_interna = clave_interna
        
    def instalador(self, nombre: str, clave_int: str):
        if self.clave_interna==clave_int:
            print("El programa se puede instalar en el equipo.")
            self.programas.append(nombre)
        else:
            print("El programa no es compatible con Mac.")
        

    
Dell = PC_Windows("Dell", "Aspire", 10)
Dell.instalador("Teams.exe")
print(Dell)

Linux1 = PC_Linux("MV", "Server", 10, "4080")
Linux1.instalador("Teams_5050")
print(Linux1)
  
Mac1 = PC_Mac("MV", "Server", 10, 1500)
Mac1.instalador("Teams_5050", 1500)
print(Mac1)