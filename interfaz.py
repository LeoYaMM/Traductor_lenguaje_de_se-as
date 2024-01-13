import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "usuario" and password == "contraseña": 
        clear_gui()
        show_camera_button()
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

def clear_gui():
    login_frame.pack_forget()
    
canvas_width = 800
canvas_height = 600
rect_width = 400
rect_height = 300
center_x = canvas_width / 2
center_y = canvas_height / 2
x1 = center_x - rect_width / 2
y1 = center_y - rect_height / 2
x2 = center_x + rect_width / 2
y2 = center_y + rect_height / 2


def show_camera_button():
    if not hasattr(window, 'rect'):
        window.rect = tk.Canvas(window, width=800, height=600, bg='#5DADE2')
        window.rect.create_rectangle(x1, y1, x2, y2, fill="#1B4F72")
        window.rect.bind("<Button-1>", open_camera)
    window.rect.pack(pady=(0,0))

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

background_image = tk.PhotoImage(file="fondo.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

login_frame = tk.Frame(window)
login_frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(login_frame, text="Nombre de usuario").pack()
entry_username = tk.Entry(login_frame)
entry_username.pack()

tk.Label(login_frame, text="Contraseña").pack()
entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

button_login = tk.Button(login_frame, text="Ingresar", command=login)
button_login.pack()

window.mainloop()
