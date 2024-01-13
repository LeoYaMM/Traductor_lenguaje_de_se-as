import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "contraseña":  # Reemplazar con la lógica de autenticación real
        clear_gui()
        show_camera_button()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def clear_gui():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_username.pack_forget()
    entry_password.pack_forget()
    button_login.pack_forget()

def show_camera_button():
    rect = tk.Canvas(window, width=200, height=100)
    rect.pack()
    rect.create_rectangle(50, 25, 150, 75, fill="blue")
    rect.bind("<Button-1>", open_camera)  # Evento para hacer clic en el rectángulo

def open_camera(event):
    messagebox.showinfo("Info", "Abriría la cámara aquí")
    


window = tk.Tk()
window.title("Sistema de Login")

window_width = 800
window_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

login_frame = tk.Frame(window)
login_frame.place(relx=0.5, rely=0.5, anchor='center')

background_image = tk.PhotoImage(file="fondo.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

tk.Label(window, text="Nombre de usuario").pack()
entry_username = tk.Entry(window)
entry_username.pack()

tk.Label(window, text="Contraseña").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

button_login = tk.Button(window, text="Ingresar", command=login)
button_login.pack()

window.mainloop()
