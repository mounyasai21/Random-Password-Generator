
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import string
import pyperclip
from datetime import datetime

# Generate password logic
def generate_password():
    try:
        length = int(length_var.get())
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        exclude_similar = exclude_var.get()

        if not (use_upper or use_lower or use_digits or use_symbols):
            messagebox.showwarning("Input Error", "Please select at least one character set.")
            return

        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_symbols:
            chars += string.punctuation

        if exclude_similar:
            for c in 'Il1O0':
                chars = chars.replace(c, '')

        # Add exclude characters from entry
        excluded_chars = exclude_entry.get()
        for c in excluded_chars:
            chars = chars.replace(c, '')

        if len(chars) == 0:
            messagebox.showerror("Error", "Character set is empty. Please adjust your selections.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)
        update_strength(password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")

# Copy to clipboard
def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Save password to a file
def save_password():
    pwd = password_var.get()
    if not pwd:
        messagebox.showwarning("No Password", "Please generate a password first!")
        return

    # Ask user where to save (optional, or use default)
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Password As"
    )
    if not file_path:
        return  # User cancelled

    try:
        with open(file_path, "a") as file:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{now} - {pwd}\n")
        messagebox.showinfo("Saved", f"Password saved to:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save password:\n{e}")

# Update password strength display
def update_strength(password):
    length = len(password)
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if length >= 12: score += 1

    strength_text = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength_colors = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#27ae60"]
    label_strength.config(text=f"Strength: {strength_text[score-1]}", fg=strength_colors[score-1])

# GUI Setup
root = tk.Tk()
root.title("🔐 Secure Password Generator")
root.geometry("520x600")  # Adjust height for new button
root.configure(bg="#1e272e")

# Title
tk.Label(root, text="Advanced Password Generator", font=("Segoe UI", 20, "bold"), bg="#1e272e", fg="#f5f6fa").pack(pady=20)

# Frame
frame = tk.Frame(root, bg="#f5f6fa", bd=5, relief="groove")
frame.pack(padx=20, pady=10, fill="both", expand=True)

# Password Display
password_var = tk.StringVar()
tk.Entry(frame, textvariable=password_var, font=("Consolas", 16), justify="center", bd=2, relief="sunken").pack(pady=15)

# Strength Label
label_strength = tk.Label(frame, text="Strength: ", font=("Segoe UI", 12, "bold"), bg="#f5f6fa")
label_strength.pack(pady=5)

# Options
length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
exclude_var = tk.BooleanVar()

tk.Label(frame, text="Password Length:", font=("Segoe UI", 12), bg="#f5f6fa").pack()
tk.Entry(frame, textvariable=length_var, font=("Segoe UI", 12), justify="center", width=5).pack(pady=5)

tk.Checkbutton(frame, text="Include Uppercase Letters", variable=upper_var, bg="#f5f6fa", font=("Segoe UI", 11)).pack(anchor="w", padx=40)
tk.Checkbutton(frame, text="Include Lowercase Letters", variable=lower_var, bg="#f5f6fa", font=("Segoe UI", 11)).pack(anchor="w", padx=40)
tk.Checkbutton(frame, text="Include Digits", variable=digits_var, bg="#f5f6fa", font=("Segoe UI", 11)).pack(anchor="w", padx=40)
tk.Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#f5f6fa", font=("Segoe UI", 11)).pack(anchor="w", padx=40)

tk.Label(frame, text="Exclude Characters:", bg="#f5f6fa", font=("Helvetica", 12)).pack(anchor="w", pady=(10, 0), padx=20)
exclude_entry = tk.Entry(frame, width=25)
exclude_entry.pack(anchor="w", padx=20, pady=5)

# Buttons
tk.Button(frame, text="Generate Password", command=generate_password, font=("Segoe UI", 12, "bold"), bg="#273c75", fg="white").pack(pady=15)
tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Segoe UI", 12, "bold"), bg="#44bd32", fg="white").pack(pady=5)
tk.Button(frame, text="Save Password", command=save_password, font=("Segoe UI", 12, "bold"), bg="#3742fa", fg="white").pack(pady=5)

root.mainloop()
