import tkinter as tk
import math

def calculate_capacitance():
    f = float(frequency_entry.get())
    V = float(voltage_entry.get())
    I = float(current_entry.get())

    C = I / (2 * math.pi * f * V)

    capacitance_label.config(text="Capacitância: " + format_capacitance(C))

def calculate_capacitance_alternate():
    q = float(charge_entry.get())
    V = float(voltage_entry_alternate.get())

    C = q / V

    capacitance_label_alternate.config(text="Capacitância: " + format_capacitance(C))

def format_capacitance(C):
    if C >= 1:
        return str(C) + " F"
    elif C >= 0.001:
        return str(C * 1000) + " mF"
    elif C >= 0.000001:
        return str(C * 1000000) + " uF"
    elif C >= 0.000000001:
        return str(C * 1000000000) + " nF"
    else:
        return str(C * 1000000000000) + " pF"

root = tk.Tk()
root.title("Calculadora de Capacitância")

frequency_label = tk.Label(root, text="Frequência (Hz):")
frequency_label.grid(row=0, column=0)

frequency_entry = tk.Entry(root)
frequency_entry.grid(row=0, column=1)

voltage_label = tk.Label(root, text="Voltagem (V):")
voltage_label.grid(row=1, column=0)

voltage_entry = tk.Entry(root)
voltage_entry.grid(row=1, column=1)

current_label = tk.Label(root, text="Corrente (A):")
current_label.grid(row=2, column=0)

current_entry = tk.Entry(root)
current_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calcular", command=calculate_capacitance)
calculate_button.grid(row=3, column=0)

capacitance_label = tk.Label(root)
capacitance_label.grid(row=3, column=1)

charge_label = tk.Label(root, text="Carga (C):")
charge_label.grid(row=4, column=0)

charge_entry = tk.Entry(root)
charge_entry.grid(row=4, column=1)

voltage_label_alternate = tk.Label(root, text="Voltagem (V):")
voltage_label_alternate.grid(row=5, column=0)

voltage_entry_alternate = tk.Entry(root)
voltage_entry_alternate.grid(row=5, column=1)

calculate_button_alternate = tk.Button(root, text="Calcular", command=calculate_capacitance_alternate)
calculate_button_alternate.grid(row=6, column=0)

capacitance_label_alternate = tk.Label(root)
capacitance_label_alternate.grid(row=6, column=1)

root.mainloop()