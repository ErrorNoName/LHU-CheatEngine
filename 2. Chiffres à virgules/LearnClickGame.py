import tkinter as tk

class MiniGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-jeu : Clics et Points")
        
        self.points = 0.0
        self.label = tk.Label(root, text=f"Points : {self.points}", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Cliquez pour ajouter 0.25 points", command=self.add_points, font=("Helvetica", 18))
        self.button.pack(pady=20)
        
        self.reset_button = tk.Button(root, text="Réinitialiser", command=self.reset_points, font=("Helvetica", 18))
        self.reset_button.pack(pady=10)
        
    def add_points(self):
        self.points += 0.25
        self.label.config(text=f"Points : {self.points:.2f}")
        
    def reset_points(self):
        self.points = 0.0
        self.label.config(text=f"Points : {self.points:.2f}")

# Créer la fenêtre du jeu
root = tk.Tk()
game = MiniGame(root)
root.mainloop()
