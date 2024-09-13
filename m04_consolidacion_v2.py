import funciones_para_v2 as funciones
import funciones_genericas as fun_gen

def seleccionar_tipo():
    v_continuar_tipo = bool(True)

    while v_continuar_tipo:
        try:
            v_tipo_vehiculo = int()
            fun_gen.limpia_consola()
            print('''
            Selecciona el Tipo de Vehiculo a ingresar:
            
            1. Vehiculo Particular
            2. Vehiculo Carga
            3. Motocicleta
        ''')
            
            v_tipo_vehiculo = int(input("ingresa tu opcion: "))

            if v_tipo_vehiculo not in [1,2,3]:
                print("Opcion Invalida, Intente Nuevamente")
                fun_gen.espera_un_rato(1)
                continue

            funciones.capturar_vehiculos(v_tipo_vehiculo)
            v_continuar_tipo = fun_gen.continuar()
            
        except ValueError as e:
            print(f"Error de Ingreso - {e}")
            fun_gen.espera_un_rato(1)

        except Exception as e:
            print(f"Otro tipo de Error - {e}")
            fun_gen.espera_un_rato(1)

def menu_ingreso():
    fun_gen.limpia_consola()
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
        fun_gen.espera_un_rato(1)
    
def menu_principal():

    v_continuar_menu_principal = bool(True)
    while v_continuar_menu_principal:

        try:
            fun_gen.limpia_consola()
            print(''' 
            Seleccione que accion desea realizar:
            
            1. Ingresar Vehiculo
            2. Revisar Listado de Vehiculos
            3. Salir
            
        ''')
            v_opcion_principal = int(input("Ingrese opcion: "))

            if v_opcion_principal == 1:
                seleccionar_tipo()

            elif v_opcion_principal == 2:
                funciones.mostrar_Vehiculos()

            elif v_opcion_principal ==3:
                fun_gen.limpia_consola()
                print("HASTA LUEGO")
                fun_gen.espera_un_rato(2)
                break
            else:
                fun_gen.limpia_consola()
                print("Opcion Invalida, Intente de nuevo")
                fun_gen.espera_un_rato(2)
    

        except ValueError as e:
            print(f"Error de ingreso - {e}")
            fun_gen.espera_un_rato(1)

        except Exception as e:
            print(f"Error No Reconocido - {e}")
            fun_gen.espera_un_rato(1)

def main():
    fun_gen.limpia_consola()
    menu_principal()    

main()