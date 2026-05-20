from funciones_de_estudiantes import *

def main():
    lista_legajos = []
    lista_nombres = []
    lista_generos = []
    lista_parciales1 = []
    lista_parciales2 = []
    lista_promedios = []

    ejecutar = True
    while ejecutar == True:
        print("\nMENU DE OPCIONES")
        print("1 - Cargar datos de estudiantes (Manual)")
        print("2 - Mostrar todos los estudiantes")
        print("3 - Calcular promedios")
        print("4 - Mostrar ordenados por promedio (DESC)")
        print("5 - Mostrar estudiantes con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir del programa")
        print("8 - Cargar datos de estudiantes (para probar funcionamiento) ")
        
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "2" or opcion == "3" or opcion == "4" or opcion == "5" or opcion == "6":
            if len(lista_legajos) == 0:
                print("\nError: Debe cargar los datos primero usando la opcion 1 o la 8.")
                continue
        
        if opcion == "1":
            lista_legajos.clear()
            lista_nombres.clear()
            lista_generos.clear()
            lista_parciales1.clear()
            lista_parciales2.clear()
            lista_promedios.clear()
            cargar_datos(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2)
            
        elif opcion == "2":
            recorrer_y_mostrar(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2, lista_promedios)
            
        elif opcion == "3":
            calcular_todos_los_promedios(lista_parciales1, lista_parciales2, lista_promedios)
            
        elif opcion == "4":
            if len(lista_promedios) == 0:
                print("Debe calcular los promedios primero (opcion 3).")
            else:
                ordenar_por_promedio(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2, lista_promedios)
                print("\nLista ordenada descendente:")
                recorrer_y_mostrar(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2, lista_promedios)
                
        elif opcion == "5":
            mostrar_mejores_promedios(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2, lista_promedios)
            
        elif opcion == "6":
            buscar_por_legajo(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2, lista_promedios)
            
        elif opcion == "7":
            print("\nFin del programa.")
            ejecutar = False
            
        elif opcion == "8":
            lista_legajos.clear()
            lista_nombres.clear()
            lista_generos.clear()
            lista_parciales1.clear()
            lista_parciales2.clear()
            lista_promedios.clear()
            cargar_datos_prueba(lista_legajos, lista_nombres, lista_generos, lista_parciales1, lista_parciales2)
            
        else:
            print("Opcion incorrecta. Elija del 1 al 8.")

if __name__ == "__main__":
    main()
