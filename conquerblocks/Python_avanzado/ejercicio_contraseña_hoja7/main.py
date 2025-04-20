
#importar modulos
import customtkinter as ctk
from tkinter import messagebox
import validador
import generador

#creamos la clase PasswordApp
class PasswordApp:
    def __init__(self):
        # Configuración inicial de la ventana
        self.root = ctk.CTk()
        self.root.title("Generador y Validador de Contraseñas / PolixDev / ConquerBlocks")
        self.root.geometry("800x700")
        
        # Configuración del tema
        ctk.set_appearance_mode("system")  # "system", "dark" o "light"
        ctk.set_default_color_theme("blue")
        
        # Container principal con scroll
        self.main_container = ctk.CTkScrollableFrame(self.root)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título principal
        self.create_title()
        
        # Frames principales
        self.create_validation_frame()
        self.create_generation_frame()
        self.create_result_frame()
        
        # Variables de estado
        self.password_strength = {
            'length': False,
            'uppercase': False,
            'lowercase': False,
            'numbers': False,
            'special': False
        }
#creamos el titulo
    def create_title(self):
        title_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        title_frame.pack(fill="x", pady=10)
        
        ctk.CTkLabel(
            title_frame,
            text="Generador y Validador de Contraseñas",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack()
        
        ctk.CTkLabel(
            title_frame,
            text="",
            font=ctk.CTkFont(size=14)
        ).pack()
#creamos el frame de validacion
    def create_validation_frame(self):
        self.validation_frame = ctk.CTkFrame(self.main_container)
        self.validation_frame.pack(fill="x", pady=15, padx=10)
        
        # Título de la sección
        ctk.CTkLabel(
            self.validation_frame,
            text="Validación de Contraseña",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)
        
        # Campo de contraseña
        self.password_entry = ctk.CTkEntry(
            self.validation_frame,
            placeholder_text="Introduce tu contraseña",
            width=350,
            show="•",
            height=35
        )
        self.password_entry.pack(pady=10)
        
        # Botón mostrar/ocultar
        self.show_password = ctk.CTkCheckBox(
            self.validation_frame,
            text="Mostrar contraseña",
            command=self.toggle_password_visibility
        )
        self.show_password.pack(pady=5)
        
        # Indicadores de fortaleza
        self.strength_frame = ctk.CTkFrame(self.validation_frame, fg_color="transparent")
        self.strength_frame.pack(fill="x", padx=20, pady=10)
        
        # Crear indicadores de requisitos
        self.strength_indicators = {}
        requirements = {
            'length': '8+ caracteres',
            'uppercase': 'Mayúsculas',
            'lowercase': 'Minúsculas',
            'numbers': 'Números',
            'special': 'Caracteres especiales'
        }
        
        for key, text in requirements.items():
            indicator = ctk.CTkLabel(
                self.strength_frame,
                text="❌ " + text,
                font=ctk.CTkFont(size=12)
            )
            indicator.pack(anchor="w", pady=2)
            self.strength_indicators[key] = indicator
        
        # Botón validar
        self.validate_button = ctk.CTkButton(
            self.validation_frame,
            text="Validar Contraseña",
            command=self.validar_password,
            height=40
        )
        self.validate_button.pack(pady=15)
#creamos el frame de generacion
    def create_generation_frame(self):
        self.generation_frame = ctk.CTkFrame(self.main_container)
        self.generation_frame.pack(fill="x", pady=15, padx=10)
        
        ctk.CTkLabel(
            self.generation_frame,
            text="Generador de Contraseñas",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)
        
        # Control de longitud
        length_frame = ctk.CTkFrame(self.generation_frame, fg_color="transparent")
        length_frame.pack(fill="x", padx=20, pady=10)
        
        self.length_var = ctk.StringVar(value="12")
        
        ctk.CTkLabel(
            length_frame,
            text=f"Longitud: {self.length_var.get()} caracteres"
        ).pack(side="left")
        
        self.length_slider = ctk.CTkSlider(
            length_frame,
            from_=8,
            to=32,
            number_of_steps=24,
            command=self.update_length_label,
            variable=ctk.DoubleVar(value=12)
        )
        self.length_slider.pack(side="right", fill="x", expand=True, padx=10)
        
        # Opciones de caracteres
        options_frame = ctk.CTkFrame(self.generation_frame, fg_color="transparent")
        options_frame.pack(fill="x", padx=20, pady=10)
        
        self.mayusculas = ctk.CTkCheckBox(options_frame, text="Mayúsculas (A-Z)")
        self.mayusculas.pack(side="left", padx=10)
        self.mayusculas.select()
        
        self.minusculas = ctk.CTkCheckBox(options_frame, text="Minúsculas (a-z)")
        self.minusculas.pack(side="left", padx=10)
        self.minusculas.select()
        
        options_frame2 = ctk.CTkFrame(self.generation_frame, fg_color="transparent")
        options_frame2.pack(fill="x", padx=20, pady=10)
        
        self.numeros = ctk.CTkCheckBox(options_frame2, text="Números (0-9)")
        self.numeros.pack(side="left", padx=10)
        self.numeros.select()
        
        self.especiales = ctk.CTkCheckBox(options_frame2, text="Especiales (!@#$)")
        self.especiales.pack(side="left", padx=10)
        self.especiales.select()
        
        # Botón generar
        self.generate_button = ctk.CTkButton(
            self.generation_frame,
            text="Generar Contraseña",
            command=self.generar_password,
            height=40
        )
        self.generate_button.pack(pady=15)
#creamos el frame de resultados
    def create_result_frame(self):
        self.result_frame = ctk.CTkFrame(self.main_container)
        self.result_frame.pack(fill="x", pady=15, padx=10)
        
        ctk.CTkLabel(
            self.result_frame,
            text="Contraseña Generada",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=10)
        
        self.resultado_entry = ctk.CTkEntry(
            self.result_frame,
            width=350,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        self.resultado_entry.pack(pady=10)
        
        buttons_frame = ctk.CTkFrame(self.result_frame, fg_color="transparent")
        buttons_frame.pack(pady=10)
        
        self.copy_button = ctk.CTkButton(
            buttons_frame,
            text="Copiar al Portapapeles",
            command=self.copiar_al_portapapeles,
            height=40
        )
        self.copy_button.pack(side="left", padx=5)
        
        self.save_button = ctk.CTkButton(
            buttons_frame,
            text="Guardar Contraseña",
            command=self.guardar_contrasena,
            height=40
        )
        self.save_button.pack(side="left", padx=5)
#actualizamos la longitud de la contraseña
    def update_length_label(self, value):
        self.length_var.set(str(int(value)))
        for widget in self.generation_frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and "Longitud:" in widget.cget("text"):
                widget.configure(text=f"Longitud: {int(value)} caracteres")

    def update_strength_indicators(self, password):
        # Actualizar indicadores según la contraseña
        self.password_strength['length'] = len(password) >= 8
        self.password_strength['uppercase'] = any(c.isupper() for c in password)
        self.password_strength['lowercase'] = any(c.islower() for c in password)
        self.password_strength['numbers'] = any(c.isdigit() for c in password)
        self.password_strength['special'] = any(not c.isalnum() for c in password)
        
        for key, indicator in self.strength_indicators.items():
            text = indicator.cget("text")[2:]  # Obtener el texto sin el emoji
            indicator.configure(text=("✅ " if self.password_strength[key] else "❌ ") + text)
#mostramos la contraseña
    def toggle_password_visibility(self):
        current_show = self.password_entry.cget("show")
        self.password_entry.configure(show="" if current_show == "•" else "•")
#validamos la contraseña
    def validar_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Error", "Por favor, introduce una contraseña")
            return
        
        self.update_strength_indicators(password)
        
        if all(self.password_strength.values()):
            messagebox.showinfo("Éxito", "¡La contraseña cumple todos los requisitos!")
        else:
            messagebox.showwarning("Advertencia", "La contraseña no cumple todos los requisitos")
#generamos la contraseña
    def generar_password(self):
        try:
            longitud = int(self.length_var.get())
            if not any([self.mayusculas.get(), self.minusculas.get(), 
                       self.numeros.get(), self.especiales.get()]):
                messagebox.showwarning("Error", "Selecciona al menos un tipo de carácter")
                return
                
            nueva_password = generador.generar_contrasena(
                longitud,
                self.mayusculas.get(),
                self.minusculas.get(),
                self.numeros.get(),
                self.especiales.get()
            )
            self.resultado_entry.delete(0, "end")
            self.resultado_entry.insert(0, nueva_password)
            self.update_strength_indicators(nueva_password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copiar_al_portapapeles(self):
        password = self.resultado_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles")
        else:
            messagebox.showwarning("Error", "No hay contraseña para copiar")
#guardamos la contraseña
    def guardar_contrasena(self):
        password = self.resultado_entry.get()
        if not password:
            messagebox.showwarning("Error", "No hay contraseña para guardar")
            return
        
        try:
            with open("passwords.txt", "a") as file:
                from datetime import datetime
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Fecha: {fecha} - Contraseña: {password}\n")
            messagebox.showinfo("Éxito", "Contraseña guardada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar la contraseña: {str(e)}")
#creamos el bucle principal
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordApp()
    app.run()

    