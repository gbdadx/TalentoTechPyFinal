#UTILES.PY
# Provee funciones auxiliares reutilizables como validaciones, limpiar pantalla, pausa, etc

import os

def pedir_texto_no_vacio(prompt):
    while True:
        texto = input(prompt).strip()
        if texto == "":
            print("Error: no puede estar vacío. Intente de nuevo.")
        else:
            return texto

def pedir_entero_positivo(prompt):
    while True:
        valor_str = input(prompt).strip()
        if valor_str.isdigit():
            return int(valor_str)
        print("Error: debe ingresar un número entero positivo.")

def pedir_decimal_positivo(prompt):
    while True:
        valor_str = input(prompt).strip().replace(',', '.') #reemplaza la coma
        try:
            valor = float(valor_str)
            if valor >= 0:
                return valor
            else:
                print("Error: el número no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número válido (por ejemplo: 123.45 o 123)")

"""def pausar(): # version original de pausar()
    input("Presione una tecla para volver al menú principal...")"""

# Pausa la ejecución y limpia la pantalla (permite personalizar el mensaje).
def pausar(mensaje="Presione una tecla para continuar..."):
    print(f"\n{mensaje}")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')

   
def mostrar_tabla_productos(resultados, titulo= f"📋 Productos en Base de Datos"):
    if resultados:

        print(f"\n{titulo}\n")
        print(f"{'ID':<4} {'Nombre':<20} {'Cant.':<8} {'Precio':<10} {'Categoría'}")

        for fila in resultados:
            id_, nombre, cantidad, precio, categoria = fila
            print(f"{id_:<4} {nombre:<20} {cantidad:<8} {precio:<10.2f} {categoria}")

        print(f"\n✅ Total de productos: {len(resultados)}\n")
    else:
        print("\n⚠ No hay productos en la base de datos.")
    
    pausar()

def error_opcion():
    print("❌ Opción inválida. Debe ingresar un número del 0 al 8.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
