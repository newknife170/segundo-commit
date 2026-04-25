'''
Crear los widgets de mi ventana principal
'''
from .windows import ttk,tk,PRIMARY,SUCCESS,DANGER
from pytubefix import YouTube

def crear_widgets(win: tk.Tk) -> None:
    def load_stream() -> None:
        url = url_var.get()
        
        if not url:
            status_var.set('Por favor ingresa un enlace valido')
            return
        
        list_box.delete(0, tk.END)
        
        try:
            youtube = YouTube(url)
            streams = youtube.streams.filter(
                progressive=True,
                file_extension='mp4').order_by('resolution').desc()
            
            for stream in streams:
                datos_stream: str = (
                    f'Itag: {stream.itag}, '
                    f'Resolución: {stream.resolution},'
                    f'FPS: {stream.fps}, '
                    f'Tipo: {stream.mime_type}, '
                    f'Tamaño: {round(stream.filesize / 1024 / 1024, 2)} MB'
        )
                
                list_box.insert(tk.END, datos_stream)
        except Exception as ex:
            status_var.set(f'Error al obtener los canales {ex}')
            
    def descargar_stream() -> None:
        pass
        
    label = ttk.Label(win, text="ingresa el enlace del video de yutu", font=40)
    label.pack(pady=25)
    
    url_var = ttk.StringVar()
    entrada_url = ttk.Entry(win, textvariable=url_var , width=80)
    entrada_url.pack(pady=5)
    
    btn_load = ttk.Button(
        win,
        text='Mostrar resoluciones',
        style=PRIMARY,
        command=load_stream
    )
    
    btn_load.pack(pady=10)
    
    list_box = tk.Listbox(
        win,
        height=10,
        width=90,
    )
    
    list_box.pack(pady=10)
    
    btn_download = ttk.Button(
        win,
        text='Descargar video',
        style=SUCCESS   ,
    )
    
    btn_download.pack(pady=10)
    
    status_var = ttk.StringVar(value='Estado: en espera...')
    label_status = ttk.Label(win, textvariable=status_var, font=80)
    label_status.pack(pady=10)
    