import tkinter as tk
from tkinter import messagebox
import numexpr  # pip install numexpr

def main():
    def evaluate_expression(expr):
        try:
            result = numexpr.evaluate(expr).item()
            return result
        except:
            raise ValueError("Invalid expression")

    def addToOperation(value):
        if value == "C":
            operation.clear()
        elif value == "=":
            try:
                result = evaluate_expression("".join(operation))
                operation.clear()
                operation.append(str(result))
            except Exception:
                messagebox.showerror("Erreur", "Opération invalide")
                operation.clear()
        elif value == "^":
            operation.append('**')
        else:
            operation.append(value)
        update_display()

    def update_display():
        display = "".join(operation)
        operationLabel.config(state="normal")
        operationLabel.delete(0, tk.END)
        operationLabel.insert(0, display)
        operationLabel.config(state="readonly")

    operation = []
    root = tk.Tk()
    root.title("Calculatrice sécurisée")
    root.configure(bg="lightblue")
    root.resizable(False, False)
    root.geometry("400x550")

    operationLabel = tk.Entry(root, font=("Arial", 24), bg="white", bd=3, justify="right")
    operationLabel.config(state="readonly")
    operationLabel.pack(pady=10, padx=10, fill="x")

    buttons_frame = tk.Frame(root, bg="lightblue")
    buttons_frame.pack()

    buttons = [
        ('C', 0, 0), ('(', 0, 1), (')', 0, 2), ('^', 0, 3),
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    button_colors = {
        '+': '#ffb84d', '-': '#ffb84d', '*': '#ffb84d', '/': '#ffb84d',
        '=': '#66cc66', 'C': '#ff6666', '^': '#ffb84d'
    }

    for (text, row, col) in buttons:
        bg_color = button_colors.get(text, "lightgray")
        button = tk.Button(buttons_frame, text=text, font=("Arial", 18),
                           bg=bg_color, bd=2, width=4, height=2,
                           command=lambda t=text: addToOperation(t))
        button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    for i in range(5):
        buttons_frame.grid_rowconfigure(i, weight=1)
        buttons_frame.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    main()
