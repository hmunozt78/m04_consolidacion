import funciones_genericas as fun_gen
import m04_consolidacion_clases as clase

autos = []

def mostrar_Vehiculos():
    for i in range (len(autos)):
        print(f"Datos del Auto {i+1}: {str(autos[i])}")   

def capturar_autos():
    prueba_continuidad = True

    while prueba_continuidad:
        try:
            cant_autos = int()
            cant_autos = int(input("Cuantos Vehiculos desea ingresar?: "))

            for i in range(cant_autos):
                auto_paso = []
                print(f"\nIngrese los datos del Auto {i+1}\n")
                marca = str(input("Ingrese Marca: "))
                modelo = str(input("Ingrese Modelo: "))
                ruedas = int(input("Ingrese Cantidad de Ruedas: "))
                velocidad = int(input("Ingrese Velocidad Maxima: "))
                cilindrada = int(input("Ingrese Cilindrada: "))
                auto_paso = clase.Automovil(marca, modelo, ruedas, velocidad, cilindrada)
                autos.append(auto_paso)
                prueba_continuidad = False
    
        except ValueError as e:
            print(f"Error de Ingreso, Intente Nuevamente - {e}")
            fun_gen.espera_un_rato(1)
            prueba_continuidad = True

        except Exception as e:
            print(f"Error General - {e}")
            fun_gen.espera_un_rato(1)
            prueba_continuidad = True


def main():
    fun_gen.limpia_consola()
    capturar_autos()
    fun_gen.limpia_consola()
    mostrar_Vehiculos()
    fun_gen.pausa_ejecucion()

main()