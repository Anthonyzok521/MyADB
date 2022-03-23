import os
import subprocess
from colorama import init, Fore, Back, Style, Cursor
init()
FA = Back.BLUE
print(FA)
os.system('cls')
R = Fore.RED
V = Fore.GREEN
B = Fore.WHITE
C = Fore.CYAN
FR = Back.RED
FV = Back.GREEN
n_lista = list()
nombre = ''
def Menu():
	print(Style.BRIGHT+R+'''                                                                 
          '''+R+'''____'''+V+'''                                                    
        '''+R+''',\'  , `.'''+V+'''             ,---,           ,---,        ,---,.  
     '''+R+''',-+-,.\' _ | '''+V+'''           \'  .\' \        .\'  .\' `\    ,\'  .\'  \ 
  '''+R+''',-+-. ;   , || '''+V+'''          /  ;    \'.    ,---.\'     \ ,---.\' .\' | 
 '''+R+''',--.\'|\'   |  ;| '''+V+'''         :  :       \   |   |  .`\  ||   |  |: | 
'''+R+'''|   |  ,\', |  \':     .--, '''+V+''':  |   /\   \  :   : |  \'  |:   :  :  / 
'''+R+'''|   | /  | |  ||   /_ ./| '''+V+'''|  :  \' ;.   : |   \' \'  ;  ::   |    ;  
'''+R+'''|   | :  | :  |,, \' , \' : '''+V+'''|  |  ;/  \   \'|   | ;  .  ||   :     \ 
'''+R+''';   . |  ; |--\'/___/ \: | '''+V+''':  :  | \  \ ,\'|   | :  |  \'|   |   . | 
'''+R+'''|   : |  | ,    .  \  \' | '''+V+'''|  |  \'  \'--\'  \'   : | /  ; \'   :  \'; | 
'''+R+'''|   : \'  |/      \  ;   : '''+V+'''|  :  :        |   | \'` ,/  |   |  | ;  
'''+R+''';   | |`-\'        \  \  ; '''+V+'''|  | ,\'        ;   :  .\'    |   :   /   
'''+R+'''|   ;/             :  \  \ '''+V+'''`--\'          |   ,.\'      |   | ,\'    
'''+R+'''\'---\'               \  \' ;'''+V+'''               \'---\'        `----\'      
'''+R+'''                     `--`  '''+V+'''                                       
'''

		+V+'''['''+C+'''1'''+V+''']'''+B+'''-Enviar archivo al teléfono
'''

		+V+'''['''+C+'''2'''+V+''']'''+B+'''-Enviar archivo al PC
'''

		+V+'''['''+C+'''3'''+V+''']'''+B+'''-Respaldar todos los archivos del teléfono
'''

		+V+'''['''+C+'''4'''+V+''']'''+B+'''-Apagar el teléfono
'''

		+V+'''['''+C+'''5'''+V+''']'''+B+'''-Reinicar el teléfono
'''

		+V+'''['''+C+'''6'''+V+''']'''+B+'''-Reiniciar en modo Fastboot
'''

		+V+'''['''+C+'''7'''+V+''']'''+B+'''-Reiniciar en modo Recovery
'''

		+V+'''['''+C+'''8'''+V+''']'''+B+'''-Salir del Programa.
''')
	try:
		s = subprocess.run(['adb.exe','devices'], stdout=subprocess.PIPE)
		M = s.stdout
		m = str(M.decode('utf-8'))
		movil = []
		movil = m.split()

		print('Conexión establecido con: '+FV+movil[4]+FA)
		print()
	except:
		print(FR+'No está conectado'+FA)
		print()

