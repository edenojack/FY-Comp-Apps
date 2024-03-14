import tkinter as tk
from sympy.logic.boolalg import Or, And, Not, simplify_logic
from sympy.parsing.sympy_parser import parse_expr

 
 # Simplify the inputted expression function

def equation_simplified():
    input_expression = equation_entry.get()

    try:
        parsed_expression = parse_expr(input_expression)
        equation_entered.config(text="Expression Entered: " + input_expression)
        simplfied_expression = simplify_logic(parsed_expression)
        simplified_label.config(text="Simplfied Expression: " + str(simplfied_expression))
    except Exception as e:
        simplified_label.config(text="Error: " + str(e))
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
 
submit = tk.Button(root, text="Submit", command=equation_simplified)
submit.pack(pady=10)
 
equation_entered = tk.Label(root, text="Expression Entered: ")
equation_entered.pack(pady=10)

simplified_label = tk.Label(root, text="Simplfied Expression: ")
simplified_label.pack(pady=10)
 
root.mainloop()