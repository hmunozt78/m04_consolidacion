from time import sleep
from funciones_genericas import limpia_consola, continuar
import funciones_para_v3_1 as funcion

v_vehiculos = []

def seleccionar_tipo(origen:str):
    v_continuar_tipo = bool(True)
    while v_continuar_tipo:
        try:
            
            v_tipo_vehiculo = int()
            limpia_consola()
            if origen == "ingreso":
                print('''
                Selecciona el Tipo de Vehiculo a ingresar:
                
                1. Vehiculo Particular
                2. Vehiculo Carga
                3. Motocicleta
                4. Bicicleta
            ''')
            elif origen == "listar":
                print('''
                Selecciona el Tipo de Vehiculo a Visualizar:
                
                1. Vehiculo Particular
                2. Vehiculo Carga
                3. Bicicleta
                4. Motocicleta
                5. Todos
            ''')
            
            v_tipo_vehiculo = int(input("ingresa tu opcion: "))

            if v_tipo_vehiculo in [1,2,3,4] and origen == "ingreso":
                funcion.capturar_vehiculos(v_tipo_vehiculo)
                break
            
            if (v_tipo_vehiculo in [1,2,3,4,5]) and (origen == "listar"):
                funcion.mostrar_Vehiculos(v_tipo_vehiculo)
                break

            v_continuar_tipo = continuar()
            
        except ValueError as e:
            print(f"Error de Ingreso - {e}")
            sleep(1)

        except Exception as e:
            print(f"Otro tipo de Error - {e}")
            sleep(1)

def menu_seleccion_visual():
    limpia_consola()
    try:
        print('''
        Bienvenido al Sistema de ingreso de Vehiculos
        
        Seleccione el tipo de Vehiculo que desea ingresar:
        
        1. Particular
        2. Carga
        3. Motocicletas

    ''')
    
        v_opcion_menu = int(input("Indique la opcion que desea: "))

    except ValueError as e:
        print(f"Error de Ingreso - {e}")
        sleep(1)

def menu_principal():

    v_continuar_menu_principal = bool(True)
    while v_continuar_menu_principal:

        try:
            limpia_consola()
            print(''' 
            Seleccione que accion desea realizar:
            
            1. Ingresar Vehiculo
            2. Revisar Listado de Vehiculos
            3. Salir
            
        ''')
            v_opcion_principal = int(input("Ingrese opcion: "))

            if v_opcion_principal == 1:
                seleccionar_tipo("ingreso")

            elif v_opcion_principal == 2:
                seleccionar_tipo("listar")

            elif v_opcion_principal ==3:
                limpia_consola()
                print("HASTA LUEGO")
                sleep(2)
                break
            else:
                limpia_consola()
                print("Opcion Invalida, Intente de nuevo")
                sleep(2)
    

        except ValueError as e:
            print(f"Error de ingreso - {e}")
            sleep(1)

        except Exception as e:
            print(f"Error No Reconocido - {e}")
            sleep(1)

def main():
    limpia_consola()
    menu_principal()    

main()