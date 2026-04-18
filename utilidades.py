from typing import Callable
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def linea(largo: int) -> None:
  print('═' *largo)


def titulo(titylo: str, largo: int) -> None:
  linea(largo)
  print(titylo.center(largo).upper())
  linea(largo)


Number = int | float
def leernum (msj: str, fn: Callable) -> Number:
  numero: int = 0
  while True:
    try:
      numero = fn(input(msj + ': '))
      return numero
    except ValueError:
      print("debe escribir un numero...")
      
      
def leertexto(msj: str, variable: str) -> str:
  while True:
      txt = input(f'{msj}: ')
      if txt.strip():
        return txt
      else:
        print(f'No se encuentra el {variable} por favor ingresalo')
                        
        
def descargar_video(enlace: str) -> None:
    youtube = YouTube(enlace, on_progress_callback=on_progress)
    
    streams = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

    titulo(f'Titulo del video: {youtube.title}',70)
    titulo(f'Autor del video: {youtube.author}',70)
    titulo(f'Fecha de publicacion del video: {youtube.publish_date}',70)
    
    titulo('Canales disponibles: ',70)
    
    for stream in streams:
        datos_stream: str = (
            f'Itag: {stream.itag}, '
            f'Resolución: {stream.resolution},'
            f'FPS: {stream.fps}, '
            f'Tipo: {stream.mime_type}, '
            f'Tamaño: {round(stream.filesize / 1024 / 1024, 2)} MB'
        )
        
        print(datos_stream)
        linea(70)
    itag_video = input('Ingresa el Itag del stream a descargar: ')
    linea(70)
    
    stream = youtube.streams.get_by_itag(itag_video)
    
    if stream is None:
        print('No se a encontrado el stream para descargar... ')
        return
    
    try:
        ruta_descarga: str = './descargados/'
        '''
        Crea la carpeta descargados si no existe.
        El parametro exist_ok=True evita un error si la carpeta ya esta creada
        '''
        os.makedirs(ruta_descarga, exist_ok=True)
        stream.download(ruta_descarga)
        print('La descarga finalizo exitosamente')
        linea(70)
        
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
        