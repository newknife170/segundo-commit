'''
Programa para descargar videos youtube - GUI
'''

from paquetededoritos.widgets import crear_widgets
import os
import threading
from pytubefix import YouTube
from paquetededoritos.windows import ventanaprincipal

def main() -> None:
    config = {
        'tema': 'morph',
        'titulo': 'Aplicacion para descargar videos del yutu',
        'tamaño': '800x600',
    }
    win = ventanaprincipal(config)
    crear_widgets(win)
    win.mainloop()

if __name__ == '__main__':
    main()