#VALIDACIONES CLAVES DICCIONARIOS 
def validar_entero(cadena: str) -> bool:
    """Funcion que valida si una cadena contiene solo dígitos usando una lista de numeros validos para controlar.
    Args: cadena(str): cadena que se ingresa y se analiza
    Returns: (bool): TRUE si toda la cadena contiene los numeros que estan en la lista
                     FALSE si la cadena no contiene ningun numero de los que estan en la lista"""

    valor = True  
    if len(cadena) == 0:
        valor = False
    else:
        digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for caracter in cadena:
            encontrado = False
            for d in digitos:
                if caracter == d:
                    encontrado = True
                    break
            if not encontrado:
                valor = False
                break

    return valor

def validar_legajo():
    """Funcion que valida si el legajo inresado es un numero entero.
    Args: None
    Returns: (int) Retorna el numero del legajo ingresado si pasa por la funcion de validacion de entero anterior"""

    while True:
        input_legajo = input("Ingrese el número de legajo: ")
        if input_legajo == "":
            print("Error: El campo no puede estar vacío")
        elif validar_entero(input_legajo):
            return int(input_legajo)
        else:
            print("Error: El legajo debe contener únicamente números enteros.")


def validar_ape_nom():
    """Funcion que valida si el nombre y apellido ingresados contiene solamente letras y espacios
    Args: None
    Return: Retorna el nombre y appellido ingresados si pasa por el bucle for que recorre la lista de letras validas"""

    while True:
        input_nombre = input("Ingrese Apellido y Nombre: ")
        if input_nombre == "":
            print("Error: El campo no puede estar vacío.")
            continue

        letras_validas = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            " " 
        ]
        
        es_valido = True
        for caracter in input_nombre:
            encontrado = False    
            for l in letras_validas:
                if caracter == l:
                    encontrado = True
                    break
            if not encontrado:
                es_valido = False
                break    
        if es_valido:
            return input_nombre
        else:
            print("Error: El nombre debe contener solo letras y espacios.")    

def validar_genero():
    """Funcion que valida si el genero ingresado esta entre alguna de las opciones F,M,X (y f,m,x)
    Args: None
    Returns: Si es alguna de las opciones que ofrece el input, entonces retorna el genero ingresado"""

    while True:
        input_genero = input("Ingrese el género (F / M / X): ")
        if input_genero == "":
            print("Error: El campo no puede estar vacío.")
        elif input_genero == "F" or input_genero == "f" or input_genero == "M" or input_genero == "m" or input_genero == "X" or input_genero == "x":
            return input_genero
        else:
            print("Error: Género inválido. Opciones permitidas: F, M o X.")


def validar_nota(mensaje: str):
    """Funcion que valida si la nota ingresada en los dos parciales es un numero entero y si esta entre 1 al 10.
    Args: mensaje(str): mensaje que aparece como entrada para ingresar las notas
    Returns: Si la nota ingresada pasa por la funcion validar entero y es un numero entre 1 y 10, retorna 
    la nota ingresada"""

    while True:
        input_nota = input(mensaje)
        if  input_nota == "":
            print("Error: El campo no puede estar vacio.")
            continue  
        if validar_entero(input_nota):
            nota = int(input_nota)
            if 1 <= nota <= 10:
                return nota  
            else:
                print("Error: La nota debe ser un numero del 1 al 10")
        else:
            print("Error: Debe inresar unicamente numeros enteros")


# ==========================================
# FUNCIONES DEL MENÚ
# ==========================================

# Opcion 1: Leer archivo JSON
def leer_archivo_json():
    """Funcion que se encarga de leer el archivo JSON, completar la lista
    hasta 10 elementos y mostrar los datos por consola.
    Args:  None
    Return: Retorna el archvio json por consola mediante la variable 'datos' """
    
    import json
    with open('prueba/data_sp.json', 'r') as archivo_json:
        datos = json.load(archivo_json)

    for i in range(len(datos)):
        print(f"ESTUDIANTE {i + 1}") 
        print(f"legajo: {datos[i]['legajo']}")
        print(f"ape_nom: {datos[i]['ape_nom']}")
        print(f"género: {datos[i]['genero']}")
        print(f"pp: {datos[i]['pp']}")
        print(f"sp: {datos[i]['sp']}")
        print(f"prom: {datos[i]['prom']}")
        print()

    
    resto_de_estudiantes = 10 - len(datos) 
    for r in range(resto_de_estudiantes):
        datos.append({
            "legajo": 0, "ape_nom": "", "genero": "", "pp": 0, "sp": 0, "prom": 0.0
        })
    
    return datos
    
