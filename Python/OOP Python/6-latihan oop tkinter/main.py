import tkinter as ttk

# Deklarasi
window = ttk.Tk()

label1 = ttk.Label(window,text = "label1")
label2 = ttk.Label(window,text = "label 2")

tombol1 = ttk.Button(window, text = "tombol1")

# Postioning
label1.pack()
label2.pack()

tombol1.pack()

# Menampilkan GUI
window.mainloop()