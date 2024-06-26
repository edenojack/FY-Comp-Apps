import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from sympy.logic.boolalg import simplify_logic
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
import subprocess
import os

# To make a new page add it as a class, for example:

    # class NewPage(BasePage):
        #def __init__(self, master, *args, **kwargs):
        #super().__init__(master, *args, **kwargs)
        #self.label_new_page = tk.Label(self, text="New Page", font=('bold', 12))
        #self.label_new_page.pack(padx=20, pady=20)

            # Add more widgets and logic as needed

            # Then go to class MenuPages(tk.Frame): and add the new page there
            # Do the same at def create_menu_buttons(self): to add the page button into the menu

class BasePage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
    
    def show(self):
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
    def hide(self):
        self.pack_forget()

class History(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_new_page = tk.Label(self, text="History of Computing", font=('bold', 16))
        self.label_new_page.pack(padx=20, pady=20)

        history_text = """

        Boolean algebra is a branch of mathematical logic that deals with the representation of truth values. It was developed by the English mathematician George Boole in the mid-19th century.

        In Boolean algebra, variables can only have two possible values: true (1) or false (0). The operations in Boolean algebra are similar to those in ordinary algebra, but they operate on truth values rather than numerical values.

        Boolean algebra laid the foundation for the design and analysis of digital circuits. This led to the development of logic gates, which are the building blocks of digital circuits.

        Logic gates are electronic devices that perform Boolean operations on one or more input signals to produce a single output signal. There are several types of logic gates, including AND, OR, NOT, NAND, NOR, XOR, and XNOR gates.

        The combination of logic gates in digital circuits allows for the implementation of complex logical functions, making them essential components in computer hardware and digital electronics.

        Boolean algebra and logic gates play a fundamental role in the design and operation of modern digital systems, including computers, microprocessors, and integrated circuits.
        """

        self.history_label = tk.Label(self, text=history_text, justify="left", wraplength=800)
        self.history_label.pack(padx=20, pady=20)

class BinaryConverter(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.create_help_button()

        self.label_title = tk.Label(self, text="Binary Converter Tool", font=('bold', 16))
        self.label_title.pack(pady=10)

        self.label_instructions = tk.Label(self, text="Enter a value and select conversion type:", font=('Arial', 12))
        self.label_instructions.pack()
        self.input_entry = tk.Entry(self, width=30, font=('Arial', 12))
        self.input_entry.pack(pady=5)

        self.conversion_type = tk.StringVar(self)
        self.conversion_type.set("Binary to Decimal")
        self.conversion_menu = ttk.Combobox(self, textvariable=self.conversion_type, values=["Binary to Decimal", "Decimal to Binary", "Decimal to Hexadecimal"], font=('Arial', 12))
        self.conversion_menu.pack(pady=5)

        self.convert_button = tk.Button(self, text="Convert", command=self.convert, font=('Arial', 12))
        self.convert_button.pack(pady=10)
        self.label_output = tk.Label(self, text="Output:", font=('Arial', 12, 'bold'))
        self.label_output.pack(pady=5)
        self.output_text = tk.Text(self, height=8, width=50, font=('Arial', 12))
        self.output_text.pack(pady=5)

    def convert(self):
        input_value = self.input_entry.get()
        conversion_type = self.conversion_type.get()

        try:
            explanation = ""
            if conversion_type == "Binary to Decimal":
                decimal_value = int(input_value, 2)
                result = str(decimal_value)
                explanation = f"To convert binary '{input_value}' to decimal:\n"
                explanation += f"1. Start from the rightmost digit.\n"
                explanation += f"2. Multiply each digit by 2 raised to the power of its position.\n"
                explanation += f"3. Add the results together to get the decimal value."
            elif conversion_type == "Decimal to Binary":
                decimal_value = int(input_value)
                result = bin(decimal_value)[2:]
                explanation = f"To convert decimal '{input_value}' to binary:\n"
                explanation += f"1. Divide the decimal number by 2.\n"
                explanation += f"2. Write down the remainder (0 or 1).\n"
                explanation += f"3. Repeat the process with the quotient until it becomes 0."
            elif conversion_type == "Decimal to Hexadecimal":
                decimal_value = int(input_value)
                result = hex(decimal_value)[2:].upper()
                explanation = f"To convert decimal '{input_value}' to hexadecimal:\n"
                explanation += f"1. Divide the decimal number by 16.\n"
                explanation += f"2. Write down the remainder as a single hexadecimal digit (0-9 or A-F).\n"
                explanation += f"3. Repeat the process with the quotient until it becomes 0."

            explanation += "\n\nResult:"
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, explanation + "\n" + result)
        except ValueError:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Invalid Input")

    def create_help_button(self):
        help_button = tk.Button(self, text="Help", command=self.show_help)
        help_button.place(x=1000, y=10)

    def show_help(self):
        help_text = """
        Welcome to the Binary Converter Help Page!

        This window provides assistance on how to use the binary converter tool.

        To use the converter:
        1. Enter a value input in the input box.
        2. Select the conversion type from the dropdown menu.
        3. Click the 'Convert' button to perform the conversion.
        4. The result will be displayed in the output box below.

        Conversion Types:
        - Binary to Decimal: Convert binary numbers to decimal numbers.
        - Decimal to Binary: Convert decimal numbers to binary numbers.
        - Decimal to Hexadecimal: Convert decimal numbers to hexadecimal numbers.

        Notes:
        - For binary input, use only 0s and 1s.
        - For decimal input, enter integer values only.
        - Hexadecimal input should be prefixed with '0x' (e.g., 0xFF).

        How to Perform Conversions:
        - Binary to Decimal:
            - Start from the rightmost digit.
            - Multiply each digit by 2 raised to the power of its position.
            - Add the results together to get the decimal value.
        - Decimal to Binary:
            - Divide the decimal number by 2.
            - Write down the remainder (0 or 1).
            - Repeat the process with the quotient until it becomes 0.
        - Decimal to Hexadecimal:
            - Divide the decimal number by 16.
            - Write down the remainder as a single hexadecimal digit (0-9 or A-F).
            - Repeat the process with the quotient until it becomes 0.

        Enjoy converting your numbers!
        """
        messagebox.showinfo("Binary Converter Help", help_text)
        
class BooleanSimplifierPage(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_boolean_simplifier = tk.Label(self, text="Simplify Boolean Expressions", font=('bold', 16))
        self.label_boolean_simplifier.pack(padx=20, pady=20)

        instruction_label = ttk.Label(self, text="Enter a Boolean expression (variables: A, B, C, D):")
        instruction_label.pack(pady=10)
        note_label = ttk.Label(self, text="NOTE IN ANSWERS: '|' = OR, '~' = NOT, '&' = AND")
        note_label.pack(pady=10)

        def simplify_expression():
            expr_text = expr_entry.get()
            try:
                expr = parse_boolean_expr(expr_text)
                simplified_expr = simplify_logic(expr, form='dnf')
                result_label.config(text=f"Simplified expression: {simplified_expr}")
            except Exception as e:
                result_label.config(text=f"Error: {e}")

        def parse_boolean_expr(expr_text):
            transformations = (standard_transformations + (implicit_multiplication_application,))
            expr_text = expr_text.replace('+', ' | ').replace('.', ' & ').replace('!', '~')
            return parse_expr(expr_text, transformations=transformations, evaluate=False)

        def insert_text(text):
            expr_entry.insert(tk.END, text)

        expr_entry = ttk.Entry(self, width=50)
        expr_entry.pack(pady=10)

        operators_frame = ttk.Frame(self)
        operators_frame.pack(pady=10)

        not_button = ttk.Button(operators_frame, text='!', command=lambda: insert_text("Not("))
        not_button.grid(row=0, column=0, padx=5)
        open_bracket_button = ttk.Button(operators_frame, text='(', command=lambda: insert_text("("))
        open_bracket_button.grid(row=0, column=1, padx=5)
        close_bracket_button = ttk.Button(operators_frame, text=')', command=lambda: insert_text(")"))
        close_bracket_button.grid(row=0, column=2, padx=5)
        or_button = ttk.Button(operators_frame, text='+', command=lambda: insert_text("+"))
        or_button.grid(row=0, column=3, padx=5)
        and_button = ttk.Button(operators_frame, text='.', command=lambda: insert_text("."))
        and_button.grid(row=0, column=4, padx=5)

        simplify_button = ttk.Button(self, text="Simplify", command = simplify_expression)
        simplify_button.pack(pady=10)

        result_label = ttk.Label(self, text="")
        result_label.pack(pady=10)

        help_button = tk.Button(self, text="Help", command=self.show_help)
        help_button.place(x=1000, y=10)

    def show_help(self):
        help_text = """
        Welcome to the Boolean Expression Simplifier!

        This tool allows you to simplify Boolean expressions using basic operators and variables (A, B, C, D).
        You can enter expressions using the following operators:
        - '!' for NOT
        - '(' and ')' for parentheses
        - '+' for OR
        - '.' for AND

        To simplify an expression, enter it in the text box and click the 'Simplify' button.
        The simplified expression will be displayed below.

        Note: In Answers: '|' = OR, '~' = NOT, '&' = AND"

        Enjoy simplifying your Boolean expressions!
        """
        messagebox.showinfo("Boolean Simplifier Help", help_text)

class LogicSimplifierPage(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_logic_simplifier = tk.Label(self, text="Simplify Logic Gates", font=('bold', 16))
        self.label_logic_simplifier.pack(padx=20, pady=20)

        # Button to open logix.py
        self.open_logix_button = tk.Button(
            self,
            text="Open Logic Gate Simplifier",
            command=self.open_logix,
            bg='lightblue'
        )
        self.open_logix_button.pack(padx=20, pady=20)

        # Adding the Help button
        self.help_button = tk.Button(self, text="Help", command=self.show_help)
        self.help_button.place(x=1000, y=10)  # Adjust position as needed

    def open_logix(self):
        # Path to the Python script to be opened
        file_path = r"C:\Users\nolan\OneDrive\Documents\Uni\VS Code\logix\logix.py"

        try:
            # Start a new process to run the logix.py script
            subprocess.Popen(["python", file_path])
        except Exception as e:
            print(f"An error occurred while opening the Logix app: {e}")

    def show_help(self):
        # Help text to be displayed
        help_text = """
        Welcome to the Logic Gate Simplifier!

        This tool allows you to simulate logic gate circuits.
        
        You need to download the python file 'logix file for final' and place in same folder as this python file.
        once you've done that, on this code go to line 258, change the pathway in brackets to the pathway of the logix file
        can find pathway by right clicking and selecting 'copy file pathway'
        you need to install all extensions, if needed write into terminal " pip install XXX "

        """
        # Show the help information in a message box
        messagebox.showinfo("Boolean Simplifier Help", help_text)

            

class BooleanFormulasPage(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_boolean_formulas = tk.Label(self, text="Boolean Algebra Cheat Sheet", font=('bold', 16))
        self.label_boolean_formulas.pack(padx=20, pady=20)

        message = "Boolean algebra laws are fundamental rules used to simplify and manipulate Boolean expressions.\n\nThese laws are essential in logic circuit design and optimization.\n\nBelow are examples of the main Boolean Algebra laws:"
        self.message_label = tk.Label(self, text=message)
        self.message_label.pack(padx=20, pady=20)

        laws = {
            "Identity Law": "A + 0 = A\nA * 1 = A",
            "Annulment Law": "A + 1 = 1\nA * 0 = 0",
            "Complement Law": "A + A' = 1\nA * A' = 0",
            "Idempotent Law": "A + A = A\nA * A = A",
            "Associative Law": "(A + B) + C = A + (B + C)\n(A * B) * C = A * (B * C)",
            "Commutative Law": "A + B = B + A\nA * B = B * A",
            "Distributive Law": "A + (B * C) = (A + B) * (A + C)\nA * (B + C) = (A * B) + (A * C)",
            "De Morgan's Law": "(A + B)' = A' * B'\n(A * B)' = A' + B'"
        }

        self.laws_text = tk.Text(self, wrap=tk.WORD)
        self.laws_text.pack(padx=20, pady=20)

        for law, formula in laws.items():
            self.laws_text.insert(tk.END, f"{law}:\n{formula}\n\n")
    
        self.laws_text.config(state=tk.DISABLED)

class LogicTheoryPage(BasePage):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label_logic_theory = tk.Label(self, text="Understanding Logic Gates", font=('bold', 16))
        self.label_logic_theory.pack(padx=20, pady=20)

        self.create_help_button()

        self.create_logic_theory()

    def create_help_button(self):
        help_button = tk.Button(self, text="Help", command=self.show_help)
        help_button.place(x=1000, y=10)

    def show_help(self):
        help_text = """
        This window provides an explanation of logic gates and their operations.

        Displayed is basic information about logic gates, including AND, OR, and NOT gates. Each gate is described along with its functionality.

        Below each gate description, you'll see an animation demonstrating how the gate works. You can interact with the animations by clicking on the input circles to toggle their states.

        When toggled 'red' the input or output represents 0
        When toggled 'green' the input or output represents 1

        Feel free to explore the content and interact with the animations to understand the concepts better.

        """
        messagebox.showinfo("Logic Theory Page Help", help_text)

    def create_logic_theory(self):
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor=tk.NW)

        self.logic_gate_explanation_1 = tk.Label(self.inner_frame, text="Logic gates are fundamental building blocks of digital circuits. Here are the basic logic gates:\n\nYou can simplify logic circuits using these gates to perform various operations.", wraplength=300)
        self.logic_gate_explanation_1.pack(padx=20, pady=20, anchor=tk.CENTER)
        
        gate_explanations = [
            ("AND", "AND Gate: Takes two inputs and produces an output only if both inputs are True."),
            ("OR", "OR Gate: Takes two inputs and produces an output if at least one input is True."),
            ("NOT", "NOT Gate: Takes one input and produces the opposite output.")
        ]
        for gate_name, explanation_text in gate_explanations:
            explanation_label, gate_animation = self.create_logic_gate_explanation(gate_name, explanation_text)
            explanation_label.pack(padx=20, pady=20)

        def on_canvas_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.inner_frame.bind("<Configure>", on_canvas_configure)

    def create_logic_gate_explanation(self, gate_name, explanation_text):
        label = tk.Label(self.inner_frame, text=explanation_text)
        label.pack(padx=20, pady=20)
        if gate_name == "AND":
            gate_animation = ANDGateAnimation(self.inner_frame)
        elif gate_name == "OR":
            gate_animation = ORGateAnimation(self.inner_frame)
        elif gate_name == "NOT":
            gate_animation = NOTGateAnimation(self.inner_frame)
        return label, gate_animation


class MenuPages(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.master.title("Boolean Algebra App")

        self.header_label = tk.Label(master, text="Boolean Algebra App", font=("Helvetica", 16, "bold"), bg="light blue")
        self.header_label.pack(pady=0, fill=tk.X)

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.margin_frame = tk.Frame(self.frame, bg="light blue", width=180)
        self.margin_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.explanation_label = tk.Label(self.frame, text="Welcome to the Boolean Algebra App!\n\nThis application helps you with Boolean algebra operations and logic circuit simplifications.\n\nTo get started, click on the options in the left menu.")
        self.explanation_label.pack(pady=20)

        self.pages = [
            History(self.frame),
            BinaryConverter(self.frame),
            BooleanSimplifierPage(self.frame),
            LogicSimplifierPage(self.frame),
            BooleanFormulasPage(self.frame),
            LogicTheoryPage(self.frame)

            #ADD NEW PAGES HERE
        ]
        
        self.current_page = None

        self.create_menu_buttons()
        self.create_close_button()

    def create_menu_buttons(self):
        self.label_menu = tk.Label(self.margin_frame, text="Menu", bg="light blue", font=("Helvetica", 14, "bold"))
        self.label_menu.pack(pady=10)
    
        buttons = [
            ("History of Computing", self.pages[0]),
            ("Binary Converter Tool", self.pages[1]),
            ("Simplfiy Boolean Expressions", self.pages[2]),
            ("Simplify Logic Gates", self.pages[3]),
            ("Boolean Algebra Cheat Sheet", self.pages[4]),
            ("Understanding Logic Gates", self.pages[5])

            #ADD NEW PAGES HERE
        ]

        for text, page in buttons:
            button = tk.Button(self.margin_frame, text=text, command=lambda p=page: self.show_page(p))
            button.pack(pady=10, padx=20)

    def create_close_button(self):
        close_button = tk.Button(self.master, text="Close", command=self.master.destroy)
        close_button.place(x=1200, y=600)

    def show_page(self, page):
        if self.current_page:
            self.current_page.hide()
        self.explanation_label.pack_forget()
        page.show()
        self.current_page = page


# These are the animations for the logic theory page

class ANDGateAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=200, bg='white')
        self.canvas.pack()
        self.input1_state = False
        self.input2_state = False
        self.output_state = False
        
        self.create_elements()
        
    def create_elements(self):
        self.input1 = self.canvas.create_oval(50, 50, 80, 80, outline='black', fill='white')
        self.input2 = self.canvas.create_oval(50, 120, 80, 150, outline='black', fill='white')
        self.output = self.canvas.create_oval(220, 85, 250, 115, outline='black', fill='white')
        
        self.gate = self.canvas.create_polygon(120, 60, 160, 60, 160, 140, 120, 140, outline='black', fill='white')
        self.canvas.create_line(80, 65, 120, 100, fill='black')
        self.canvas.create_line(80, 135, 120, 100, fill='black')
        self.canvas.create_line(160, 100, 220, 100, fill='black')
        
        self.canvas.create_text(25, 70, text='IN1')
        self.canvas.create_text(25, 140, text='IN2')
        self.canvas.create_text(275, 100, text='OUT')
        self.canvas.create_text(140, 100, text='AND Gate')
        
        self.canvas.tag_bind(self.input1, '<Button-1>', lambda event: self.toggle_input(1))
        self.canvas.tag_bind(self.input2, '<Button-1>', lambda event: self.toggle_input(2))
        
    # AND Gate Logic
    def toggle_input(self, input_num):
        if input_num == 1:
            self.input1_state = not self.input1_state
            self.canvas.itemconfig(self.input1, fill='green' if self.input1_state else 'red')
        elif input_num == 2:
            self.input2_state = not self.input2_state
            self.canvas.itemconfig(self.input2, fill='green' if self.input2_state else 'red')
        
        self.update_output()
        
    def update_output(self):
        if self.input1_state and self.input2_state:
            self.output_state = True
        else:
            self.output_state = False
            
        self.canvas.itemconfig(self.output, fill='green' if self.output_state else 'red')

class ORGateAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=200, bg='white')
        self.canvas.pack()
        self.input1_state = False
        self.input2_state = False
        self.output_state = False
        
        self.create_elements()
        
    def create_elements(self):
        self.input1 = self.canvas.create_oval(50, 50, 80, 80, outline='black', fill='white')
        self.input2 = self.canvas.create_oval(50, 120, 80, 150, outline='black', fill='white')
        self.output = self.canvas.create_oval(220, 85, 250, 115, outline='black', fill='white')

        self.gate = self.canvas.create_polygon(120, 60, 160, 60, 160, 140, 120, 140, outline='black', fill='white')
        self.canvas.create_line(80, 65, 120, 100, fill='black')
        self.canvas.create_line(80, 135, 120, 100, fill='black')
        self.canvas.create_line(160, 100, 220, 100, fill='black')

        self.canvas.create_text(25, 70, text='IN1')
        self.canvas.create_text(25, 140, text='IN2')
        self.canvas.create_text(275, 100, text='OUT')
        self.canvas.create_text(140, 100, text='OR Gate')

        self.canvas.tag_bind(self.input1, '<Button-1>', lambda event: self.toggle_input(1))
        self.canvas.tag_bind(self.input2, '<Button-1>', lambda event: self.toggle_input(2))

    # OR Gate Logic
    def toggle_input(self, input_num):
        if input_num == 1:
            self.input1_state = not self.input1_state
            self.canvas.itemconfig(self.input1, fill='green' if self.input1_state else 'red')
        elif input_num == 2:
            self.input2_state = not self.input2_state
            self.canvas.itemconfig(self.input2, fill='green' if self.input2_state else 'red')
        
        self.update_output()
        
    def update_output(self):
        if self.input1_state or self.input2_state:
            self.output_state = True
        else:
            self.output_state = False
            
        self.canvas.itemconfig(self.output, fill='green' if self.output_state else 'red')

class NOTGateAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=200, bg='white')
        self.canvas.pack()
        self.input_state = False
        self.output_state = False
        
        self.create_elements()
        
    def create_elements(self):
        self.input = self.canvas.create_oval(50, 100, 80, 130, outline='black', fill='white')
        self.output = self.canvas.create_oval(220, 100, 250, 130, outline='black', fill='white')
        
        self.gate = self.canvas.create_rectangle(110, 80, 170, 150, outline='black', fill='white')
        self.not_gate_symbol = self.canvas.create_text(140, 115, text='NOT Gate')
        self.not_gate_line = self.canvas.create_line(80, 115, 110, 115, fill='black')
        self.not_gate_output_line = self.canvas.create_line(170, 115, 220, 115, fill='black')

        self.canvas.create_text(25, 115, text='IN')
        self.canvas.create_text(275, 115, text='OUT')
        
        self.canvas.tag_bind(self.input, '<Button-1>', self.toggle_input)

     # NOT Gate Logic   
    def toggle_input(self, event):
        self.input_state = not self.input_state
        self.canvas.itemconfig(self.input, fill='green' if self.input_state else 'red')
        self.update_output()
        
    def update_output(self):
        self.output_state = not self.input_state
        self.canvas.itemconfig(self.output, fill='green' if self.output_state else 'red')
       

def main():
    root = tk.Tk()
    app = MenuPages(root)
    root.mainloop()

if __name__ == "__main__":
    main()
