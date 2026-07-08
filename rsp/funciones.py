MAX_ALUMNOS= 27
#VALIDACIONES CLAVES DICCIONARIOS 
def validar_entero(cadena: str) -> bool:
    """Funcion que valida si una cadena contiene solo dígitos."""

    valor = True #bandera para no escribir mas de un retorono
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


#OPCION 2: Carga de datos
def cargar_datos(legajos, ape_nombres, generos, parciales1, parciales2):
    print(f"\nIniciando carga manual de {MAX_ALUMNOS} estudiantes")
    for i in range(MAX_ALUMNOS):
        #cuenta del 0 al 26
        print(f"Carga del estudiante {i + 1}:")
        legajos.append(validar_legajo())
        ape_nombres.append(validar_ape_nom())
        generos.append(validar_genero())
        parciales1.append(validar_nota("Nota del Primer Parcial (1-10): "))
        parciales2.append(validar_nota("Nota del Segundo Parcial (1-10): "))
    print("Carga de datos finalizada con éxito.")


#OPCION 3: Mostrar un elemento
def mostrar_un_elemento(lista_estudiantes, legajo, nombre, genero, pp, sp, estudiante, promedio=None): # esta mal #lista_estudiantes,legajo, ape_nom, genero, pp, sp, promedio=None
    if promedio is not None and promedio != 0.0:
        print("----------------------------------------------------------------")
        print("| LEGAJO | NOMBRE      | GENERO | Nota PP | Nota SP | PROMEDIO |")
        print("|--------|-------------|--------|---------|---------|----------|")
        for estudiante in lista_estudiantes:
            print(f'|{estudiante["legajo"]:<7} | {estudiante["ape_nom"]:<11} | {estudiante["genero"]:<6} | {estudiante["pp"]:<7} | {estudiante["sp"]:<7} | {estudiante["prom"]:<9}|')
    else:
        print("----------------------------------------------------------------")
        print("| LEGAJO | NOMBRE      | GENERO | Nota PP | Nota SP | PROMEDIO |")
        print("|--------|-------------|--------|---------|---------|----------|")
        for estudiante in lista_estudiantes:
            print(f'|{estudiante["legajo"]:<7} | {estudiante["ape_nom"]:<11} | {estudiante["genero"]:<6} | {estudiante["pp"]:<7} | {estudiante["sp"]:<7}')   


#3b: Recorrer
def recorrer_y_mostrar(legajos, nombres, generos, parciales1, parciales2, promedios_lista): #esta mal
    print("REPORTE GENERAL DE ESTUDIANTES")
    for i in range(len(legajos)):
        if len(promedios_lista) == 0:
            break #promedios_lista = none
        else:    
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], parciales1[i], parciales2[i], promedios_lista[i])


#Opcion 4: Calcular promedio 
def calcular_todos_los_promedios(parciales1, parciales2, promedios):
    promedios.clear()
    for i in range(len(parciales1)):
        promedios_lista = (parciales1[i] + parciales2[i]) / 2.0
        promedios.append(promedios_lista)
    print("Promedios calculados y guardados exitosamente.")


#Opcion 5: Ordenar promedios DESC (descendente)
def ordenar_por_promedio(legajos, nombres, generos, parciales1, parciales2, promedios, criterio="DESC"):
    n = len(promedios)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            debe_intercambiar = False
            # if criterio == "ASC" and promedios[j] > promedios[j + 1]:
            #     debe_intercambiar = True
            if criterio == "DESC" and promedios[j] < promedios[j + 1]:
                debe_intercambiar = True
                
            if debe_intercambiar:
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                generos[j], generos[j + 1] = generos[j + 1], generos[j]
                parciales1[j], parciales1[j + 1] = parciales1[j + 1], parciales1[j]
                parciales2[j], parciales2[j + 1] = parciales2[j + 1], parciales2[j]


#Opcion 6: Mostrar mejores promedios:
def mostrar_mejores_promedios(legajos, nombres, generos, parciales1, parciales2, promedios):
    if not promedios:
        print("Primero debe calcular los promedios (Opción 3).")
        return
    
    mayor_promedio = promedios[0]
    for p in promedios:
        if p > mayor_promedio:
            mayor_promedio = p
            
    print(f"Estudiante(s) con el Mayor Promedio ({mayor_promedio})")
    for i in range(len(promedios)):
        if promedios[i] == mayor_promedio:
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], parciales1[i], parciales2[i], promedios[i])


#Opcion 7: Buscar estudiante por promedio 
def buscar_por_legajo(legajos, nombres, generos, parciales1, parciales2, promedios):
    print("\nBúsqueda de Estudiante")
    buscado = validar_legajo()
    encontrado = False
    
    for i in range(len(legajos)):
        if legajos[i] == buscado:
            print("\nEstudiante encontrado:")
            if len(promedios) == 0:
                prom = None
            else:
                prom = promedios[i]
            mostrar_un_elemento(legajos[i], nombres[i], generos[i], parciales1[i], parciales2[i], prom)
            encontrado = True
            break
            
    if not encontrado:
        print(f"No se encontró ningún estudiante con el legajo {buscado}.")
