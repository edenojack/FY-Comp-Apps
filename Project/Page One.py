import tkinter as tk
 
 # Equation display

def equation():
    equation = equation_entry.get()
    equation_entered.config(text="Expression Entered: " + equation)

# Code to simplify equation

def equation_simplified():
    equation_simplifed = ()
    # Needs work - this is where code will code to simplify


# Main Loop
root = tk.Tk()
root.title("Equation Entry")
 
title = tk.Label(root, text="Boolean Algebra Simplifier", font=("Helvetica", 14, "bold"), fg="black")
title.pack(pady=10)
 
enter_expression = tk.Label(root, text="Enter the expression below:", font=("Helvetica", 12,), fg="black")
enter_expression.pack(pady=10)
 
equation_entry = tk.Entry(root, width=30)
equation_entry.pack(pady=10)
 
submit = tk.Button(root, text="Submit", command=equation)
submit.pack(pady=10)
 
equation_entered = tk.Label(root, text="Expression Entered: ")
equation_entered.pack(pady=10)
 
root.mainloop()