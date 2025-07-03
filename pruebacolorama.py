from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Style.BRIGHT + Back.CYAN + Fore.WHITE + " Texto brillante ")
print(Style.DIM + Back.YELLOW + Fore.BLACK + " Texto tenue (si la terminal lo permite)")
print(Style.NORMAL + Back.RESET + Fore.RESET + " Texto normal sin colores")
print(Style.RESET_ALL + "Todo reseteado")
print(Style.BRIGHT + Back.RED + Fore.WHITE + "error")