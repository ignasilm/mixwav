# mixwav
 Fusion varios wav en uno solo

---

## Descripción

El motivo de esta herramienta es para fusionar/mezclar varios ficheros wav en uno solo. La necesidad surgió al usar la IA [Demucs](https://github.com/facebookresearch/demucs), que separa en varios ficheros wav la voz y ciertos  instrumentos, a partir de un fichero de audio. En mi caso la utilicé para eliminar el sonido del viento de una grabacion de video. Como Demucs separa una pista con la voz, me permitía recuperar por separado la voz del resto de sonidos. Pero como casi todo el sonido del viento lo enviaba a la misma pista, quise volver a unir el resto de pistas con la de la voz para tener algo de sonido ambiente pero sin el ruido molesto del viento. Así que necesitaba volver a fusionar otra vez los ficheros wav que habia generado Demucs sin el fichero del viento.

---

## Instalación en local

1. Instalar Python 3.8+ desde [python.org](https://www.python.org/downloads/)

2. crear directorio:

	`cd c:\Dev\Python\workspace`
	
	`mkdir mixwav`
	
	`cd mixwav`
	
3. crear entorno virtual
	
	`pip install virtualenv`
	
	`virtualenv env`
	
4. Activar el entorno virtual
	desde C:\Dev\Python\workspace\mixwav ejecutar:
	
	`c:/Dev/Python/workspace/mixwav/env/Scripts/activate.ps1`
	
5. Copiar codigo de mixwav en C:\Dev\Python\workspace\mixwav

6. instalar librerias

	`pip install -r .\requirements.txt`
	
7. Ejecutar aplicacion

	`c:/Dev/Python/workspace/mixwav/env/Scripts/python.exe c:/Dev/Python/workspace/mixwav/mixwav.py`


## Uso
~~~
usage: mixwav.py [-h] -i INPUT [-o OUTPUT]

Utilidad para fusionar varios ficheros wav en un solo archivo.

optional arguments:
  -h, --help            Muestra esta información y termina la ejecución.
  -i INPUT, --input INPUT
                        Path que contiene los wav que hay que fusionar
  -o OUTPUT, --output OUTPUT
                        Nombre del fichero de salida. Por defecto será mixwav.wav

Ejemplo de uso:
    Para fusionar todos los wav dentro de un path e indicar el fichero de salida:
                    mixwav -i "C:\videos\Viaje Alicante\audios_corte_1" -o "C:\videos\Viaje Alicante\GOPRO\voz_corte_1.wav"
~~~