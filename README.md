
### 📦 Proyecto: Gestor de Productos (Consola - Python + SQLite)

Este es un proyecto educativo en Python que permite gestionar productos utilizando una base de datos SQLite desde una interfaz de consola. Incluye operaciones CRUD (crear, leer, actualizar, eliminar) y funciones adicionales como búsqueda y reportes de inventario bajo.

---

### 📁 Estructura del proyecto

```
gestor_productos/
├── main.py               # Archivo principal, contiene el menú y bucle principal
├── db.py                 # Funciones CRUD y acceso a la base de datos
├── vista.py              # Funciones de interacción con el usuario (menú, validaciones, etc.)
├── productos.db          # Base de datos SQLite (se genera automáticamente)
```

---

### ⚙️ Requisitos

- Python 3.10 o superior

---

### ▶️ Cómo ejecutar

1. Cloná o descargá los archivos del proyecto. Github: https://github.com/gbdadx/TalentoTechPyFinal.git
2. Abrí una terminal en la carpeta del proyecto.
3. Ejecutá:

```bash
python main.py
```

---

### 🤩 Funcionalidades

- Ingresar productos (nombre, cantidad, precio, categoría)
- Listar todos los productos
- Buscar productos por ID, nombre o categoría
- Actualizar productos por ID (uno o varios campos)
- Eliminar productos por ID
- Reportar productos con inventario bajo
- Validaciones para evitar errores de entrada
- Manejo de errores y transacciones con `try/except/finally`

---

### 💃 Base de datos

Se crea automáticamente al iniciar el programa. Los datos se almacenan en `productos.db` con una tabla llamada `productos`.

---

### 🌟 Mejoras futuras (hecho)

- Incorporación de librerías externas  para mejorar el estilo visual y la experiencia del usuario.(Colorama)


---

### ✍️ Autor

Proyecto realizado por **Gabriela Díaz** como práctica de programación en Python con fines educativos.
