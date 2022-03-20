import os
from colorama import init, Fore, Back, Style
init()
os.system('cls')
R = Fore.RED
V = Fore.GREEN
B = Fore.WHITE
print(R+'''
         _     _  _  _ '''+V+'''    _________________   _______
        '''+R+'''| \   / |\ \/ /'''+V+'''   |  ___  ||   __ \ \ |  _  \ \ 
        '''+R+'''|  \_/  | \  /'''+V+'''    | |   | ||  |  | | ||_|_|_/ /
        '''+R+'''| |\_/| | / / '''+V+'''    | |___| ||  |__| | ||  _  \ \ 
        '''+R+'''|_|   |_|/_/  '''+V+'''    |_|   |_||______/_/ |_|_|_/_/
''')
print(Style.DIM+'Coloque el nombre del archivo que desea pasar a la ruta de su telefono: '+B)
nombre = input('> ')
os.system('adb.exe push \"'+nombre+'\" /sdcard/')

# para el comando de enviar archivos es adb.exe push +nombre del archivo+
# para enviar archivos a la PC primero crea una carpeta con el comando mkdir MyADB, depués usa adb.exe pull /sdcard/+nombre del archivo+ MyADB
# para apagar el telefono usa adb.exe shell reboot -p
# para reiniciar adb.exe reboot
# para fastboot adb.exe reboot bootloader
# para recoveru adb.exe reboot recovery

# Por cada acción que el usuario haga que imprima Listo no importa si hubo error.

print('Listo')

