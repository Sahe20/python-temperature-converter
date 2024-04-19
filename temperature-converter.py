import tkinter as tk

def converter_celsius_to_fahrenheit(): 
    try: 
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit}\u00b0C")
    except ValueError:
        label_result.config(text="Invalid input, # only \U0001F609")
