# modulos.py: 
# Funciones de interfaz de usuario, como el menú principal.


# importando modulos
from utiles import *
from colorama import Fore, Back, Style, init

init(autoreset=True, convert=True)  # convert=True arregla ANSI en Windows


# Menu funciones-opciones 
def mostrar_menu():
    limpiar_pantalla()
    #print( Back.CYAN + Fore.WHITE  + f" MENÚ DE PRODUCTOS   "+ Style.RESET_ALL)
    print(Style.BRIGHT + Back.CYAN + f" 📦 MENÚ DE PRODUCTOS   " + Style.RESET_ALL)

    print(Back.BLACK + Fore.WHITE +""" 
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
    