def Opciones():
	intentos=4
	while True:
		Menu()
		opcion=int(input('Ingrese una opcion del Menú: '))
		print('')
		if opcion>0 and opcion<=8:

			if opcion==1:
				print('Coloque el nombre del archivo que desea pasar a la ruta de su teléfono: '+B)
				nombre = input('> ')
				s = subprocess.run(['adb.exe','push',nombre,'/sdcard/'],stdout=subprocess.PIPE)
				p = s.stdout
				P = str(p.decode('utf-8'))
				push = []
				push = P.split()

				if push[2] == 'file':
					print()
					print(FV+P)
					input()
					print(FA)
					os.system('cls')
				elif push[2] == 'cannot':
					print()
					print(FR+'Archivo no encontrado.')
					input()
					print(FA)
					os.system('cls')
				elif push[2] == 'failed':
					print()
					print(FR+'Error.Telefono no está conectado.')
					input()
					print(FA)
					os.system('cls')

			elif opcion==2:
				os.system('mkdir MyADBFiles')
				print('Coloque el nombre del archivo que desea pasar a la ruta de su computadora: '+B)
				nombre = input('> ')
				s = subprocess.run(['adb.exe','pull','/sdcard/'+nombre,'MyADBFiles'],stdout=subprocess.PIPE)
				p = s.stdout
				P = str(p.decode('utf-8'))
				pull = []
				pull = P.split()
				print()
				print('Buscando archivo')
				if pull[2] == 'file':
					print()
					print(FV+'Envío completo. El '+nombre+' está en la carpeta MyADBFiles')
					input()
					print(FA)
					os.system('cls')

				elif pull[2] == 'failed':
					print()
					print(FR+'Archivo no encontrado.')
					input()
					print(FA)
					os.system('cls')

			elif opcion==3:
				os.system('mkdir Respaldo')
				print('Si desea cancelar la operación haga la combinación Ctrl + C '+B)
				nombre = "."
				s = subprocess.run(['adb.exe','pull','/sdcard/',nombre,'Respaldo'],stdout=subprocess.PIPE)
				r = s.stdout
				Res = str(p.decode('utf-8'))
				res = []
				res = P.split()
				print()
				print('Iniciando Respaldo.')
				print(Res)
				if push[2] == 'file':
					print()
					print(FV+'Archivos guardados!')
					input()
					print(FA)
					os.system('cls')

				elif push[2] == 'failed':
					print()
					print(FR+'Teléfono no conectado.')
					input()
					print(FA)
					os.system('cls')

				input()
				print(FA)
				os.system('cls')

			elif opcion==4:

				s = subprocess.run(['adb.exe','shell','reboot','-p'],stdout=subprocess.PIPE)
				a = s.stdout
				Apagar = str(a.decode('utf-8'))
				print()
				if Apagar == 'error: no devices/emulators found':
					print(FR+'Teléfono no conectado.')
				else:
					print(FV+'Su teléfono se apagó correctamente.')

				input()
				print(FA)
				os.system('cls')

			elif opcion==5:
				s = subprocess.run(['adb.exe','shell','reboot'],stdout=subprocess.PIPE)
				r = s.stdout
				Reiniciar = str(r.decode('utf-8'))
				print()
				if Apagar == 'error: no devices/emulators found':
					print(FR+'Teléfono no conectado.')
				else:
					print(FV+'Su teléfono se reinició correctamente.')

				input()
				print(FA)
				os.system('cls')

			elif opcion==6:
				s = subprocess.run(['adb.exe','shell','reboot','bootloader'],stdout=subprocess.PIPE)
				f = s.stdout
				Fastboot = str(f.decode('utf-8'))
				print()
				if Apagar == 'error: no devices/emulators found':
					print(FR+'Teléfono no conectado.')
				else:
					print(FV+'Su teléfono se reinició en modo fastboot correctamente.')

				input()
				print(FA)
				os.system('cls')

			elif opcion==7:
				s = subprocess.run(['adb.exe','shell','reboot','recovery'],stdout=subprocess.PIPE)
				r = s.stdout
				Recovery = str(r.decode('utf-8'))
				print()
				if Apagar == 'error: no devices/emulators found':
					print(FR+'Teléfono no conectado.')
				else:
					print(FV+'Su teléfono se reinició en modo recovery correctamente.')

				input()
				print(FA)
				os.system('cls')

			elif opcion==8:
				opcion=input('¿Seguro que desea salir, ingrese Yes o No: ').lower()
				if opcion=='yes' or opcion=='y':
					print('Hasta pronto. ')
					break
				elif opcion=='no' or opcion=='n':
					pass
				else:
					print('Usted marcó un argumento incorrecto. ')

		else:
			print('Digite una opción valida')
			intentos-=1
			print(f'Le quedan {intentos} intento(s).')
			input('Presiona Enter para reintentar...')
			print(FA)
			os.system('cls')
			if intentos==0:
				print('Lo sentimos, usted excedió el limite de intentos.')
				break

		
Opciones()



