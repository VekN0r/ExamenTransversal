from funcionesPrueba import *
while True:
    print("="*30)
    print("1. Cargar Sueldos")
    print("2. Ver Lista de Trabajadores")
    print("3. Ver Estadisticas")
    print("4. Reporte de Sueldos")
    print("5. Salir")
    print("="*30)
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ponerSueldoAleatorio(nuevaListaSueldo)
        elif opcion == 2:
            verListaTrabajadoresSueldo(nuevaListaSueldo)
        elif opcion == 3:
            verEstadisticas(nuevaListaSueldo)
        elif opcion == 4:
            reporteSueldos(nuevaListaSueldo)
        elif opcion == 5:
            print("Saliendo del programa")
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("Salida con exito, hasta pronto")
            break
        else:
            print("Opción incorrecta, ingrese una dentro del rango.")
    except ValueError:
        print("La opción ingresada no es un número.")        
        
            