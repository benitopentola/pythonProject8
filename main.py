import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from langdetect import detect, LangDetectException
import pyperclip

def es_ingles(texto):
    try:
        return detect(texto) == 'en'
    except LangDetectException:
        return False

def procesar():
    texto_entrada = entrada_texto.get("1.0", tk.END)
    lineas_procesadas = []
    for linea in texto_entrada.splitlines():
        if es_ingles(linea):
            lineas_procesadas.append(linea)
        else:
            # Opcional: incluir algo para marcar líneas no inglesas o simplemente omitirlas
            continue
    texto_salida = '\n'.join(lineas_procesadas)
    salida_texto.delete("1.0", tk.END)
    salida_texto.insert("1.0", texto_salida)

def copiar_todo():
    texto = salida_texto.get("1.0", tk.END)
    pyperclip.copy(texto)

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Procesador de Texto")

# Creación de los widgets
entrada_texto = ScrolledText(ventana, height=10, width=50)
entrada_texto.pack(pady=10)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
boton_procesar.pack(pady=5)

salida_texto = ScrolledText(ventana, height=10, width=50)
salida_texto.pack(pady=10)

boton_copiar = tk.Button(ventana, text="Copiar Todo", command=copiar_todo)
boton_copiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
