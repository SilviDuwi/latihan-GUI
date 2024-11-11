import tkinter as tk

# objek utama 
button = tk.Tk()

# judul halaman web
button.title("Keysa ghea - Button")

# Membuat label
label = tk.Label(button, text="Silakan Masukkan Nama Anda:")
label.pack()

# Membuat entry
entry = tk.Entry(button)
entry.pack()

# Fungsi yang akan dijalankan saat tombol diclick
def on_button_click():
    nama = entry.get()
    label.config(text=f"Nama Anda: {nama}")

# Membuat tombol
button = tk.Button(button, text="click here", command=on_button_click)
button.pack()

# Menjalankan GUI
button.mainloop()