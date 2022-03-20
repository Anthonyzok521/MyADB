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
print('Coloque el nombre del archivo que desea pasar a la ruta de su telefono: '+B)
nombre = input('> ')
os.system('adb.exe push \"'+nombre+'\" /sdcard/')
print('Listo')

