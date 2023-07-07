# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def calcular():
    try:
        valor_a = float(entry_valor_a.get())
        valor_b = float(entry_valor_b.get())
        ganancia_percent = float(entry_ganancia.get())

        tasa_bruta = valor_a / valor_b
        tasa_neta = tasa_bruta - (tasa_bruta * ganancia_percent / 100)
        ganancia_bruta = tasa_bruta * ganancia_percent / 100

        label_tasa_bruta["text"] = f"Tasa Bruta: {tasa_bruta:.3f}"
        label_tasa_neta["text"] = f"Tasa Neta: {tasa_neta:.3f}"
        label_ganancia["text"] = f"Ganancia: {ganancia_bruta:.3f}"

        button_calcular_monto["state"] = "normal"
        button_imprimir_tasa["state"] = "normal"

    except ValueError:
        label_resultado["text"] = "Por favor, ingresa números válidos."


def calcular_monto():
    try:
        cantidad = float(entry_cantidad.get())
        tasa_neta_str = label_tasa_neta["text"].replace("Tasa Neta: ", "")
        tasa_neta = float(tasa_neta_str.split()[0])
        monto_neto = cantidad * tasa_neta
        label_monto_neto["text"] = f"Monto Neto en {combo_divisa.get()}: {monto_neto:.3f}"
    except ValueError:
        label_monto_neto["text"] = "Ingrese un valor válido."


def imprimir_tasa():
    if label_tasa_neta["text"]:
        bg_path = "C:/Users/AbrahamFerrer/Documents/finango/remesas/background.png"
        try:
            background = Image.open(bg_path)
        except:
            print(f"Error: no se puede abrir la imagen en {bg_path}")
            return
        
        d = ImageDraw.Draw(background)

        # Añadir texto al centro
        width, height = background.size
        text = label_tasa_neta["text"] + " VES"
        font = ImageFont.truetype("arialbd.ttf", 90)
        text_width, text_height = d.textsize(text, font=font)
        position = ((width - text_width) / 2, ((height - text_height) / 2) - 100)
        d.text(position, text, (255, 255, 255), font=font)

        # Fecha en la esquina inferior derecha
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        d.text((100, height - 100), f"Tasa del día {formatted_date}", (255, 255, 255), font=ImageFont.truetype("arialbd.ttf", 20))

        # Guardar la imagen con un nombre que incluya la fecha
        background.save(f"tasadeldia{formatted_date}.png")
        background.show()
    else:
        print("No hay datos para imprimir la tasa.")


# Crear la ventana de la aplicación
app = tk.Tk()
app.title("Calculadora de Cambio")
app.geometry("500x450")

# Estilos
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Arial", 10), padding=5)
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", font=("Arial", 10), padding=5)

# Widgets y etiquetas
label_valor_a = ttk.Label(app, text="Valor A (VES):")
label_valor_a.pack()

entry_valor_a = ttk.Entry(app)
entry_valor_a.pack()

label_valor_b = ttk.Label(app, text="Valor B (ARS/CLP/COP):")
label_valor_b.pack()

entry_valor_b = ttk.Entry(app)
entry_valor_b.pack()

label_ganancia_text = ttk.Label(app, text="Ganancia (%):")
label_ganancia_text.pack()

entry_ganancia = ttk.Entry(app)
entry_ganancia.pack()

label_divisa_text = ttk.Label(app, text="Divisa de ganancia:")
label_divisa_text.pack()

divisas = ["ARS", "CLP", "COP", "VES"]
combo_divisa = ttk.Combobox(app, values=divisas)
combo_divisa.pack()

button_calcular = ttk.Button(app, text="Calcular", command=calcular)
button_calcular.pack()

label_tasa_bruta = ttk.Label(app, text="")
label_tasa_bruta.pack()

label_tasa_neta = ttk.Label(app, text="")
label_tasa_neta.pack()

label_ganancia = ttk.Label(app, text="")
label_ganancia.pack()

label_cantidad_text = ttk.Label(app, text="Cantidad a intercambiar:")
label_cantidad_text.pack()

entry_cantidad = ttk.Entry(app)
entry_cantidad.pack()

button_calcular_monto = ttk.Button(app, text="Calcular Monto", command=calcular_monto, state='disabled')
button_calcular_monto.pack()

label_monto_neto = ttk.Label(app, text="")
label_monto_neto.pack()

button_imprimir_tasa = ttk.Button(app, text="Imprimir Tasa", command=imprimir_tasa, state='disabled')
button_imprimir_tasa.pack()

# Ejecutar la aplicación
app.mainloop()
