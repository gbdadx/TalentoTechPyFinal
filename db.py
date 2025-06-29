# db.py: Gestiona la base de datos SQLite con todas las operaciones CRUD para los productos.
# Todas las funciones incluyen manejo de errores con try-except-finally.
# Las funciones que modifican datos (no SELECT) usan transacciones con commit y rollback.

import sqlite3
from utiles import *

#establece conexion
def obtener_conexion():
    conn = sqlite3.connect('productos.db')
    cursor = conn.cursor()
    return conn, cursor

#crear tabla productos si no existe
def crear_tabla():
    conn, cursor = obtener_conexion()# Abro conexión local
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                categoria TEXT 
            )
        """)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error al crear la tabla: {e}")
    finally:
        conn.close()

# Ejecuta crear_tabla() dentro de una transacción con manejo de errores.
def inicializar_base():
    conn, cursor = obtener_conexion()
    try:
        crear_tabla()
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error al inicializar la base: {e}")
    finally:
        conn.close()

def mostrar_producto_por_id(id_producto):
    conn, cursor = obtener_conexion()  
    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        resultado = cursor.fetchone()
        if resultado:
            mostrar_tabla_productos([resultado], titulo="✅ Registro actualizado")
        else:
            print("❌ Producto no encontrado.")
    except Exception as e:
        print(f"Error al mostrar producto por ID: {e}")
    finally:
        conn.close()
    pausar("Producto encontrado. Presione una tecla para continuar...")


def ingresar_productos():
    limpiar_pantalla()
    print("INGRESAR PRODUCTOS")
    conn, cursor = obtener_conexion()
    try:
        while True:
            producto = pedir_texto_no_vacio("Ingrese el nombre del producto: ").lower()
            cantidad = pedir_entero_positivo(f"Ingrese la cantidad del producto {producto}: ")
            precio = pedir_decimal_positivo(f"Ingrese el precio del producto {producto}: ")
            categoria = pedir_texto_no_vacio(f"Ingrese la categoría del producto {producto}: ").lower()

            cursor.execute(
                "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (?, ?, ?, ?)",
                (producto, cantidad, precio, categoria)
            )
            conn.commit()

            seguir = input("¿Desea continuar agregando productos (s/n)? ").strip().lower()
            if seguir == 'n':
                break
    except Exception as e:
        conn.rollback()
        print(f"❌ Error al ingresar productos: {e}")
    finally:
        conn.close()
        pausar("Producto(s) ingresado(s). Presione una tecla para volver al menú...")


def listar_productos():
    limpiar_pantalla()
    conn, cursor = obtener_conexion()
    try:
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        mostrar_tabla_productos(resultados, titulo="📋 Productos en Base de Datos")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Función auxiliar que realiza una búsqueda en la tabla productos según el campo y valor indicados.
def buscar_por(campo, valor):
    limpiar_pantalla()
    print(f"... buscando por {campo} ...")

    campos_validos = {'id', 'nombre', 'categoria'}
    if campo not in campos_validos:
        print("Campo no válido")
        return

    conn, cursor = obtener_conexion()
    try:
        cursor.execute(f"SELECT * FROM productos WHERE {campo} = ?", (valor,))
        resultados = cursor.fetchall()
        mostrar_tabla_productos(resultados, titulo=(f"📋 Productos en Base de Datos, búsqueda por {campo} == {valor}"))
        pausar()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def buscar_nombre():
    limpiar_pantalla()
    print("Buscar por nombre")
    try:
        nombre = pedir_texto_no_vacio("Ingrese el nombre del producto: ").lower()
        buscar_por('nombre', nombre)
    except Exception as e:
        print(f"Error al buscar por nombre: {e}")

def buscar_categoria():
    limpiar_pantalla()
    print("Buscar por categoria")
    try:
        categoria = pedir_texto_no_vacio("Ingrese la categoria del producto: ").lower()
        buscar_por('categoria', categoria)
    except Exception as e:
        print(f"Error al buscar por categoria: {e}")

def buscar_id():
    limpiar_pantalla()
    print("Buscar por ID")
    conn, cursor = obtener_conexion()
    resultado = None

    try:
        ID = pedir_entero_positivo("Ingrese el ID del producto: ")
        cursor.execute("SELECT * FROM productos WHERE id = ?", (ID,))
        resultado = cursor.fetchone()
    except Exception as e:
        print(f"Error al buscar el producto: {e}")
    finally:
        conn.close()

    if resultado:
        return resultado 
    else:
        print("❌ No se encontró ningún producto con ese ID.")
        return None

# Elimina el registro segun ID ingresada
def eliminar_id():
    limpiar_pantalla()
    print("Eliminar por ID")
    encontrado = buscar_id()  # Usa su propia conexión

    encontrado = buscar_id()

    if not encontrado:
        return

    # Mostrar el producto antes de confirmar
    mostrar_tabla_productos([encontrado], titulo="🔍 Registro a eliminar")

    respuesta = input("¿Está seguro que quiere eliminar este registro? (s/n): ").strip().lower()


    try:
        conn, cursor = obtener_conexion()
        cursor.execute("DELETE FROM productos WHERE id = ?", (encontrado[0],))
        conn.commit()
        print("✅ Registro eliminado correctamente.\n\n\n\n\n\n")
    except Exception as e:
        conn.rollback()
        print(f"❌ Error al eliminar el producto: {e}")
    finally:
        conn.close()

    pausar("Producto eliminado. Presione una tecla para continuar...")

#Permite actualizar (cambiar) el valor de uno o mas campos
def actualizar_id():
    limpiar_pantalla()
    conn, cursor = obtener_conexion()
    try:
        print("Actualizar por ID")
        encontrado = buscar_id()
        print("\n\n")
        if not encontrado:
            return

        # Mostrar el producto antes de confirmar si se quiere modificar
        mostrar_tabla_productos([encontrado], titulo="🔍 Registro encontrado")


        respuesta = input("¿Está seguro que quiere modificar este registro? (s/n): ").strip().lower()
        if respuesta != 's':
            print("❌ Operación cancelada.")
            return

        opcion = input("""¿Qué campo/campos desea modificar?:  
        1. nombre
        2. cantidad
        3. precio
        4. categoría
        5. todos
        → """)

        id_producto = encontrado[0]  

        match opcion:
            case '1':
                producto = pedir_texto_no_vacio("Ingrese el nombre del producto: ").lower()
                cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (producto, id_producto))

            case '2':
                cantidad = pedir_entero_positivo("Ingrese la cantidad del producto: ")
                cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (cantidad, id_producto))

            case '3':
                precio = pedir_decimal_positivo("Ingrese el precio del producto: ")
                cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id_producto))

            case '4':
                categoria = pedir_texto_no_vacio("Ingrese la categoría del producto: ").lower()
                cursor.execute("UPDATE productos SET categoria = ? WHERE id = ?", (categoria, id_producto))

            case '5':
                producto = pedir_texto_no_vacio("Ingrese el nombre del producto: ").lower()
                precio = pedir_decimal_positivo(f"Ingrese el precio del producto {producto}: ")
                categoria = pedir_texto_no_vacio(f"Ingrese la categoría del producto {producto}: ").lower()
                cantidad = pedir_entero_positivo(f"Ingrese la cantidad del producto {producto}: ")
                cursor.execute(
                    "UPDATE productos SET nombre = ?, precio = ?, categoria = ?, cantidad = ? WHERE id = ?",
                    (producto, precio, categoria, cantidad, id_producto)
                )

            case _:
                print("❌ Opción inexistente - Operación cancelada.")
                return

        conn.commit()
        mostrar_producto_por_id(id_producto)
        print("✅ Registro actualizado correctamente.\n\n\n\n\n")

    except Exception as e:
        conn.rollback()
        print(f"❌ Error al actualizar el producto: {e}")
    finally:
        conn.close()

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
