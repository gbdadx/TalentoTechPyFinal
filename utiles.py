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

   
def mostrar_tabla_productos(resultados, titulo="📋 Productos en Base de Datos", pausar_al_final=True):
    if resultados:
        print(titulo)
        print(f"{'ID':<4} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
        print("-" * 60)
        for fila in resultados:
            print(f"{fila[0]:<4} {fila[1]:<20} {fila[2]:<10} {fila[3]:<10.2f} {fila[4]:<15}")
        print(f"\n✅ Total de productos: {len(resultados)}\n")
    else:
        print(f"⚠️  No existe en la base de datos. Verifique el nombre.")

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
