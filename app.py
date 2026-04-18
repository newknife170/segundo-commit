'''
Programa para descargar videos de youtube
'''
from pytubefix import YouTube
from pytubefix.cli import on_progress
from utilidades import linea,leertexto, descargar_video

def main() -> None:
    linea(90)
    enlace = leertexto('Ingresa el enlace del video de youtube','enlace')
    
    descargar_video(enlace)
    

if __name__ == '__main__':
    main()
   