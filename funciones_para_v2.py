import funciones_genericas as funcion
import m04_consolidacion_clases as clase

v_vehiculos = []

def mostrar_Vehiculos():
    '''
    Descripcion:

    Esta funcion no recibe ningun parametro, ni retorna nada, se encarga de
    mostrar 2 elementos los cuales son:

    1. Lista de Vehiculos ingresados en esta sesion
    2. Pruebas de Instancias con elementos definidos segun PDF de requerimientos
    
    '''
    funcion.limpia_consola()
    if (len(v_vehiculos)) >0 :
        for i in range (len(v_vehiculos)):
            print(f"Datos del Vehiculo {i+1}: {str(v_vehiculos[i])}")
            funcion.espera_un_rato(0.5)
    else:
        print("NO SE HAN INGRESADO VEHICULOS MANUALMENTE")

    funcion.mostrar_instanciado()
        
    funcion.pausa_ejecucion()

def capturar_vehiculos(tipo:int) -> None:
    '''
    Esta funcion, recibe una variable de tipo entero entre 1 y 3, para definir 
    cual menu de ingreso de informacion se va a desplegar

    Parametro: 
    tipo(int): Valor entre 1 y 3 que define el tipo de vehiculo

    Return: None
    '''
    prueba_continuidad = True

    while prueba_continuidad:
        try:
            funcion.limpia_consola()
            cant_autos = int(0)
            cant_autos = int(input("Cuantos Vehiculos desea ingresar?: "))
            if (cant_autos <= 0):
                print(f"Ingreso una cantidad invalida {cant_autos}, intente nuevamente")
                funcion.espera_un_rato(1)
                continue
                

            if tipo == 1:

                for i in range(cant_autos):
                    funcion.limpia_consola()
                    print(f"\nIngrese los datos del Vehiculo Particular {i+1}\n")
                    marca = str(input("Ingrese Marca: "))
                    modelo = str(input("Ingrese Modelo: "))
                    ruedas = int(input("Ingrese Cantidad de Ruedas: "))
                    velocidad = int(input("Ingrese Velocidad Maxima: "))
                    cilindrada = int(input("Ingrese Cilindrada: "))
                    pasajeros = int(input("Ingrese Cantidad e Pasajeros: "))
                    vehiculo_paso = clase.Particular(marca, modelo, ruedas, velocidad, cilindrada, pasajeros)
                    v_vehiculos.append(vehiculo_paso)
                    prueba_continuidad(False)

            elif tipo == 2:
                for i in range(cant_autos):
                    funcion.limpia_consola()
                    print(f"\nIngrese los datos del Vehiculo de Carga {i+1}\n")
                    marca = str(input("Ingrese Marca: "))
                    modelo = str(input("Ingrese Modelo: "))
                    ruedas = int(input("Ingrese Cantidad de Ruedas: "))
                    velocidad = int(input("Ingrese Velocidad Maxima: "))
                    cilindrada = int(input("Ingrese Cilindrada: "))
                    tara = int(input("Ingrese Capacidad de Carga: "))
                    vehiculo_paso = clase.Carga(marca, modelo, ruedas, velocidad, cilindrada, tara)
                    v_vehiculos.append(vehiculo_paso)
                    prueba_continuidad(False)
            
            elif tipo == 3:
                for i in range(cant_autos):
                    funcion.limpia_consola()
                    print(f"\nIngrese los datos de la Motocicleta {i+1}\n")
                    marca = str(input("Ingrese Marca: "))
                    modelo = str(input("Ingrese Modelo: "))
                    ruedas = int(input("Ingrese Cantidad de Ruedas: "))
                    tipo = input("Ingrese el tipo de Motocicleta (Urbana o Deportiva): ")
                    radios = int(input("Ingrese el numero de radios: "))
                    cuadro = input("Ingrese Tipo de cuadro: ")
                    motor = input("Ingrese Tipo de Motor (2T / 4T): ")
                    vehiculo_paso = clase.Motocicleta(marca, modelo, ruedas, tipo, radios, cuadro, motor)
                    v_vehiculos.append(vehiculo_paso)
                    prueba_continuidad(False)
        
        except ValueError as e:
            print(f"Error de Ingreso, Intente Nuevamente - {e}")
            funcion.espera_un_rato(1)
            prueba_continuidad = True

        except Exception as e:
            print(f"Error General - {e}")
            funcion.espera_un_rato(1)
            prueba_continuidad = True