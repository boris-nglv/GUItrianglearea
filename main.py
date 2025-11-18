import tkinter as tk
from logic import calculate_area_from_entries, clear_entries

root = tk.Tk()
root.title("Лице на триъгълник")

tk.Label(root, text="Страна a:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Страна b:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Страна c:").grid(row=2, column=0, padx=10, pady=5)


entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)

entry_a.grid(row=0, column=1, padx=10, pady=5)
entry_b.grid(row=1, column=1, padx=10, pady=5)
entry_c.grid(row=2, column=1, padx=10, pady=5)

button = tk.Button(
    root, text="Сметни", command=lambda: calculate_area_from_entries(entry_a, entry_b, entry_c), bg="#4CAF50", fg="white", font=("Arial", 12))
button.grid(row=3, column=0, columnspan=2, pady=10)

triangle_img = tk.PhotoImage(file="triangle.png.png")
triangle_label = tk.Label(root, image=triangle_img)
triangle_label.grid(row=0, column=2, rowspan=4, padx=20, pady=10)

clear_button = tk.Button(root, text="Изчисти", command=lambda: clear_entries(entry_a, entry_b, entry_c), bg="#f44336", fg="white", font=("Arial", 12))
clear_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
