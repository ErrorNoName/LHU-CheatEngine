import tkinter as tk

class MiniGameText:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini-jeu : Modification de texte")
        
        self.message = "Bienvenue dans le jeu !"
        self.label = tk.Label(root, text=self.message, font=("Helvetica", 24))
        self.label.pack(pady=20)
        
        self.button = tk.Button(root, text="Changer le message", command=self.change_message, font=("Helvetica", 18))
        self.button.pack(pady=20)
        
        self.message_list = ["C'est trop cool !", "Cheat Engine en action", "Modification en direct", "Amuse-toi bien !"]
        self.index = 0
        
    def change_message(self):
        self.message = self.message_list[self.index]
        self.label.config(text=self.message)
        self.index = (self.index + 1) % len(self.message_list)

# Créer la fenêtre du jeu
root = tk.Tk()
game = MiniGameText(root)
root.mainloop()
