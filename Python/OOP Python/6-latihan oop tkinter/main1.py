import tkinter as ttk

# Membuat objek
window = ttk.Tk()

# Label
label1 = ttk.Label(window,text="Label 1")
label2 = ttk.Label(window,text="Label 2")

# Positioning
label1.pack()
label2.pack()

# Loop
window.mainloop()