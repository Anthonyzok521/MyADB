import os
try:
    os.system('python main.py')
except:
    print('Hubo un problema al abrir el programa, verifique que los archivos esten completos.')
input('Presione una tecla para salir...')
os.system('exit')
