import tkinter as tk
import random
import string

passwords = []  # List to store generated passwords

def generate_password(digitsAmount, specialAmount, uppercaseAmount, ownWordOption):
    global passwords
    passwords.clear()  # Clear the list to hold the new passwords

    for _ in range(5):  # Generate 5 different passwords
        password = ""

        # Generate digits
        for i in range(0, digitsAmount):
            password += str(random.randint(0, 9))
        
        # Special characters
        specialCharacters = string.punctuation
        for i in range(0, specialAmount):
            password += random.choice(specialCharacters)
        
        # Uppercase letters
        for i in range(0, uppercaseAmount):
            password += random.choice(string.ascii_uppercase)

        # If the user selects to add their own word
        if ownWordOption == "Yes":
            ownWord = entry.get()
            temp_pass = list(password)
            random.shuffle(temp_pass)  # Shuffle the password to mix up the characters
            temp_pass = ''.join(temp_pass)

            # Insert own word at random positions
            index = random.randint(0, len(temp_pass))  # Random index for the own word
            final_password = temp_pass[:index] + ownWord + temp_pass[index:]
            passwords.append(final_password)
        else:
            # Just shuffle the password without adding the own word
            password = list(password)
            random.shuffle(password)
            password = ''.join(password)
            passwords.append(password)

    display_passwords()

def display_passwords():
    for widget in window.winfo_children():
        widget.destroy()  # Remove all widgets before displaying new ones
    
    # Display the passwords
    title_label = tk.Label(window, text="Generated Passwords", font=("Arial", 44, "bold", "underline"))
    title_label.pack()

    for i, password in enumerate(passwords):
        generatedPassword_label = tk.Label(window, text=f"Password {i+1}: {password}", font=("Arial", 16))
        generatedPassword_label.pack(pady=10)

    # Back button
    back_button = tk.Button(window, text="Back", font=("Arial", 20), command=main)
    back_button.pack(pady=10)

def options():
    for widget in window.winfo_children():
        widget.destroy()

    options_frame = tk.Frame(window)
    options_frame.pack(pady=20)

    # Digits
    number_frame = tk.Frame(options_frame)
    number_frame.grid(row=0, column=0, padx=20)
    number_label = tk.Label(number_frame, text="Number of Digits", font=("Arial", 16))
    number_label.grid(row=0, column=0, pady=5)
    numberAmount_value_inside = tk.StringVar(window)
    numberAmount_value_inside.set("0")
    numberAmount_menu = tk.OptionMenu(number_frame, numberAmount_value_inside, "0", "1", "2", "3", "4")
    numberAmount_menu.config(font=("Arial", 14))
    numberAmount_menu.grid(row=1, column=0)

    # Special Characters
    special_frame = tk.Frame(options_frame)
    special_frame.grid(row=1, column=0, padx=20)
    special_label = tk.Label(special_frame, text="Number of Special Characters", font=("Arial", 16))
    special_label.grid(row=0, column=0, pady=5)
    special_value_inside = tk.StringVar(window)
    special_value_inside.set("0")
    special_menu = tk.OptionMenu(special_frame, special_value_inside, "0", "1", "2", "3", "4")
    special_menu.config(font=("Arial", 14))
    special_menu.grid(row=1, column=0)

    # Uppercase Letters
    uppercase_frame = tk.Frame(options_frame)
    uppercase_frame.grid(row=2, column=0, padx=20)
    uppercase_label = tk.Label(uppercase_frame, text="Number of Uppercase Letters", font=("Arial", 16))
    uppercase_label.grid(row=0, column=0, pady=5)
    uppercase_value_inside = tk.StringVar(window)
    uppercase_value_inside.set("0")
    uppercase_menu = tk.OptionMenu(uppercase_frame, uppercase_value_inside, "0", "1", "2", "3", "4")
    uppercase_menu.config(font=("Arial", 14))
    uppercase_menu.grid(row=1, column=0)

    # Own Word Option
    own_word_frame = tk.Frame(options_frame)
    own_word_frame.grid(row=3, column=0, padx=20)
    own_word_label = tk.Label(own_word_frame, text="Do you want to add your own word?", font=("Arial", 16))
    own_word_label.grid(row=0, column=0, pady=5)
    ownWordOption = tk.StringVar(window)
    ownWordOption.set("No")
    ownWord_menu = tk.OptionMenu(own_word_frame, ownWordOption, "Yes", "No")
    ownWord_menu.config(font=("Arial", 14))
    ownWord_menu.grid(row=1, column=0)

    # Entry for own word
    global entry  # Define entry as a global variable to access it inside generate_password
    entry = tk.Entry(window, font=("Arial", 16))
    entry.pack(pady=10)

    # Submit Button
    submit_button = tk.Button(window, text="Submit", font=("Arial", 20), command=lambda: [
        submit_button.config(state="disabled"),  # Disable the button
        generate_password(
            int(numberAmount_value_inside.get()),
            int(special_value_inside.get()),
            int(uppercase_value_inside.get()),
            ownWordOption.get()
        )])
    submit_button.pack(pady=10)

    # Back Button
    back_button = tk.Button(window, text="Back", font=("Arial", 20), command=main)
    back_button.pack(pady=10)

def main():
    for widget in window.winfo_children():
        widget.destroy()  # Clear all widgets before starting fresh
    
    title_label = tk.Label(window, text="Password Generator", font=("Arial", 44, "bold", "underline"))
    title_label.pack()

    choice_label = tk.Label(window, text="Choose your option", font=("Arial", 28, "underline"))
    choice_label.pack(pady=10)

    btn1 = tk.Button(window, text="Generate Password", font=("Arial", 20), command=options)
    btn1.pack(pady=10)

    btn2 = tk.Button(window, text="Password Security Check", font=("Arial", 18))
    btn2.pack(pady=10)

# Window setup
window = tk.Tk()
window.title("Password Generator")
window.geometry("800x800")

main()  # Start the app by calling the main function

window.mainloop()
