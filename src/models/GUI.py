import tkinter as tk
from tkinter import ttk  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys

from Game import *

import tkinter as tk

class GUI:
    def __init__(self):
        self.num_simulations = 0  # Variable global para almacenar el número de simulaciones
        self.game = None
        self.root = tk.Tk()
        self.root.geometry("800x700")
        self.root.title("Un problema Montecarlo")

        # Create and pack the top frame
        self.frameTop = tk.Frame(self.root, width=800, height=300)
        self.frameTop.pack(side=tk.TOP, expand=True)

        # Labels and entry fields for the additional fields
        self.sim_label = tk.Label(self.frameTop, text="Ingrese el numero de simulaciones:")
        self.sim_label.grid(row=0, column=0, padx=5, pady=5)
        self.sim_entry = tk.Entry(self.frameTop)
        self.sim_entry.grid(row=0, column=1, padx=5, pady=5)

        self.men_label = tk.Label(self.frameTop, text="# de hombres que ganaron:")
        self.men_label.grid(row=1, column=0, padx=5, pady=5)
        self.men_count = tk.Label(self.frameTop, text="")  # Empty label for men count
        self.men_count.grid(row=1, column=1, padx=5, pady=5)

        self.women_label = tk.Label(self.frameTop, text="# de mujeres que ganaron:")
        self.women_label.grid(row=2, column=0, padx=5, pady=5)
        self.women_count = tk.Label(self.frameTop, text="")  # Empty label for women count
        self.women_count.grid(row=2, column=1, padx=5, pady=5)

        # Additional buttons
        self.exp_button = tk.Button(self.frameTop, text="Mostrar arqueros con más experiencia", command=self.show_experience)
        self.exp_button.grid(row=3, column=0, padx=5, pady=5)
        self.luck_button = tk.Button(self.frameTop, text="Mostrar arqueros con más suerte", command=self.show_luck)
        self.luck_button.grid(row=3, column=1, padx=5, pady=5)
        self.groups_button = tk.Button(self.frameTop, text="Mostrar equipos ganadores", command=self.show_groups)
        self.groups_button.grid(row=3, column=2, padx=5, pady=5)

        self.player_options = ['J{}'.format(i) for i in range(1, 11)]
        self.archer_combo = ttk.Combobox(self.frameTop, values=self.player_options, state='readonly')
        self.archer_combo.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        
        # Establecer J1 como el valor predeterminado
        self.archer_combo.set('J1')

        # Asociar evento a cambio de selección en el ComboBox
        self.archer_combo.bind("<<ComboboxSelected>>", self.plot)

        # Start Simulation Button
        self.simulation_button = tk.Button(self.frameTop, text="Comenzar Simulación", command=self.start_simulation)
        self.simulation_button.grid(row=5, columnspan=3, padx=5, pady=5)


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Run the window
        self.root.mainloop()
        
    
    def on_closing(self):
        # Manejar el cierre de la ventana principal
        self.root.destroy()  # Cerrar la ventana principal
        sys.exit()  # Salir del programa

    # Define functions for the additional buttons
    def show_experience(self):
        if self.game is not None:
            # Crear una nueva ventana emergente
            experience_window = tk.Toplevel(self.root)
            experience_window.title("Registros de exp")

            # Crear un widget de texto para mostrar el registro de experiencia
            experience_text = tk.Text(experience_window, height=20, width=50)
            experience_text.pack()

            # Insertar los registros de experiencia en el widget de texto
            for record in self.game.most_experienced_archers:
                experience_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def show_luck(self):
        if self.game is not None:
            # Crear una nueva ventana emergente
            lucky_window = tk.Toplevel(self.root)
            lucky_window.title("Registros de suerte")

            # Crear un widget de texto para mostrar el registro de experiencia
            lucky_text = tk.Text(lucky_window, height=20, width=50)
            lucky_text.pack()

            # Insertar los registros de experiencia en el widget de texto
            for record in self.game.luckiest_archers:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def show_groups(self):
        if self.game is not None:
            # Crear una nueva ventana emergente
            teams_window = tk.Toplevel(self.root)
            teams_window.title("Registros de suerte")

            # Crear un widget de texto para mostrar el registro de suerte
            lucky_text = tk.Text(teams_window, height=20, width=50)
            lucky_text.pack()

            # Insertar los registros de suerte en el widget de texto
            for record in self.game.champions_teams_with_scores:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de suerte disponibles")

    def start_simulation(self):
        self.num_simulations = int(self.sim_entry.get())
        print(f"Empezar con {self.num_simulations} simulaciones.")
        self.game = Game(self.num_simulations)
        print("Archer Scores: ", self.game.archers_scores)
        self.plot()
        self.men_count.config(text=f"{self.game.count_men}")
        self.women_count.config(text=f"{self.game.count_women}")


    def plot(self, event=None):
        selected_value = self.archer_combo.get()  # Obtener el valor seleccionado en el ComboBox
        selected_index = self.player_options.index(selected_value)  # Obtener el índice del valor seleccionado

        if self.game != None: 
            x = []
            for i in range(1, len(self.game.archers_scores[selected_index])+1):
                x.append(i)
            
            y = self.game.archers_scores[selected_index]

            fig, ax = plt.subplots()
            ax.bar(x, y)  # Cambiar a ax.bar para un gráfico de barras
            ax.set_title(f'Puntuaciones en cada juego del arquero {selected_value}')
            ax.set_xlabel('Juegos')
            ax.set_ylabel('Puntuaciones')

            # Clear previous plot if exists
            for widget in self.frameTop.winfo_children():
                if isinstance(widget, FigureCanvasTkAgg):
                    widget.get_tk_widget().destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.frameTop)
            canvas.get_tk_widget().grid(row=6, columnspan=3, padx=5, pady=5)  # Use grid instead of pack
            canvas.draw()
        else:
            print("No se ha iniciado ninguna simulación")



if __name__ == "__main__":
    gui = GUI()