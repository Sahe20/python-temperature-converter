import tkinter as tk

def converter_celsius_to_fahrenheit(): 
    try: 
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit}\u00b0C")
    except ValueError:
        label_result.config(text="Invalid input, # only \U0001F609")

def convert_fahrenheit_to_celsius():
    try: 
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9 
        label_result.config(text=f"{celsius}\u00b0C") 
    except ValueError:
        label_result.config(text="Invalid input, # only \U0001F609")


root = tk.Tk()
root.title("Temperature Converter") 

label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0)
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1)
button_celsius = tk.Button(root, text="Convert to Fahrenheit", command=converter_celsius_to_fahrenheit)
button_celsius.grid(row=0, column=2)

label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(row=1, column=0)
entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=1, column=1)
button_fahrenheit = tk.Button(root, text="Convert to Celsius", command=convert_fahrenheit_to_celsius)
button_fahrenheit.grid(row=1, column=2)

