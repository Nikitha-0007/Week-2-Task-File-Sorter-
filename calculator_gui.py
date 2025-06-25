import tkinter as tk
from db_helper import log_operation

def calculate():
    try:
        expr = entry.get()
        result = str(eval(expr))
        label_result.config(text="Result: " + result)
        log_operation(expr, result)
    except ZeroDivisionError:
        label_result.config(text="Error: Division by zero")
    except Exception:
        label_result.config(text="Invalid Input")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Calculate", command=calculate).pack()
label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
