def registro_cientificos():
    print("¡Bienvenido al sistema de registro de científicos del Instituto de Investigación Avanzada.! ")

    while True:
        try:
            cant_input = input("¿Cuantos cientificos desea registrar?")
            cant_cientificos = int(cant_input)
            if cant_cientificos > 0:
                break 
            else:
                print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
        except:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

    investigadores_principales = 0
    investigadores_asistentes = 0

    for i in range(1, cant_cientificos + 1):
        print(print(f"\n--- Registro Científico #{i} ---"))

        while True:
            id_cientifico = input("Ingrese el ID del científico: ").strip()
            if len(id_cientifico) >= 12 and " " not in id_cientifico:
                break
            else:
                print("¡Error de registro! El ID debe tener al menos 12 caracteres y no contener espacios.")

        while True:
            try:
                pub_input = input("Ingrese número de publicaciones: ")
                publicaciones = int(pub_input)
                if publicaciones >= 0:
                    break
                else:
                    print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
            except:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")

        if publicaciones > 12:
            tipo = "Investigador Principal"
            investigadores_principales += 1
        else:
            tipo = "Investigador Asistente"
            investigadores_asistentes += 1
            
        print(f" Registrado exitosamente como: {tipo}")

    print(f"\n¡El instituto cuenta con {investigadores_principales} Investigadores Principales y {investigadores_asistentes} Investigadores Asistentes! ¡Ciencia en marcha!")

if __name__ == "__main__":
    registro_cientificos()

