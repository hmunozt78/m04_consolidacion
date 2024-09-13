from os import system, name
from time import sleep
import m04_consolidacion_clases as clase

def limpia_consola():
    sist_operativo = str(name).lower()
    if sist_operativo == "nt":
        system("cls")
    else:
        system("clear")

def continuar() -> bool:
    v_repeticion = bool(True)
    while v_repeticion:
        limpia_consola()
        v_opcion_continuar = input("Desea Continuar (s/n): ").lower()
        if v_opcion_continuar == "s":
            return True
        elif v_opcion_continuar =="n":
            return False
        else:
            print("opcion Invalida, Intente Nuevamente")
            sleep(1)

def mostrar_instanciado():
    particular_muestra = clase.Particular("Ford", "Fiesta", 4, 180, 500, 5)
    carga_muestra = clase.Carga("Daft Trucks", "G38", 10, 120, 1000, 2000)
    bicicleta_muestra = clase.Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    moto_muestra = clase.Motocicleta("Harley Davidson", "Roadster XL 1200 CX", 2, "Urbana", 18, "Diamante", "4T")

    print("*************************************************************************************")
    print("Los datos de los Vehiculos de Muestra son los siguientes:")
    print("")
    print(str(particular_muestra))
    print(str(carga_muestra))
    print(str(bicicleta_muestra))
    print(str(moto_muestra))
    print()
    print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(moto_muestra,clase.Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(moto_muestra,clase.Automovil)}")  
    print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(moto_muestra,clase.Particular)}")  
    print(f"Motocicleta es instancia con relación a Vehículo de Carga: {isinstance(moto_muestra,clase.Carga)}")  
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(moto_muestra,clase.Bicicleta)}")  
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(moto_muestra,clase.Motocicleta)}")
    print("*************************************************************************************")

def pausa_ejecucion ():
    system("pause")

def espera_un_rato(tiempo:float):
    sleep(tiempo)