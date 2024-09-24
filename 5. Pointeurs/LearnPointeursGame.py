import tkinter as tk

class MiniGameResources:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-jeu : Ressources")
        
        self.gold = 100  # Commence avec 100 pièces d'or
        self.label = tk.Label(root, text=f"Or : {self.gold} pièces", font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Ajouter 10 pièces d'or", command=self.add_gold, font=("Helvetica", 18))
        self.button.pack(pady=20)
        
        self.reset_button = tk.Button(root, text="Réinitialiser l'or", command=self.reset_gold, font=("Helvetica", 18))
        self.reset_button.pack(pady=10)
    
    def add_gold(self):
        self.gold += 10
        self.label.config(text=f"Or : {self.gold} pièces")
        
    def reset_gold(self):
        self.gold = 100
        self.label.config(text=f"Or : {self.gold} pièces")

# Créer la fenêtre du jeu
root = tk.Tk()
game = MiniGameResources(root)
root.mainloop()
