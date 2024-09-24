import tkinter as tk
import time

class MiniGameTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-jeu : Timer")
        
        self.time_left = 30.0  # 30 secondes pour commencer
        self.running = False
        
        self.label = tk.Label(root, text=f"Temps restant : {self.time_left:.2f} secondes", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Démarrer le timer", command=self.start_timer, font=("Helvetica", 18))
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(root, text="Arrêter le timer", command=self.stop_timer, font=("Helvetica", 18))
        self.stop_button.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Réinitialiser le timer", command=self.reset_timer, font=("Helvetica", 18))
        self.reset_button.pack(pady=10)
        
        self.update_timer()

    def start_timer(self):
        self.running = True
    
    def stop_timer(self):
        self.running = False
    
    def reset_timer(self):
        self.time_left = 30.0
        self.label.config(text=f"Temps restant : {self.time_left:.2f} secondes")
    
    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 0.1  # Réduire de 0.1 secondes à chaque mise à jour
            self.label.config(text=f"Temps restant : {self.time_left:.2f} secondes")
        elif self.time_left <= 0:
            self.running = False
            self.label.config(text="Temps écoulé !")
        
        self.root.after(100, self.update_timer)  # Mise à jour toutes les 100 ms

# Créer la fenêtre du jeu
root = tk.Tk()
game = MiniGameTimer(root)
root.mainloop()
