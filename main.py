import funciones_genericas as fun_gen

continua = True
while continua:
    try:
        opcion = int(0)
        fun_gen.limpia_consola()

        print("Bienvenido al Drill del Modulo 04")
        print("Nombre Alumno: Hugo Muñoz T.")
        print('''
            Seleccione cual parte desea ejecutar:
            
            1. Parte 1
            2. Parte 2
            3. Parte 3
            4. Salir
        ''')
        opcion = int(input("Ingrese la opcion: "))

        if opcion == 1:
            from m04_consolidacion_v1 import main
        elif opcion ==2:
            from m04_consolidacion_v2 import main
        elif opcion == 3:
            from m04_consolidacion_v3_1 import main
        elif opcion == 4:
            break
        else:
            print("Opcion Invalida, Intente Nuevamente")
            fun_gen.espera_un_rato(1)

    except ValueError as e:
        print(f"Error de Ingreso, Intente Nuevamente - {e}")
        fun_gen.espera_un_rato(1)

