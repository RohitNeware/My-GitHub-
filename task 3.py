# -----------------TASK NO 3-----------------#
# ---------------PASSWORD GENERATOR----------------#

import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6.")
            return

        
        use_upper = upper_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        # (lowercase letters)
        all_characters = string.ascii_lowercase
        
        
        if use_upper:
            all_characters += string.ascii_uppercase
        if use_digits:
            all_characters += string.digits
        if use_symbols:
            all_characters += string.punctuation

        password = ''.join(random.choices(all_characters, k=length))
        
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")

length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

upper_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_checkbox = tk.Checkbutton(window, text="Include Uppercase Letters", variable=upper_var)
upper_checkbox.pack(pady=5)

digits_checkbox = tk.Checkbutton(window, text="Include Digits", variable=digits_var)
digits_checkbox.pack(pady=5)

symbols_checkbox = tk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

password_entry = tk.Entry(window, width=40)
password_entry.pack(pady=10)

window.mainloop()