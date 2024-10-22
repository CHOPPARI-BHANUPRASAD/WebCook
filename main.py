import tkinter as tk
from tkinter import messagebox

# Function to update the display with the button click
def button_click(value):
    current_text = display_var.get()
    if value == "C":
        display_var.set("")
    elif value == "=":
        try:
            result = eval(current_text)
            display_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            display_var.set("")
    else:
        display_var.set(current_text + str(value))

# Main application window
root = tk.Tk()
root.title("Simple Calculator")

# Display for showing the current input and results
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons and place them on the grid
row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: button_click(x)
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
root.mainloop()