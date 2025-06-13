from collections import defaultdict

#EXPRESIÓN NATURAL
def verificar_validez_digito(digito, grupo):
    # Se convierte el dígito a string para poder buscarlo dentro de los DNI
    digito_a_buscar = str(digito)
    
    # Se inicializa un contador para las personas que cumplen la condición
    contador = 0
    
    # Se recorre cada persona en el grupo
    for persona in grupo:
        # Si el dígito está en el DNI de la persona...
        if digito_a_buscar in persona['DNI']:
            # ...se incrementa el contador
            contador += 1
            
    # La función devuelve True solo si el contador es 4 o más
    return contador >= 4

def evaluar_condiciones(listado_dnis, funcion_condicion):
    resultados = []
    for dni in listado_dnis:
        resultado = funcion_condicion(dni) 
        resultados.append(resultado)
    return resultados

def validar_dni(dni):
    if not (7 <= len(dni) <= 9) or not dni.isdigit():
        return False
    return True


def es_par(anio):
    return anio % 2 == 0

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def calcular_edad(anio_nacimiento, anio_actual):
    return anio_actual - anio_nacimiento

def contar_frecuencias(dni):
    frecuencia_digitos = {}
    for digito in dni:
        if digito in frecuencia_digitos:
            frecuencia_digitos[digito] += 1
        else:
            frecuencia_digitos[digito] = 1
    return frecuencia_digitos

def sumar_digitos(dni):
    suma_total = sum(int(digito) for digito in dni)
    return suma_total


def evaluar_digito_exclusivo(listado_dni): #Expresion Natural Nº 4: "Un dígito es exclusivo si aparece únicamente en un solo DNI del grupo."
    digitos_exclusivos = set()
    for i, dni in enumerate(listado_dni):
        digitos_dni = set(dni)
        for digito in digitos_dni:
            if sum(1 for d in listado_dni if digito in d) == 1:
                digitos_exclusivos.add(digito)
    return digitos_exclusivos

# Función para Expresión 2
def encontrar_digitos_especiales(lista_dnis):
    conjuntos = [generar_conjunto(dni) for dni in lista_dnis]
    contador = defaultdict(int)

    for conjunto in conjuntos:
        for digito in conjunto:
            contador[digito] += 1

    especiales = {digito for digito, cantidad in contador.items() if cantidad == 2}
    return especiales


def generar_conjunto(dni):
    conjunto = set(dni)
    return conjunto

def realizar_union(conjunto_1, conjunto_2):
    return conjunto_1.union(conjunto_2)

def realizar_interseccion(conjunto_1, conjunto_2):
    return conjunto_1.intersection(conjunto_2)

def realizar_diferencia(conjunto_1, conjunto_2):
    return conjunto_1.difference(conjunto_2)

def realizar_diferencia_simetrica(conjunto_1, conjunto_2):
    return conjunto_1.symmetric_difference(conjunto_2)

def realizar_operaciones(conjunto_1, conjunto_2):
    union_resultado = realizar_union(conjunto_1, conjunto_2)
    print(f"Unión: {union_resultado}")

    interseccion_resultado = realizar_interseccion(
        conjunto_1, conjunto_2)
    print(f"Intersección: {interseccion_resultado}")

    diferencia_resultado = realizar_diferencia(conjunto_1, conjunto_2)
    print(f"Diferencia: {diferencia_resultado}")

    diferencia_simetrica_resultado = realizar_diferencia_simetrica(
        conjunto_1, conjunto_2)
    print(f"Diferencia Simétrica: {diferencia_simetrica_resultado}")


def procesar_anios():
    listado_anios = []
    anios_pares = 0
    anios_impares = 0

    print("=== Ingreso de años de nacimiento ===")
    cantidad = int(input("Cuántos años de nacimiento desea ingresar? "))
    for _ in range(cantidad):
        anio = int(input("\nIngrese un año de nacimiento: "))
        if es_par(anio):
            anios_pares += 1
        else:
            anios_impares += 1
        listado_anios.append(anio)

    gen_z = all(anio >= 2000 for anio in listado_anios)
    hay_bisiesto = any(es_bisiesto(anio) for anio in listado_anios)

    anio_actual = 2025
    listado_edades = [calcular_edad(anio, anio_actual) for anio in listado_anios]

    producto_cartesiano = list(zip(listado_anios, listado_edades))

    # Mostrar resultados
    print("\n\n=== Resultados ===")
    print(f"\nCantidad de años pares: {anios_pares}")
    print(f"Cantidad de años impares: {anios_impares}")

    if gen_z:
        print("\nGrupo Z")
        print("Todos los años ingresados son posteriores al 2000")

    if hay_bisiesto:
        print("\nTenemos un año especial")

    print("\nProducto cartesiano de años y edades:")
    for anio, edad in producto_cartesiano:
        print(f"Año: {anio}, Edad: {edad}")
        
def verificar_digito_comun(conjuntos):
    if not conjuntos:
        return
    interseccion = conjuntos[0]
    for conjunto in conjuntos[1:]:
        interseccion = interseccion.intersection(conjunto)
    if interseccion:
        print(f"Dígito(s) compartido(s) en todos los conjuntos: {interseccion}")
    else:
        print("No hay ningún dígito compartido en todos los conjuntos.")
