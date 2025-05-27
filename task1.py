import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_temperature():
    try:
        temp = float(entry.get())
        option = conversion_var.get()
        result = 0

        if option == "Celsius to Fahrenheit":
            result = (temp * 9 / 5) + 32
            result_label.config(text=f"Result: {result:.2f} °F")
        elif option == "Celsius to Kelvin":
            result = temp + 273.15
            result_label.config(text=f"Result: {result:.2f} K")
        elif option == "Fahrenheit to Celsius":
            result = (temp - 32) * 5 / 9
            result_label.config(text=f"Result: {result:.2f} °C")
        elif option == "Fahrenheit to Kelvin":
            result = (temp - 32) * 5 / 9 + 273.15
            result_label.config(text=f"Result: {result:.2f} K")
        elif option == "Kelvin to Celsius":
            result = temp - 273.15
            result_label.config(text=f"Result: {result:.2f} °C")
        elif option == "Kelvin to Fahrenheit":
            result = (temp - 273.15) * 9 / 5 + 32
            result_label.config(text=f"Result: {result:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x200")

# Input Field
tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

# Dropdown Menu
options = [
    "Celsius to Fahrenheit",
    "Celsius to Kelvin",
    "Fahrenheit to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Celsius",
    "Kelvin to Fahrenheit"
]
conversion_var = tk.StringVar(value=options[0])
ttk.Combobox(root, textvariable=conversion_var, values=options, state="readonly").pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", command=convert_temperature).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=5)

# Run the GUI loop
root.mainloop()
