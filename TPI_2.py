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
    cantidad = int(input("Cuantos años de nacimiento desea ingresar? "))
    for _ in range(cantidad):
        anio = int(input("\nIngrese un año de nacimiento: "))
        if es_par(int(anio)):
            anios_pares += 1
        else:
            anios_impares += 1
        listado_anios.append(int(anio))
    gen_z = True
    for anio in listado_anios:
        if anio < 2000:
            gen_z = False
            break
    hay_bisiesto = False
    for anio in listado_anios:
        if es_bisiesto(anio):
            hay_bisiesto = True
    anio_actual = 2025
    listado_edades = []
    for anio in listado_anios:
        edad = calcular_edad(anio, anio_actual)
        listado_edades.append(edad)
    producto_cartesiano = []
    for anio in listado_anios:
        for edad in listado_edades:
            producto_cartesiano.append((anio, edad))
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