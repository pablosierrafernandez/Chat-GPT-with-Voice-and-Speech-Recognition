import tkinter as tk
from tkinter import ttk
def open_config_window():
    # Crear la ventana de configuración
    config_window = tk.Toplevel(root)
    config_window.title("Configuración")

    # Crear el marco de la ventana de configuración
    config_frame = tk.Frame(config_window, bd=2, relief=tk.GROOVE)
    config_frame.pack(padx=10, pady=10)

    # Crear el label y el entry para la clave
    key_label = tk.Label(config_frame, text="Clave:", font=("Helvetica", 12))
    key_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    key_entry = tk.Entry(config_frame, font=("Helvetica", 12))
    key_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

    # Crear el combo box para elegir el idioma
    language_label = tk.Label(config_frame, text="Idioma:", font=("Helvetica", 12))
    language_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    language_options = ["Español", "Inglés", "Francés"]
    language_combobox = ttk.Combobox(config_frame, values=language_options)
    language_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="we")

    # Función para guardar la configuración
    def save_config():
        # Aquí iría el código para guardar la configuración
        config_window.destroy()

    # Crear los botones de guardar y cancelar
    save_button = tk.Button(config_frame, text="Guardar", font=("Helvetica", 12), command=save_config)
    save_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    cancel_button = tk.Button(config_frame, text="Cancelar", font=("Helvetica", 12), command=config_window.destroy)
    cancel_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")
# Crear la ventana principal
root = tk.Tk()
root.title("Chat")

# Crear el título de la ventana
title_label = tk.Label(root, text="Chat", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Crear el marco del chat
chat_frame = tk.Frame(root, bd=2, relief=tk.GROOVE)
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)



# Crear el botón de configuración
config_button = tk.Button(root, text="Configuración", font=("Helvetica", 12),command=open_config_window)
config_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Función para abrir la ventana de configuración

    
    # Ejecutar la aplicación
root.mainloop()