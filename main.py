# codigo principal main.py
# Controla el flujo principal del programa .


#importa modulos requeridos para el flujo principal
from vista import *
from db import *
from utiles import limpiar_pantalla

limpiar_pantalla()

# Menu principal
while True:
    mostrar_menu()
    opcion = input("Elija una opción (0 al 8): ").strip()
    
    if opcion.isdigit():
        match int(opcion):
            case 0:
                print("Saliendo del programa... ¡Hasta luego!")
                pausar()
                break

            case 1:
                ingresar_productos()
            case 2:
                listar_productos()
            case 3:
                buscar_nombre()
            case 4:
                buscar_categoria()
            case 5:
                resultado = buscar_id()
                if resultado:
                        mostrar_tabla_productos([resultado], titulo="🔍 Producto encontrado por ID")

            case 6:
                actualizar_id()
            case 7:
                eliminar_id()
            case 8:
                reportar_bajo_inventario()
                
            case _:
                error_opcion()
    else:
        print("❌ Error: Debe ingresar un número.")

