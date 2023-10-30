\import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = entry.get()  # Get the current input
    entry.delete(0, tk.END)  # Clear the input field
    entry.insert(0, current + str(number))  # Append the clicked number or operator

# Function to perform calculations when the "=" button is clicked
def calculate():
    current = entry.get()  # Get the current input
    try:
        result = str(eval(current))  # Evaluate the expression and convert the result to a string
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(0, result)  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)  # Clear the input field
        entry.insert(0, "Error")  # Display "Error" if there's a calculation error

# Function to handle backspace when the "Backspace" button is clicked
def backspace():
    current = entry.get()  # Get the current input
    entry.delete(0, tk.END)  # Clear the input field
    entry.insert(0, current[:-1])  # Remove the last character

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for input
entry = tk.Entry(window, width=50, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons for digits, operators, and special functions
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons in the grid
row = 1
col = 0

for button_text in buttons:
    # Create a button with specified text, command, font, width, and height
    tk.Button(window, text=button_text, command=lambda text=button_text: button_click(text),
              font=("Arial", 16), width=6, height=2).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear (C) button for clearing the input field
tk.Button(window, text='C', command=lambda: entry.delete(0, tk.END),
          font=("Arial", 16), width=6, height=2).grid(row=row, column=col, padx=5, pady=5)

# Create the backspace (Backspace) button for removing the last character
tk.Button(window, text='Backspace', command=backspace,
          font=("Arial", 16), width=10, height=2).grid(row=row, column=col+1, padx=5, pady=5)

# Create the equals (=) button for calculating the result
tk.Button(window, text='=', command=calculate,
          font=("Arial", 16), width=6, height=2).grid(row=row, column=col+2, padx=5, pady=5)

# Start the main loop to run the GUI
window.mainloop()
