import tkinter as tk
from tkinter import ttk  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sys
from Game import *

class Main:
    def __init__(self):
        self.num_simulations = 0  # Variable global para almacenar el número de simulaciones
        self.game = None
        self.root = tk.Tk()
        self.root.geometry("700x500")
        self.root.title("Un problema Montecarlo")

        # Colores y estilo
        bg_color = '#f0f0f0'
        btn_color = '#2596be'
        btn_text_color = 'white'
        font_label = ('Arial', 12)
        font_button = ('Arial', 10, 'bold')

        # Crear y configurar el frame superior
        self.frameTop = tk.Frame(self.root, width=800, height=300, bg=bg_color)
        self.frameTop.pack(side=tk.TOP, expand=True)

        # Etiquetas y campos de entrada para los parámetros
        self.sim_label = tk.Label(self.frameTop, text="Numero de juegos a realizar:", bg=bg_color, font=font_label)
        self.sim_label.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.sim_entry = tk.Entry(self.frameTop)
        self.sim_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botón de simulación
        self.simulation_button = tk.Button(self.frameTop, text="Comenzar Juegos", command=self.start_simulation, bg=btn_color, fg=btn_text_color, font=font_button)
        self.simulation_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.men_label = tk.Label(self.frameTop, text="Numero de hombres que ganaron en total:", bg=bg_color, font=font_label)
        self.men_label.grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.men_count = tk.Label(self.frameTop, text="", bg=bg_color)  # Etiqueta vacía para contar hombres
        self.men_count.grid(row=3, column=1, padx=10, pady=10)

        self.women_label = tk.Label(self.frameTop, text="Numero de mujeres que ganaron en total:", bg=bg_color, font=font_label)
        self.women_label.grid(row=4, column=0, sticky='w', padx=10, pady=10)
        self.women_count = tk.Label(self.frameTop, text="", bg=bg_color)  # Etiqueta vacía para contar mujeres
        self.women_count.grid(row=4, column=1, padx=10, pady=10)

        # Botones adicionales
        self.exp_button = tk.Button(self.frameTop, text="Arqueros con más experiencia", command=self.show_experience, bg=btn_color, fg=btn_text_color, font=font_button)
        self.exp_button.grid(row=5, column=0, padx=10, pady=10)
        self.luck_button = tk.Button(self.frameTop, text="Arqueros con más suerte", command=self.show_luck, bg=btn_color, fg=btn_text_color, font=font_button)
        self.luck_button.grid(row=5, column=1, padx=10, pady=10)
        self.groups_button = tk.Button(self.frameTop, text="Equipos ganadores", command=self.show_groups, bg=btn_color, fg=btn_text_color, font=font_button)
        self.groups_button.grid(row=6, column=0, padx=10, pady=10)
        self.genders_button = tk.Button(self.frameTop, text="Genero con mas victorias x juego", command=self.show_genders, bg=btn_color, fg=btn_text_color, font=font_button)
        self.genders_button.grid(row=6, column=1, padx=10, pady=10)

        # Combobox para seleccionar arqueros
        self.player_options = ['A{}'.format(i) for i in range(1, 11)]
        self.archer_combo = ttk.Combobox(self.frameTop, values=self.player_options, state='readonly')
        self.archer_combo.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.archer_combo.set('A1')  # Valor predeterminado
        self.archer_combo.bind("<<ComboboxSelected>>", self.plot)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Ejecutar la ventana
        self.root.mainloop()
    
    def on_closing(self):
        self.root.destroy()  # Cerrar la ventana principal
        sys.exit()  # Salir del programa

    # Funciones para mostrar información adicional
    def show_experience(self):
        if self.game is not None:
            experience_window = tk.Toplevel(self.root)
            experience_window.title("Registros de exp")
            experience_text = tk.Text(experience_window, height=20, width=50)
            experience_text.pack()
            for record in self.game.most_experienced_archers:
                experience_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de experiencia disponibles")

    def show_luck(self):
        if self.game is not None:
            lucky_window = tk.Toplevel(self.root)
            lucky_window.title("Registros de suerte")
            lucky_text = tk.Text(lucky_window, height=20, width=50)
            lucky_text.pack()
            for record in self.game.luckiest_archers:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de suerte disponibles")

    def show_groups(self):
        if self.game is not None:
            teams_window = tk.Toplevel(self.root)
            teams_window.title("Registros de ganadores")
            lucky_text = tk.Text(teams_window, height=20, width=50)
            lucky_text.pack()
            for record in self.game.champions_teams_with_scores:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de ganadores disponibles")

    def show_genders(self):
        if self.game is not None:
            teams_window = tk.Toplevel(self.root)
            teams_window.title("Registros de victorias x género")
            lucky_text = tk.Text(teams_window, height=20, width=60)
            lucky_text.pack()
            for record in self.game.winner_gender_per_game:
                lucky_text.insert(tk.END, record + "\n")
        else:
            print("No hay registros de victorias x género disponibles")

    # Iniciar la simulación
    def start_simulation(self):
        self.num_simulations = int(self.sim_entry.get())
        print(f"Empezar con {self.num_simulations} simulaciones.")
        self.game = Game(self.num_simulations)
        print('SIMULACION FINALIZADA')
        self.plot()
        self.men_count.config(text=f"{self.game.count_men}")
        self.women_count.config(text=f"{self.game.count_women}")

    # Graficar los datos
    def plot(self, event=None):
        selected_value = self.archer_combo.get()  # Obtener el valor seleccionado
        selected_index = self.player_options.index(selected_value)

        if self.game != None:
            x = list(range(1, len(self.game.archers_scores[selected_index])+1))
            y = self.game.archers_scores[selected_index]

            # Crear una nueva ventana emergente
            graph_window = tk.Toplevel(self.root)
            graph_window.title(f'Gráfico de {selected_value}')

            fig, ax = plt.subplots()
            ax.plot(x, y, marker='o', linestyle='-', color='g')  # Gráfico de líneas con estilo
            ax.set_title(f'Puntajes en cada juego del arquero {selected_value}', fontsize=14, fontweight='bold')
            ax.set_xlabel('Juegos')
            ax.set_ylabel('Puntajes')

            # Mostrar el gráfico en la ventana emergente
            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.get_tk_widget().pack()
            canvas.draw()
        else:
            print("No se ha iniciado ninguna simulación")


if __name__ == "__main__":
    main = Main()
