# modulos.py: 
#  funciones de presentación e interacción con el usuario, como mostrar el menú y validar entradas.


# importando modulos
from utiles import *

from db import inicializar_base, obtener_conexion


#operaciones bbdd

inicializar_base()


def mostrar_menu():
    print( "📦 MENÚ DE PRODUCTOS")
    print("""
1. Ingresar producto  
2. Listar productos  
3. Buscar por nombre
4. Buscar por categoria  
5. Buscar por ID  
6. Actualizar por ID
7. Eliminar por ID  
8. Inventario bajo  

0. Salir del programa

""")
    

def reportar_bajo_inventario():    
    limpiar_pantalla()

    conn, cursor = obtener_conexion()
    try:
        cantidad = pedir_entero_positivo("Ingrese el límite inferior de stock: ")
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (cantidad,))
        resultados = cursor.fetchall()
        mostrar_tabla_productos(resultados, titulo=(f"📋 Productos con inventario ≤ {cantidad}"))
    except Exception as e:
        print(f"Error al generar el reporte: {e}")
    finally:
        conn.close()




