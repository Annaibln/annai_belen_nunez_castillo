def sistema_gestion_equipos():
    capacidad_maxima = 20
    equipos_disponibles = 20
    historial_usos = 0

    print("Bienvenida ¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!\n")

    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. 1.- Equipos disponibles.")
        print("2. 2.- Asignar equipo.")
        print("3. 3.- Liberar equipo.")
        print("4. 4.- Historial de usos.")
        print("5. 5.- Salir.")
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            print(f"\nEquipos disponibles: {equipos_disponibles}")
            print("-" * 45)

        elif opcion == "2":
            while True:
                try:
                    cant = int(input("\nIngrese la cantidad de equipos a asignar: "))
                    if cant <= 0:
                        print(" La cantidad no puede ser menor o igual a 0.")
                    elif cant > equipos_disponibles:
                        print(f" No puede superar la cantidad de equipos disponibles ({equipos_disponibles}).")
                    else:
                        equipos_disponibles -= cant
                        historial_usos += cant
                        print(f" Asignación exitosa. Quedan {equipos_disponibles} equipos disponibles.")
                        break
                except:
                    print(" Error: Ingrese un número entero válido.")
            print("-" * 45)

        elif opcion == "3":
            while True:
                try:
                    cant = int(input("\nIngrese la cantidad de equipos a liberar: "))
                    if cant <= 0:
                        print(" La cantidad a liberar debe ser mayor a 0.")
                    elif equipos_disponibles + cant > capacidad_maxima:
                        print(f" No puede superar la capacidad máxima del laboratorio ({capacidad_maxima} equipos).")
                    else:
                        equipos_disponibles += cant
                        historial_usos = max(0, historial_usos - cant)
                        print(f"-> Liberación exitosa. Equipos disponibles: {equipos_disponibles}.")
                        break
                except:
                    print(" Error: Ingrese un número entero válido.")
            print("-" * 45)

        elif opcion == "4":
            print(f"\n-> Historial de usos: Total de equipos asignados durante la sesión: {historial_usos}")
            print("-" * 45)

        elif opcion == "5":
            print('\n"Gracias por utilizar nuestro software, hasta la próxima."')
            break

        else:
            print("\n Opción inválida. Seleccione nuevamente una opción del 1 al 5.")
            print("-" * 45)

if __name__ == "__main__":
    sistema_gestion_equipos()
