import string
import tkinter as tk
from tkinter import messagebox

common_passwords = ['123456', 'password', '12345678', 'qwerty', 'abc123', '111111']

def check_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_symbol])

    analysis = [
        f"Length: {length}",
        f"Includes lowercase: {has_lower}",
        f"Includes uppercase: {has_upper}",
        f"Includes digits: {has_digit}",
        f"Includes symbols: {has_symbol}",
    ]

    if password in common_passwords:
        analysis.append("Warning: This is a common weak password!")

    if length < 8 or score < 3:
        strength = "Strength: Weak"
    elif length >= 8 and score == 3:
        strength = "Strength: Moderate"
    else:
        strength = "Strength: Strong"

    analysis.append(strength)
    return "\n".join(analysis)


def estimate_brute_force_time(password):
    charset_size = 0
    if any(c.islower() for c in password): charset_size += 26
    if any(c.isupper() for c in password): charset_size += 26
    if any(c.isdigit() for c in password): charset_size += 10
    if any(c in string.punctuation for c in password): charset_size += len(string.punctuation)

    total_combinations = charset_size ** len(password)
    guesses_per_second = 1e6
    seconds = total_combinations / guesses_per_second

    if seconds < 60:
        verdict = "=> Can be cracked in under a minute."
    elif seconds < 3600:
        verdict = "=> Can be cracked in under an hour."
    elif seconds < 86400:
        verdict = "=> Can be cracked in a day."
    else:
        verdict = "=> Cracking this would take days or more — relatively secure."

    return f"Estimated brute-force time: {seconds:.2e} seconds\n{verdict}"


def analyze_password():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Input Required", "Please enter a password.")
        return
    analysis_result = check_strength(pwd)
    brute_force_result = estimate_brute_force_time(pwd)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"{analysis_result}\n\n{brute_force_result}")



root = tk.Tk()
root.title("Password Strength Checker")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Enter your password:").pack()

entry = tk.Entry(frame, width=30, show="*")
entry.pack(pady=5)

tk.Button(frame, text="Check Strength", command=analyze_password).pack(pady=10)

result_text = tk.Text(frame, height=12, width=60)
result_text.pack()

root.mainloop()
