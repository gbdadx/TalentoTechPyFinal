# modulos.py: 
# Funciones de interfaz de usuario, como el menú principal.


# importando modulos
from utiles import *
from colorama import Fore, Back, Style 



# Menu funciones-opciones 
def mostrar_menu():
    print(Style.BRIGHT + Back.CYAN + f" 📦 MENÚ DE PRODUCTOS " + Style.RESET_ALL)
    print(Back.BLACK + Fore.WHITE + """
╔════════════════════════════════════╗
║ 1. Ingresar producto               ║
║ 2. Listar productos                ║
║ 3. Buscar por nombre               ║
║ 4. Buscar por categoría            ║
║ 5. Buscar por ID                   ║
║ 6. Actualizar por ID               ║
║ 7. Eliminar por ID                 ║
║ 8. Inventario bajo                 ║
║ 9. Exportar a csv                  ║
║                                    ║
║ 0. Salir del programa              ║
╚════════════════════════════════════╝
""")






