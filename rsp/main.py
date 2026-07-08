MAIN PRACTICA_SP2
from practica_sp2 import*

def menu():
    """Imprime el menú de opciones en consola."""
    print("\n=== MENÚ DE OPCIONES ===")
    print("2 - Cargar datos de estudiantes (Máx 3)")
    print("3 - Mostrar todos los estudiantes")
    print("4 - Calcular promedios")
    print("5 - Mostrar ordenados por promedio (DESC)")
    print("6 - Mostrar estudiante(s) con mayor promedio")
    print("7 - Buscar estudiante por legajo")
    print("0 - Salir")

def main():
    lista_estudiantes = []
    MAX_ALUMNOS = 3
    promedios_calculados = False # Control de flujo para saber si ya se pasó por el ítem 4

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Saliendo del programa...")
            break

        # Nota 0: Validación de datos cargados previamente
        if opcion in ["3", "4", "5", "6", "7"] and len(lista_estudiantes) == 0:
            print("\n[!] Error: No se puede acceder a esta opción sin antes haber cargado los datos (Opción 2).")
            continue

        # Ítem 2: Carga de datos
        if opcion == "2":
            if len(lista_estudiantes) >= MAX_ALUMNOS:
                print(f"\n[!] Ya se alcanzó el límite máximo de {MAX_ALUMNOS} estudiantes.")
                continue
            
            print(f"\n--- Carga del Estudiante {len(lista_estudiantes) + 1} de {MAX_ALUMNOS} ---")
            legajo = validar_legajo("Ingrese el legajo (entero): ") #mensaje
            nombre = validar_nombre_apellido("Ingrese Apellido y Nombre: ")
            genero = validar_genero("Ingrese género (F / M / X): ")
            parcial1 = validar_nota("Ingrese nota del 1° Parcial (1-10): ")
            parcial2 = validar_nota("Ingrese nota del 2° Parcial (1-10): ")

            # Creamos el diccionario del estudiante
            estudiante = {
                "legajo": legajo,
                "nombre": nombre,
                "genero": genero,
                "parcial1": parcial1,
                "parcial2": parcial2
            }
            lista_estudiantes.append(estudiante)
            print("Estudiante cargado con éxito.")

        # Ítem 3: Mostrar todos los datos cargados originariamente
        elif opcion == "3":
            print("\n=== LISTA DE ESTUDIANTES REGISTRADOS ===")
            recorrer_y_mostrar_estudiantes(lista_estudiantes, mostrar_promedio=promedios_calculados)

        # Ítem 4: Calcular promedio
        elif opcion == "4":
            calcular_promedios(lista_estudiantes)
            promedios_calculados = True
            print("\nPromedios calculados y guardados con éxito.")

        # Ítem 5: Mostrar ordenados por promedio DESC
        elif opcion == "5":
            if not promedios_calculados:
                print("\n[!] Advertencia: Primero debe calcular los promedios (Opción 4) para ordenar correctamente.")
                continue
            print("\n=== ESTUDIANTES ORDENADOS POR PROMEDIO (DESC) ===")
            lista_ordenada = ordenar_por_promedio_desc(lista_estudiantes)
            recorrer_y_mostrar_estudiantes(lista_ordenada, mostrar_promedio=True)

        # Ítem 6: Mostrar mayor promedio
        elif opcion == "6":
            if not promedios_calculados:
                print("\n[!] Advertencia: Primero debe calcular los promedios (Opción 4).")
                continue
            print("\n=== ESTUDIANTE(S) CON MAYOR PROMEDIO ===")
            mejores = buscar_mayor_promedio(lista_estudiantes)
            recorrer_y_mostrar_estudiantes(mejores, mostrar_promedio=True)

        # Ítem 7: Buscar por legajo
        elif opcion == "7":
            legajo_búsqueda = validar_legajo("Ingrese el legajo del estudiante a buscar: ")
            resultado = buscar_por_legajo(lista_estudiantes, legajo_búsqueda)
            
            if resultado:
                print("\n=== ESTUDIANTE ENCONTRADO ===")
                recorrer_y_mostrar_estudiantes(resultado, mostrar_promedio=promedios_calculados)
            else:
                print(f"\nNo se encontró ningún estudiante con el legajo {legajo_búsqueda}.")

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