# #OPCION 2: Carga de datos
def cargar_datos(lista_estudiantes):
    """Funcion que sirve para cargar los datos de los estudiantes. Si los datos pasan por la validacion correspondiente
    entonces quedan guardados en las respectivas claves del diccionario
    Args: lista_estudiantes""" 

    cargado = False
    for i in range(len(lista_estudiantes)): #10
        if lista_estudiantes[i]["legajo"] == 0:
            print(f"Cargando datos del estudiante {i + 1}:")
            
            legajo = validar_legajo()
            nombre = validar_ape_nom()
            genero = validar_genero()
            p1 = validar_nota("Nota del Primer Parcial (1-10): ")
            p2 = validar_nota("Nota del Segundo Parcial (1-10): ")

            lista_estudiantes[i]["legajo"] = legajo
            lista_estudiantes[i]["ape_nom"] = nombre
            lista_estudiantes[i]["genero"] = genero
            lista_estudiantes[i]["pp"] = p1
            lista_estudiantes[i]["sp"] = p2
            lista_estudiantes[i]["prom"] = 0.0
            print("Estudiante cargado con éxito.")
            cargado = True
            break    
        
    if cargado == False:
        print("La lista de alumnos esta completa. No hay espacio libre.")

#Opcion 3a: Mostrar un elemento
def mostrar_un_elemento(estudiante):
    """Funcion que se encarga de mostrar los datos de cada estudiante usando su correspondiente diccionario.
    Args: estudiante"""

    promedio = estudiante["prom"]
    if promedio is not None and promedio != 0.0:
        print(f'|{estudiante["legajo"]:<7} | {estudiante["ape_nom"]:<18} | {estudiante["genero"]:<6} | {estudiante["pp"]:<7} | {estudiante["sp"]:<7} | {estudiante["prom"]:<8} |')
    else:
        print(f'|{estudiante["legajo"]:<7} | {estudiante["ape_nom"]:<18} | {estudiante["genero"]:<6} | {estudiante["pp"]:<7} | {estudiante["sp"]:<7} | {"-":<8} |') 

#Opcion 3b: Recorrer y mostrar
def recorrer_y_mostrar(lista_estudiantes):
    """Funcion que imprime la estructura de la tabla y recorre los estudiantes cargados.
    Args: lista_estudiantes """

    print("-----------------------------------------------------------------------")
    print("| LEGAJO | NOMBRE             | GENERO | Nota PP | Nota SP | PROMEDIO |")
    print("|--------|--------------------|--------|---------|---------|----------|")
    
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] != 0:  
            mostrar_un_elemento(estudiante)
            
    print("-----------------------------------------------------------------------")

# ITEM 4: Calcular promedio
def calcular_promedio(lista_estudiantes): 
    """Funcion que calcula el promedio de cada estudiante activo (legajo != 0)."""
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["legajo"] != 0:
            lista_estudiantes[i]["prom"] = (lista_estudiantes[i]["pp"] + lista_estudiantes[i]["sp"]) / 2.0
    print("Promedios calculados y guardados exitosamente.")

# auxiliar 
def obtener_promedio(estudiante):
    """Funcion que extrae el/los promedios cargados de los estudiantes para usarlo como "llave" en la funcion de 
    ordenamiento: sort()
    Args: estudiante"""
    return estudiante["prom"]

