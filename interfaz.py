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
        
def open_registration_form():
    register_window = tk.Toplevel(window)
    register_window.title("Formulario de Registro")
    
    background_color = "#5DADE2"
    register_window.configure(bg=background_color)
    
    register_window_width = 400
    register_window_height = 300
    
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
    center_x = int((screen_width - register_window_width) / 2)
    center_y = int((screen_height - register_window_height) / 2)

    register_window.geometry(f'{register_window_width}x{register_window_height}+{center_x}+{center_y}')
    
    registration_frame = tk.Frame(register_window, bg=background_color)
    registration_frame.pack(pady=50) 

    tk.Label(registration_frame, text="Nombre").pack()
    entry_name = tk.Entry(registration_frame)
    entry_name.pack()

    tk.Label(registration_frame, text="Correo electrónico").pack()
    entry_email = tk.Entry(registration_frame)
    entry_email.pack()

    tk.Label(registration_frame, text="Contraseña").pack()
    entry_password = tk.Entry(registration_frame, show="*")
    entry_password.pack()

    tk.Label(registration_frame, text="Confirmar contraseña").pack()
    entry_confirm_password = tk.Entry(registration_frame, show="*")
    entry_confirm_password.pack()

    button_submit = tk.Button(registration_frame, text="Registrarse", command=lambda: register(entry_name.get(), entry_email.get(), entry_password.get(), entry_confirm_password.get()))
    button_submit.pack()
        
def register(name, email, password, confirm_password):
    messagebox.showinfo("Registro", f"Datos recibidos:\nNombre: {name}\nCorreo electrónico: {email}")

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
window.title("Sistema Traductor de Lengua de Señas")

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

button_register = tk.Button(login_frame, text="Registrate!", command=open_registration_form)
button_register.pack(pady=10)

window.mainloop()
