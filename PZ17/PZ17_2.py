#Разработать программу с применением пакета tk, взяв в качестве условия эту задачу: "Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_segments():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())

        if a <= 0 or b <= 0:
            messagebox.showerror("Ошибка", "A и B должны быть положительными числами.")
            return
        if a <= b:
            messagebox.showerror("Ошибка", "A должно быть больше B.")
            return

        count = a // b
        result_label.config(text=f"Количество отрезков B в A: {count}")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целые числа.")


root = tk.Tk()
root.title("Расчет отрезков")

a_label = ttk.Label(root, text="Введите длину отрезка A:")
a_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

a_entry = ttk.Entry(root)
a_entry.grid(row=0, column=1, padx=10, pady=5)

b_label = ttk.Label(root, text="Введите длину отрезка B:")
b_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

b_entry = ttk.Entry(root)
b_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = ttk.Button(root, text="Рассчитать", command=calculate_segments)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)


root.mainloop()
