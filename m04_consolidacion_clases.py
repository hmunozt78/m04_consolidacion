class Vehiculo():
    def __init__(self, marca:str, modelo: str, nro_ruedas: int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas
    
class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, velocidad: int, cilindrada: int) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro de Ruedas: {self.nro_ruedas}, Velocidad Max.: {self.velocidad}, Cilindrada: {self.cilindrada}"

class Particular(Automovil):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, velocidad: int, cilindrada: int, pasajeros:int) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.pasajeros = pasajeros

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro de Ruedas: {self.nro_ruedas}, Velocidad Max.: {self.velocidad}, Cilindrada: {self.cilindrada}, Cantidad de Psajeros: {self.pasajeros}"

class Carga(Automovil):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, velocidad: int, cilindrada: int, tara:int) -> None:
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.tara = tara

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro de Ruedas: {self.nro_ruedas}, Velocidad Max.: {self.velocidad}, Cilindrada: {self.cilindrada}, Capacidad Carga: {self.tara}"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, tipo:str) -> None:
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo
        
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro de Ruedas: {self.nro_ruedas}, Tipo de Ciclo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca: str, modelo: str, nro_ruedas: int, tipo: str, nro_radios:int, cuadro: str, motor: str) -> None:
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Nro de Ruedas: {self.nro_ruedas}, Tipo de Ciclo: {self.tipo}, Nro de Radios: {self.nro_radios}, Tipo de Cuadro: {self.cuadro}, Tipo de Motor: {self.motor}"
