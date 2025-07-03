#UTILES.PY
# Provee funciones auxiliares reutilizables como validaciones, limpiar pantalla, pausa, etc

import os
from colorama import init, Fore, Back
init()

def pedir_texto_no_vacio(prompt):
    while True:
        texto = input(prompt).strip()
        if texto == "":
            print(Back.RED + Fore.WHITE + "Error: no puede estar vacío. Intente de nuevo.")
        else:
            return texto

def pedir_texto(prompt):
        texto = input(prompt).strip()
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

   
def mostrar_tabla_productos(resultados, titulo="📋 Productos en Base de Datos", pausar_al_final=True):
    limpiar_pantalla()
    if resultados:
        print(Back.LIGHTCYAN_EX + titulo + '\n')
        print(Back.BLACK + Fore.WHITE + f"{'ID':^6} {'Nombre':^24} {'Descripción':^30} {'Cantidad':^10} {'Precio':>10} {'Categoría':^15}")

        print("-" * 100)
        for fila in resultados:
            id_, nombre, descripcion, cantidad, precio, categoria = fila
            print(f"{id_:^6} {nombre:<24} {descripcion:^30}{cantidad:>10}  {precio:>10.2f} {categoria:^15}")

        print(f"\n✅ Total de productos: {len(resultados)}\n")
    else:
        print(f"⚠️  No se encontraron productos con ese criterio.")

    if pausar_al_final:
        pausar()



def error_opcion():
    print("❌ Opción inválida. Debe ingresar un número del 0 al 8.")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


# Symbols
error_symbol = "❌"  # Red cross
warning_symbol = "⚠️"  # Yellow triangle
success_symbol = "✅"  # Green check mark
