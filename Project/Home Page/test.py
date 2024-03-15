import tkinter as tk

class NOTGateAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=300, height=200, bg='white')
        self.canvas.pack()
        self.input_state = False
        self.output_state = False
        
        self.create_elements()
        
    def create_elements(self):
        # Create input and output nodes
        self.input = self.canvas.create_oval(50, 100, 80, 130, outline='black', fill='white')
        self.output = self.canvas.create_oval(220, 100, 250, 130, outline='black', fill='white')
        
        # Create gate
        self.gate = self.canvas.create_rectangle(110, 80, 170, 150, outline='black', fill='white')
        self.not_gate_symbol = self.canvas.create_text(140, 115, text='NOT', font=('bold', 12))
        self.not_gate_line = self.canvas.create_line(80, 115, 110, 115, fill='black')
        self.not_gate_output_line = self.canvas.create_line(170, 115, 220, 115, fill='black')
        
        # Create labels
        self.canvas.create_text(25, 115, text='IN')
        self.canvas.create_text(275, 115, text='OUT')
        
        # Bind mouse click to input node
        self.canvas.tag_bind(self.input, '<Button-1>', self.toggle_input)
        
    def toggle_input(self, event):
        self.input_state = not self.input_state
        self.canvas.itemconfig(self.input, fill='green' if self.input_state else 'white')
        self.update_output()
        
    def update_output(self):
        self.output_state = not self.input_state  # NOT gate logic
        self.canvas.itemconfig(self.output, fill='green' if self.output_state else 'white')

def main():
    root = tk.Tk()
    root.title('NOT Gate Animation')
    not_gate = NOTGateAnimation(root)
    root.mainloop()

if __name__ == "__main__":
    main()