# ÍTEM 5: Ordenar por promedio (DESC)
def ordenar_por_promedio(lista_estudiantes):
    """Funcion que ordena la lista de diccionarios de forma DESC basándose en el promedio.
    Para eso, separa los alumnos cargados de los alumnos que no han sido cargados y despues de ordenar los promedios
    agrega a la lista los datos que correspondan
    Args: lista_estudiantes"""
    
    datos_cargados = []
    datos_no_cargados = []
    
   #Separa alumnos ya cargados de los que no se cargaron 
    for estudiante in lista_estudiantes:
        if estudiante["legajo"] != 0: 
            datos_cargados.append(estudiante)
        else:
            datos_no_cargados.append(estudiante)
            
    datos_cargados.sort(key=obtener_promedio, reverse=True)
    
    lista_estudiantes.clear()
    
    for cargados in datos_cargados:
        lista_estudiantes.append(cargados) 
        
    for no_cargados in datos_no_cargados:
        lista_estudiantes.append(no_cargados)

#ITEM 6: mostrar mejor promedio
def mostrar_mejores_promedios(lista_estudiantes):
    """Funcion que busca el mayor promedio entre los estudiantes cargados y los muestra.
    Args: lista_estudiantes"""

    #Promedio de base
    mayor_promedio = lista_estudiantes[0]["prom"]
                        
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["legajo"] == 0:
            continue 
        elif lista_estudiantes[i]["prom"] > mayor_promedio:
            mayor_promedio = lista_estudiantes[i]["prom"]
            
    print(f"Estudiante(s) con el Mayor Promedio ({mayor_promedio})") 
    print("-----------------------------------------------------------------------")
    print("| LEGAJO | NOMBRE             | GENERO | Nota PP | Nota SP | PROMEDIO |")
    print("|--------|--------------------|--------|---------|---------|----------|")
    
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["legajo"] != 0 and lista_estudiantes[i]["prom"] == mayor_promedio: 
            mostrar_un_elemento(lista_estudiantes[i])
    
    print("-----------------------------------------------------------------------")

# ITEM 7: Buscar por legajo
def buscar_por_legajo(lista_estudiantes):
    """Funcion que realiza la busqueda de un estudiante pidiendo el legajo mediante la validacion."""
    print("Búsqueda de Estudiante")
    buscado = validar_legajo()
    encontrado = False
   
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i]["legajo"] != 0 and lista_estudiantes[i]["legajo"] == buscado:
           
            print("Estudiante encontrado:")
            print("-----------------------------------------------------------------------")
            print("| LEGAJO | NOMBRE             | GENERO | Nota PP | Nota SP | PROMEDIO |")
            print("|--------|--------------------|--------|---------|---------|----------|")

            mostrar_un_elemento(lista_estudiantes[i])
            encontrado = True
            
            print("-----------------------------------------------------------------------")    
    
    if not encontrado:
        print(f"No se encontró ningún estudiante con el legajo {buscado}. ") 
        
#ITEM 8: Exportar a json
def exportar_a_json(lista_estudiantes):
    import json
    print("Exportando a JSON...")
    
    alumnos_cargados = []

    for estudiante in lista_estudiantes:
        if estudiante["legajo"] != 0:
            alumnos_cargados.append(estudiante)
            
    with open('prueba/data_sp.json', 'w') as archivo_json:
        json.dump(alumnos_cargados, archivo_json, indent=4) 

# ÍTEM 9: Exportar a CSV   
def exportar_a_csv(lista_estudiantes):
    """Exporta la lista de diccionarios a un archivo CSV sin los casilleros vacíos."""
    print("Exportando a CSV...")
    nombres_columnas = ["legajo", "ape_nom", "genero", "pp", "sp", "prom"]
    
    with open("prueba/data_sp.csv", "w") as archivo:
        archivo.write(",".join(nombres_columnas) + "\n")
        for estudiante in lista_estudiantes:
            # FILTRO: Solo escribe si el alumno es real (legajo distinto de 0)
            if estudiante['legajo'] != 0:
                linea = f"{estudiante['legajo']},{estudiante['ape_nom']},{estudiante['genero']},{estudiante['pp']},{estudiante['sp']},{estudiante['prom']}"
                archivo.write(linea + "\n")
                #"\n": salto de linea
    
    print("Archivo 'data_sp.csv' guardado con éxito.")

#Item 10: Salir del programa
def salir_programa():
    """Funcion que se encarga de salir del programa"""
    print("Hasta luego!")
    print("Saliendo del programa...")
