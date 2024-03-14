import tkinter as tk

# Defines Landing Page
class LandingPage:
    def __init__(self, master):
        #Title of main window
        self.master = master
        self.master.title("Boolean Algebra App")
        
        # Frame to hold buttons and labels
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.margin_frame = tk.Frame(self.frame, bg="light grey", width=200)  # Set background color and width
        self.margin_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Initial explanatory text
        self.explanation_label = tk.Label(self.frame, text="Welcome to Boolean Algebra App!\n\nThis application helps you with Boolean algebra operations and logic circuit simplifications.\n\nTo get started, click on the options in the left menu.")
        self.explanation_label.pack(pady=20)
        
        # Title for the margin
        self.label_menu = tk.Label(self.margin_frame, text="Menu", bg="light grey", font=("Helvetica", 14, "bold"))
        self.label_menu.pack(pady=10)
        
        # Buttons in the left margin
        self.button_theory = tk.Button(self.margin_frame, text="Theory", command=self.show_theory_page)
        self.button_theory.pack(pady=10, padx=20)
        
        self.button_simplifier = tk.Button(self.margin_frame, text="Boolean Algebra Simplifier", command=self.show_simplifier_page)
        self.button_simplifier.pack(pady=10, padx=20)
        
        self.button_circuit = tk.Button(self.margin_frame, text="Boolean Logic Circuit Simplifier", command=self.show_circuit_page)
        self.button_circuit.pack(pady=10, padx=20)
        
        # Frames for each page
        self.theory_frame = tk.Frame(self.frame)
        self.simplifier_frame = tk.Frame(self.frame)
        self.circuit_frame = tk.Frame(self.frame)
        
        self.theory_frame.pack_forget()
        self.simplifier_frame.pack_forget()
        self.circuit_frame.pack_forget()
        
        # Create page contents
        self.create_theory_page()
        self.create_simplifier_page()
        self.create_circuit_page()
    
    def create_theory_page(self):
        self.label_theory = tk.Label(self.theory_frame, text="This is the Theory Page")
        self.label_theory.pack(padx=20, pady=20)

        # Theory code will go under here
        
    def create_simplifier_page(self):
        self.label_simplifier = tk.Label(self.simplifier_frame, text="This is the Boolean Algebra Simplifier Page")
        self.label_simplifier.pack(padx=20, pady=20)

        # Boolean simplfier code will go under here
        
    def create_circuit_page(self):
        self.label_circuit = tk.Label(self.circuit_frame, text="This is the Boolean Logic Circuit Simplifier Page")
        self.label_circuit.pack(padx=20, pady=20)

        # Boolean logic circuit code will go under here
    
    def show_theory_page(self):
        self.hide_all_frames()
        self.explanation_label.pack_forget()  # Hide explanation label
        self.theory_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def show_simplifier_page(self):
        self.hide_all_frames()
        self.explanation_label.pack_forget()  # Hide explanation label
        self.simplifier_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def show_circuit_page(self):
        self.hide_all_frames()
        self.explanation_label.pack_forget()  # Hide explanation label
        self.circuit_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def hide_all_frames(self):
        self.theory_frame.pack_forget()
        self.simplifier_frame.pack_forget()
        self.circuit_frame.pack_forget()

# Main Loop
        
def main():
    root = tk.Tk()
    app = LandingPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
