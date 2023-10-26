import tkinter as tk


def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Helvetica", 20))
entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("=",)
]

for button_row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for button_text in button_row:
        button = tk.Button(frame, text=button_text, font=("Helvetica", 15), padx=20, pady=20)
        button.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_click)

root.mainloop()
