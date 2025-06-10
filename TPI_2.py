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