#EXPRESION NATURAL 3
def digitos_relevantes_AyC_noD(dni_a, dni_c, dni_d):
    set_a = set(str(dni_a))
    set_c = set(str(dni_c))
    set_d = set(str(dni_d))
    interseccion_ac = set_a.intersection(set_c)
    resultado = interseccion_ac.difference(set_d)
    return resultado


def compartidos_sin_A(dni_a, dni_b, dni_c):
    set_a = set(str(dni_a))
    set_b = set(str(dni_b))
    set_c = set(str(dni_c))
    
    resultado = (set_b & set_c) - set_a    
    return resultado


def procesar_dnis():
    listado_dni = []
    conjuntos_unicos = []
    print("=== Ingreso de DNIs ===")
    print("Ingrese los DNIs (sin puntos). Deje en blanco para finalizar.")
    while True:
        dni = input("Ingrese un DNI: ")
        if dni == "":
            break
        if not validar_dni(dni):
            print("DNI inválido. Debe tener entre 7 y 9 dígitos y contener solo números.")
            continue                                  
        else:
            listado_dni.append(dni)
            
    print("\n\n=== Resultados ===")
    print("=== Generación de conjuntos de dígitos únicos ===")
    conjuntos_unicos = [generar_conjunto(dni) for dni in listado_dni]
    for i, conjunto in enumerate(conjuntos_unicos):
        print(f"DNI {listado_dni[i]}: Conjunto de dígitos únicos: {conjunto}")

        # Aporte de Valentín: Verificar dígitos comunes en todos los conjuntos
    if len(conjuntos_unicos) >= 2:
        verificar_digito_comun(conjuntos_unicos)
    
    print("\n=== Cálculo de operaciones con conjuntos ===")
    if len(listado_dni) < 2:
        print("Debe ingresar al menos dos DNIs para realizar operaciones.")
        return

    conjunto_1 = conjuntos_unicos[0]
    conjunto_2 = conjuntos_unicos[1]
    realizar_operaciones(conjunto_1, conjunto_2)

    print("\n=== Conteo de frecuencia de cada dígito en cada DNI ===")
    if not listado_dni:
        print("No hay DNIs ingresados.")
        return

    for dni in listado_dni:
        frecuencias = contar_frecuencias(dni)
        print(f"Frecuencia del DNI {dni}: {frecuencias}")

    print("\n=== Suma total de los dígitos de cada DNI ===")
    if not listado_dni:
        print("No hay DNIs ingresados.")
        return

    for dni in listado_dni:
        suma = sumar_digitos(dni)
        print(f"Suma total de los dígitos del DNI {dni}: {suma}")

    print("\n=== Evaluación de condiciones lógicas ===")
    if not listado_dni:
        print("No hay DNIs ingresados.")
        return

    def funcion_condicion(conjunto): return "Dígito compartido" if len(
        conjunto) < 8 else "Diversidad numérica alta"
    resultados = evaluar_condiciones(listado_dni, funcion_condicion)
    for i, resultado in enumerate(resultados):
        print(f"DNI {listado_dni[i]}: {resultado}")

    print("\n=== Evaluación de Expresiones Naturales ===")
    if len(listado_dni) < 2:
        print("Se necesitan al menos 2 DNIs para evaluar las expresiones.")
        return

    #print("\nExpresión 1: Dígitos que aparecen exactamente en 2 DNI distintos")
    

    print("\nExpresión 2: Dígitos que aparecen exactamente en 2 DNI distintos")
    digitos_especiales_2 = encontrar_digitos_especiales(listado_dni)
    print(f"Dígitos especiales: {digitos_especiales_2}")

    #print("\nExpresión 3: Dígitos en A y C pero no en D")
    if len(listado_dni) >= 4:
        dni_a = listado_dni[0]
        dni_c = listado_dni[2]
        dni_d = listado_dni[3]
        relevantes = digitos_relevantes_AyC_noD(dni_a, dni_c, dni_d)
        print("\nExpresión 3: Dígitos en A y C pero no en D")
        print(f"Dígitos relevantes: {relevantes}")
    else:
        print("\nExpresión 3: Se requieren al menos 4 DNIs para esta expresión.")

    print("\nExpresión 4: Dígitos exclusivos (aparecen en un solo DNI)")
    digitos_exclusivos = evaluar_digito_exclusivo(listado_dni)
    print(f"Dígitos exclusivos: {digitos_exclusivos}")

    print("\nExpresión 5: Dígitos compartidos entre B y C pero no en A")
    if len(listado_dni) < 3:
        print("Se necesitan al menos 3 DNIs para esta expresión")
    else:
        digitos_compartidos_BC = compartidos_sin_A(listado_dni[0], listado_dni[1], listado_dni[2])
        print(f"Dígitos compartidos entre B y C pero no en A: {digitos_compartidos_BC}")

def menu():
    print("\n=== Menú de Ejercicios ===")    
    print("\n1. Operaciones con DNIs")
    print("2. Operaciones con años de nacimiento")
    print("3. Salir")
    opcion = input("Elige el ejercicio a ejecutar: ")
    return opcion

if __name__ == "__main__":
    while True:
        opcion = menu()

        if opcion == "1":
            procesar_dnis()
        elif opcion == "2":
            procesar_anios()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del menú.")