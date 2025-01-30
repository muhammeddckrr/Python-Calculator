import tkinter as tk
from tkinter import messagebox

# mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# getting inputs from user

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

# printing results

    if operation == 'Add':
        result = add(num1, num2)
    elif operation == 'Subtract':
        result = subtract(num1, num2)
    elif operation == 'Multiply':
        result = multiply(num1, num2)
    elif operation == 'Divide':
        result = divide(num1, num2)
    
    result_label.config(text=f"Result: {result}")

# App Informations

app = tk.Tk()
app.title("Calculator")

tk.Label(app, text="First Number:").grid(row=0, column=0)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

tk.Label(app, text="Second Number:").grid(row=1, column=0)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

operation_var = tk.StringVar(app)
operation_var.set("Add")
operations_menu = tk.OptionMenu(app, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=0, columnspan=2)

tk.Button(app, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(app, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

app.mainloop()