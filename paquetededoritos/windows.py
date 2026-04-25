'''
Clase para crear una ventana GUI
'''

import tkinter as tk
from typing import Any, Tuple, Dict
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SUCCESS, DANGER
#tema puede ser litera,minty,lumen,sandstone,yeti,pulse,united,morph,journal,darkly,superhero,solar,cyborg,vapor,simplex,cerculean

class ventanaprincipal(ttk.Window):
    def __init__(self,config: Dict[str, str]) -> None:
        super().__init__(themename=config['tema']) 
        self.title(config['titulo'])
        self.geometry(config['tamaño'] if config['tamaño'] else '640x480')
        self.position_center()


