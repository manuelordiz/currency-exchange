import requests
import tkinter as tk
from tkinter  import ttk, messagebox

endpoints = { 
            'dolar_oficial' : 'https://dolarapi.com/v1/dolares/oficial',
            'dolar_blue' : 'https://dolarapi.com/v1/dolares/blue',
            'dolar_tarjeta' : 'https://dolarapi.com/v1/dolares/tarjeta',
            'dolar_crypto' : 'https://dolarapi.com/v1/dolares/cripto',
            'euro' : 'https://dolarapi.com/v1/cotizaciones/eur',
            'real_brasil' : 'https://dolarapi.com/v1/cotizaciones/brl'

        }

def get_valor(url, key='venta'):
    try:
        res = requests.get(url)
        res.raise_for_status()
        datos = res.json()
        valor = datos.get(key)
    
        if valor is None:
            messagebox.showerror("Error", f"No se encotro el valor'{key} en el JSON")
            return None
        return valor
    
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", f"No se puede conectar a la api {url}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")
        return None
    
def convertidor():
    try:
        monto = float(monto_entry.get())
        moneda_seleccionada = moneda_combobox.get()
        
        if not moneda_seleccionada:
            messagebox.showerror("Error", "Por favor seleccione una moneda")
            return

        url = endpoints.get(moneda_seleccionada)
        tasa = get_valor(url, key='venta')
        if tasa is None:
            return
        
        valor_convertido = monto * tasa
        resultado_label.config(text=f"{monto:.2f} USD equivale a {valor_convertido:.2f} en {moneda_seleccionada} (tasa: {tasa}).")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresar un numero valido en el campo de cantidad")
        
        
root = tk.Tk()
root.title("Conversor de Monedas")
root.geometry("250x250")

monto_label = tk.Label(root, text="Cantidad en USD: ")
monto_label.pack()
monto_entry = tk.Entry(root, font=("Times New Roman", 12))
monto_entry.pack()

moneda_label = tk.Label(root, text="Selecciona la moneda:")
moneda_label.pack()
moneda_combobox = ttk.Combobox(root, values=list(endpoints.keys()), font=("Arial", 12))
moneda_combobox.pack(pady=5)

convert_button = tk.Button(root, text="Convertir", command=convertidor, font=("Arial", 12), bg="Green", fg="white")
convert_button.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
resultado_label.pack(pady=10)

root.mainloop()