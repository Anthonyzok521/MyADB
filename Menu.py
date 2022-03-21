import os
import subprocess
from colorama import init, Fore, Back, Style
from subprocess import Popen, PIPE, STDOUT
init()
os.system('cls')
R = Fore.RED
V = Fore.GREEN
B = Fore.WHITE

def Menu():
	print(R+'''
		         _     _  _  _ '''+V+'''    _________________   _______
        '''+R+'''| \   / |\ \/ /'''+V+'''   |  ___  ||   __ \ \ |  _  \ \ 
        '''+R+'''|  \_/  | \  /'''+V+'''    | |   | ||  |  | | ||_|_|_/ /
        '''+R+'''| |\_/| | / / '''+V+'''    | |___| ||  |__| | ||  _  \ \ 
        '''+R+'''|_|   |_|/_/  '''+V+'''    |_|   |_||______/_/ |_|_|_/_/

		[1]-Enviar archivo al teléfono

		[2]-Enviar archivo al PC

		[3]-Apagar el teléfono

		[4]-Reinicar el teléfono

		[5]-Reiniciar en modo Fastboot

		[6]-Reiniciar en modo Recovery

		[7]-Salir del Programa.''')

def Opciones():
	Menu()
	intentos=4
	while True:
		Menu()
		opcion=int(input('Ingrese una opcion del Menú: '))
		if opcion>0 and opcion<=7:
			if opcion==1:
				print(Style.DIM+'Coloque el nombre del archivo que desea pasar a la ruta de su telefono: '+B)
				nombre = input('> ')
				os.system('adb.exe push \"'+nombre+'\" /sdcard/')
			elif opcion==2:
				os.system('mkdir MyADB')
				print('Carpeta creada correctamente.')
				print('')
				print(Style.DIM+'Coloque el nombre del archivo que desea pasar a la ruta de su computadora: '+B)
				nombre1 = input('> ')
				os.system('adb.exe pull /sdcard/\"'+nombre+'\" MyADB')
			elif opcion==3:
				os.system('adb.exe shell reboot -p')
				print('Su telefono se apago correctamente.')
			elif opcion==4:
				os.system('adb.exe reboot')
				print('Su telefono se reinicio correctamente')
			elif opcion==5:
				os.system('adb.exe reboot bootloader')
				print('Su telefono se ingreso en Fastboot correctamente.')
			elif opcion==6:
				os.system('adb.exe reboot recovery')
				print('Usted ingreso al modo recovery correctamente.')
			elif opcion==7:
				opcion=input('¿Seguro que desea salir, ingrese Yes o No: ').lower()
				if opcion=='yes':
					print('Hasta pronto. ')
					break
				elif opcion=='no':
					pass
				else:
					print('Usted marco un argumento incorrecto. ')
		else:
			print('Digite una opcion valida')
			intentos-=1
			print(f'Le quedan {intentos} intento.')
			if intentos==0:
				print('Lo sentimos, usted excedio el limite de intentos.')
				break

		
Opciones()
