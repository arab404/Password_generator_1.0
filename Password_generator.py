import re
import random
import string
import tkinter as tk
from tkinter import messagebox


def check_password_strength(password):
    """Check the strength of a password and suggest improvements."""
    strength = 0
    suggestions = []
    
    # Define criteria
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters.")
    else:
        strength += 1

    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    else:
        strength += 1

    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    else:
        strength += 1

    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one number.")
    else:
        strength += 1

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character (e.g., !@#$%^&*).")
    else:
        strength += 1

    # Classify password strength
    if strength == 5:
        return "Strong", []
    elif strength >= 3:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions


def generate_password(length=12):
    """Generate a secure random password."""
    if length < 8:
        length = 8  # Ensure minimum length

    # Characters to include in the password
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure password includes at least one of each required character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
    ]

    # Fill the rest of the password with random choices
    password += random.choices(characters, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)


def display_generated_password():
    """Generate and display a secure random password."""
    length = 12  # Default length
    generated_password = generate_password(length)
    entry_password.delete(0, tk.END)  # Clear the input field
    entry_password.insert(0, generated_password)  # Insert plain-text password


def check_password():
    """Get password input from the user and display results."""
    password = entry_password.get()
    strength, suggestions = check_password_strength(password)
    
    result_text = f"Password Strength: {strength}"
    if suggestions:
        result_text += "\n\nSuggestions:\n" + "\n".join(suggestions)
    
    messagebox.showinfo("Password Strength Checker", result_text)


# Set up the GUI
root = tk.Tk()
root.title("Password Strength Checker")

# Input label and entry
label = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label.pack(pady=10)

entry_password = tk.Entry(root, width=30, font=("Arial", 14), show="")
entry_password.pack(pady=10)

# Check button
button_check = tk.Button(root, text="Check Strength", font=("Arial", 14), command=check_password)
button_check.pack(pady=10)

# Generate Password button
button_generate = tk.Button(root, text="Generate Password", font=("Arial", 14), command=display_generated_password)
button_generate.pack(pady=10)

# Run the application
root.geometry("400x300")
root.mainloop()
