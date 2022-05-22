from pydub import AudioSegment
import argparse
import textwrap
from os import chdir
import glob

print(' ')
ap = argparse.ArgumentParser(add_help=False, 
                             description='Utilidad para fusionar varios ficheros wav en un solo archivo.',
                             formatter_class=argparse.RawDescriptionHelpFormatter,
                             epilog=textwrap.dedent('''\
                                Ejemplo de uso:
                                    Para fusionar todos los wav dentro de un path e indicar el fichero de salida: 
                                                    mixwav -i "C:\\videos\\Viaje Alicante\\audios_corte_1" -o "C:\\videos\\Viaje Alicante\\GOPRO\\voz_corte_1.wav"
                                    ''' ))
ap.add_argument('-h', '--help', action='help', help='Muestra esta información y termina la ejecución.')
ap.add_argument('-i', '--input', required=True, help='Path que contiene los wav que hay que fusionar')
ap.add_argument('-o', '--output', required=False, help='Nombre del fichero de salida. Por defecto será mixwav.wav')
args = vars(ap.parse_args())



if args['input'] is not None:
    path = args['input']

salida = './mixwav.wav'
if args['output'] is not None:
    salida = args['output']


chdir(path)

#Recuperamos los ficheros de la carpeta que cumplen el patron
lista_ficheros = glob.glob('*.wav')

if len(lista_ficheros) < 2:
    print('No hay suficientes ficheros *.wav para fusionar.')
else:
    #Recuperamos un fichero como inicial al que ir añadiendo el resto de pistas
    print('Fichero inicial:', lista_ficheros[0])
    combined = AudioSegment.from_file(lista_ficheros[0], format='wav')
    print('     Número de canales:', combined.channels)
    print('     Bits por Sample:', combined.sample_width * 8)
    print('     Frame rate:', combined.frame_rate)
    print('     Duración (segundos):', combined.duration_seconds)
    print(' ')
    
    #Recorremos el resto de ficheros 
    for file_name in lista_ficheros[1:]:
        print('Procesando el fichero:', file_name)
        mix = AudioSegment.from_file(file_name, format='wav')
        combined = combined.overlay(mix)

combined.export(salida, format='wav')
print(' ')
print('El fichero final se ha generado en:', salida)