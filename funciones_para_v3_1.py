import funciones_genericas as funcion
import csv
import m04_consolidacion_clases as clase

v_vehiculos = []


def mostrar_Vehiculos(opcion_seleccionada:int):
    '''
    Descripcion:
    Recibe un entero, que corresponmde a la opcion seleccionada en el menu de mostrar vehiculos.
    Esto hace 3 pasos: 

    1.  Mostrar Vehiculos ingresados en esta sesion
    2.  Invocar la funcion Mostrar_Instanciado, del modulo funciones_genericas, 
        para mostrar requerimiento del PDF
    3.  Invocar funcion leer_archivo, ubicada en este mismo archivo, para que abra el archivo y muestre
        la informacion guardada en el mismo

    Parametros:
        opcion_seleccionada = Entero

    Return:
        None
    '''

    funcion.limpia_consola()
    if (len(v_vehiculos)) >0 :
        for i in range (len(v_vehiculos)):
            print(f"Datos del Vehiculo {i+1}: {str(v_vehiculos[i])}")
    else:
        print("NO SE HAN INGRESADO VEHICULOS MANUALMENTE")

    funcion.mostrar_instanciado()
    funcion.pausa_ejecucion()

    leer_archivo(opcion_seleccionada)
        
    funcion.pausa_ejecucion()

def leer_archivo(opcion:int):
    vehiculos = []
    print()
    print("Vehiculos en archivo - Sin Alteraciones")
    with open ("vehiculos2.csv", "r") as archivo_vehiculos:
        data = csv.reader(archivo_vehiculos)
        if(opcion == 1):
            tipo_vehiculo = "<class '__main__.Particular'>" 
        elif(opcion == 2):
            tipo_vehiculo = "<class '__main__.Carga'>"
        elif(opcion == 3):
            tipo_vehiculo = "<class '__main__.Bicicleta'>"
        elif(opcion == 4):
            tipo_vehiculo = "<class '__main__.Motocicleta'>"

        if opcion in [1,2,3,4]:

            for fila in data:
                if fila[0] == tipo_vehiculo:
                    print(f"{nombres_vehiculos(tipo_vehiculo)} - {fila[1]}")
        else:
            for fila in data:
                tipo = nombres_vehiculos(fila[0])
                print(f"{tipo} - {fila[1]}")
            
    print("********************************************************************")

def nombres_vehiculos(tipo:str) -> str:
    '''
    Descripcion:
    Esta funcion recibe un String, para comparar y devolver el nombre que mostrara en pantalla,
    para hacer más facil la identificacion del mismo:

    Parametro: tipo(String)

    Return: String
    '''
    if tipo == "<class '__main__.Particular'>" :
        t_veh = "Vehiculo Particular"
    elif tipo == "<class '__main__.Carga'>" :
        t_veh = "Vehiculo de Carga"
    elif tipo == "<class '__main__.Bicicleta'>" :
        t_veh = "Vehiculo Bicicleta"
    elif tipo == "<class '__main__.Motocicleta'>" :
        t_veh = "Vehiculo Motocicleta"
    return t_veh

def grabar_archivo(vehiculo):
    '''
    Descripcion:
    Esta funcion graba los datos del obtejo recibido en un archivo .CSV
    Los datos quedan grabados, como Descriptor de Objeto y un Diccionario con los
    datos del Objeto

    Parametros:
    vehiculo: objeto del cual tomara la informacion

    Return: None

    '''
    with open("vehiculos2.csv", "a", newline= "\n") as vehiculos_nuevos:
                write = csv.writer(vehiculos_nuevos, delimiter = ',')
                diccionario = vehiculo.__dict__
                datos = [vehiculo.__class__, diccionario]
                write.writerow(datos)

def capturar_vehiculos(tipo:int):

    '''
    Esta funcion, recibe una variable de tipo entero entre 1 y 4, para definir 
    cual menu de ingreso de informacion se va a desplegar

    Parametro: 
    tipo(int): Valor entre 1 y 4 que define el tipo de vehiculo

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
                    grabar_archivo(vehiculo_paso)
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
                    grabar_archivo(vehiculo_paso)
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
                    grabar_archivo(vehiculo_paso)
                    prueba_continuidad(False)

            elif tipo == 4:
                for i in range(cant_autos):
                    funcion.limpia_consola()
                    print(f"\nIngrese los datos de la Bicicleta {i+1}\n")
                    marca = str(input("Ingrese Marca: "))
                    modelo = str(input("Ingrese Modelo: "))
                    ruedas = int(input("Ingrese Cantidad de Ruedas: "))
                    tipo = input("Ingrese el tipo de Bicicleta (Urbana o Deportiva): ")
                    vehiculo_paso = clase.Bicicleta(marca, modelo, ruedas, tipo)
                    v_vehiculos.append(vehiculo_paso)
                    grabar_archivo(vehiculo_paso)
                    prueba_continuidad(False)

        except ValueError as e:
            print(f"Error de Ingreso, Intente Nuevamente - {e}")
            funcion.espera_un_rato(1)
            prueba_continuidad = True

        except Exception as e:
            print(f"Error General - {e}")
            funcion.espera_un_rato(1)
            prueba_continuidad = True