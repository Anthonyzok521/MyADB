import os
telefono = str(os.system('adb.exe device'))
os.system('clear')
print('''\033[31m
         _     _  _  _ \033[32m    _________________   _______
        \033[31m| \   / |\ \/ /\033[32m   |  ___  ||   __ \ \ |  _  \ \ 
        \033[31m|  \_/  | \  /\033[32m    | |   | ||  |  | | ||_|_|_/ /
        \033[31m| |\_/| | / / \033[32m    | |___| ||  |__| | ||  _  \ \ 
        \033[31m|_|   |_|/_/  \033[32m    |_|   |_||______/_/ |_|_|_/_/
''')

print(telefono)
print('Coloque el nombre del archivo que desea pasar a la ruta de su : ')
print('\033[0m')
nombre = input()
os.system('adb.exe push \"'+nombre+'\" /sdcard/')
print('Listo')

