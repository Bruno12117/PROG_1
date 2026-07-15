from funciones2 import * 

lista_estudiantes =  [
        {"legajo": 1, "ape_nom": "Lopez Pedro", "genero": "M", "pp": 6, "sp": 7, "prom": 0.0},
        {"legajo": 2, "ape_nom": "Perez Alba", "genero": "F", "pp": 9, "sp": 6, "prom": 0.0},
        {"legajo": 3, "ape_nom": "Gil Ariel", "genero": "X", "pp": 7, "sp": 6, "prom": 0.0}
    ]

for i in range(7):
        lista_estudiantes.append({
            "legajo": 0, "ape_nom": "", "genero": "", "pp": 0, "sp": 0, "prom": 0.0
        })

promedios_calculados = False
ejecutar = True
datos_cargados = False  

while ejecutar == True:
    print()
    print("MENU DE OPCIONES")
    print("1 - Leer lista de estudiantes (archivo .json)") 
    print("2 - Carga de los datos") 
    print("3 - Mostrar datos de los estudiantes") 
    print("4 - Calcular promedios de estudiantes") 
    print("5 - Mostrar datos ordenados por promedio (DESC)") 
    print("6 - Mostrar estudiante/s con mayor promedio") 
    print("7 - Buscar un estudiante por legajo") 
    print("8 - Exportar la lista actual a JSON") 
    print("9 - Exportar la lista actual a CSV") 
    print("10 - Salir del programa") 
    
    opcion = input("Ingrese una opción (1-10): ")

    if opcion >= "3" and opcion <= "9":
            if datos_cargados == False: 
                print("Error: No se puede acceder. Debe cargar datos (opcion 2) o leer el archivo .json (opcion 1) primero.")
                continue 
            
    match opcion: 
        case "1":
            lista_estudiantes = leer_archivo_json() 
            datos_cargados = True 
            
            if lista_estudiantes[0]["prom"] > 0: 
                promedios_calculados = True  
            else:
                promedios_calculados = False 

        case "2":
            cargar_datos(lista_estudiantes)
            promedios_calculados = False
            datos_cargados = True 
            
        case "3":
            recorrer_y_mostrar(lista_estudiantes)
            
        case "4":
            calcular_promedio(lista_estudiantes)
            promedios_calculados = True
            
        case "5": 
            if promedios_calculados == False:
                print("Debe calcular los promedios primero (opcion 4).")     
            else:
                ordenar_por_promedio(lista_estudiantes) 
                print("Lista ordenada descendente:")
                recorrer_y_mostrar(lista_estudiantes)
            
        case "6":
            if promedios_calculados == False:
                print("Debe calcular los promedios primero (opcion 4).")
            else:
                mostrar_mejores_promedios(lista_estudiantes)
            
        case "7":
            buscar_por_legajo(lista_estudiantes)
            
        case "8":
            exportar_a_json(lista_estudiantes)
            
        case "9":
            exportar_a_csv(lista_estudiantes)
            
        case "10":
            salir_programa()
            ejecutar = False
            
        case _:
            print("Opción no válida. Por favor, ingrese un número del 1 al 10.")
