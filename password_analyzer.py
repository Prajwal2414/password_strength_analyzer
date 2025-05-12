import tkinter as tk
from tkinter import messagebox
import re
import string
from tkinter import ttk

def evaluate_password_strength(password):
    strength = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short. Use at least 12 characters for better security.")
    
    # Upper and Lower Case Check
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        strength += 2
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    # Digit Check
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    # Special Character Check
    if any(c in string.punctuation for c in password):
        strength += 2
    else:
        feedback.append("Include at least one special character (e.g., @, #, $).")
    
    # Common Passwords Check
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password.lower() in common_passwords:
        feedback.append("This password is too common. Choose a more unique one.")
        strength = 0
    
    # Repetitive Characters Check
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid using repeated characters.")
    
    return strength, feedback

def analyze_password():
    password = entry.get()
    strength, feedback = evaluate_password_strength(password)
    
    result_window = tk.Toplevel(root)
    result_window.title("Password Analysis Result")
    result_window.geometry("450x350")
    result_window.configure(bg="#e0f7fa")
    
    title_label = tk.Label(result_window, text="Password Strength Analysis", font=("Arial", 16, "bold"), bg="#e0f7fa")
    title_label.pack(pady=10)
    
    result_message = ""
    if strength >= 6:
        result_message += "✅ Strong password.\n"
    elif strength >= 3:
        result_message += "⚠️ Moderate password. Consider improving it.\n"
    else:
        result_message += "❌ Weak password. Change it immediately.\n"
    
    result_label = tk.Label(result_window, text=result_message, font=("Arial", 14), fg="#333", bg="#e0f7fa")
    result_label.pack(pady=10)
    
    if feedback:
        feedback_label = tk.Label(result_window, text="Suggestions to improve your password:", font=("Arial", 12, "bold"), bg="#e0f7fa")
        feedback_label.pack(pady=5)
        
        feedback_text = tk.Text(result_window, wrap="word", font=("Arial", 12), height=6, width=50, bg="#ffffff", relief="flat", bd=3, padx=5, pady=5)
        feedback_text.pack(pady=5)
        
        for tip in feedback:
            feedback_text.insert(tk.END, f"- {tip}\n")
        feedback_text.config(state="disabled")

def toggle_password():
    if entry.cget('show') == "*":
        entry.config(show="")
        eye_button.config(text="👁️")
    else:
        entry.config(show="*")
        eye_button.config(text="🔒")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("450x350")
root.configure(bg="#f0f0f0")

# Styling
label_font = ("Arial", 14, "bold")
button_font = ("Arial", 12, "bold")

# Label
label = tk.Label(root, text="Enter Password:", font=label_font, bg="#f0f0f0")
label.pack(pady=10)

# Password Entry with Eye Button
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack()
entry = tk.Entry(frame, show="*", width=30, font=("Arial", 14), relief="solid", bd=2)
entry.pack(side=tk.LEFT, padx=5, ipadx=5, ipady=5)

eye_button = tk.Button(frame, text="🔒", command=toggle_password, font=("Arial", 12), relief="flat", bg="#ddd")
eye_button.pack(side=tk.RIGHT, padx=5)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Password", font=button_font, command=analyze_password, bg="#4CAF50", fg="white", padx=10, pady=5, relief="raised")
analyze_button.pack(pady=20)

root.mainloop()