[🔓 Learn HackGame Lvl1]  

### Cheat Engine - Rechercher et Modifier des Valeurs à Virgule Flottante

**Clés principales** :
1. **Identifier le type de données** : Les valeurs décimales sont souvent stockées sous forme de "Float" (32-bit) ou "Double" (64-bit).
2. **Recherche de valeur** : Au lieu d'une recherche "Exact Value" comme tu fais avec les valeurs entières, tu dois utiliser la recherche en **"Type: Float"** ou **"Type: Double"**.
3. **Approche de recherche progressive** : Si tu ne connais pas la valeur exacte, tu peux utiliser une recherche de "valeur inconnue" suivie de recherches de "valeurs augmentées" ou "réduites" selon le changement dans le jeu.
4. **Précision des flottants** : Lorsque tu recherches des valeurs décimales, il peut y avoir une petite différence entre la valeur que tu vois à l’écran et celle stockée dans la mémoire. Par exemple, une valeur que tu vois comme "12.35" pourrait être en réalité "12.3499999" en mémoire. Pour contourner cela, utilise la recherche de "valeurs approximatives" ou utilise un écart minime dans la précision (par exemple, 12.34 à 12.36).

### Étapes pratiques :
1. **Démarrer une première analyse** :
   - Lancer Cheat Engine et attacher le processus du jeu.
   - Mettre la recherche sur **"Float"** ou **"Double"**.
   - Si la valeur affichée est "12.35", entre "12.35" dans la recherche.

2. **Refiner les résultats** :
   - Quand la valeur change dans le jeu (par exemple elle passe à 13.45), fais une nouvelle analyse en sélectionnant **"Augmenté"**.
   - Continue ce processus jusqu’à trouver l’adresse.

3. **Modifier la valeur** :
   - Une fois que tu as localisé l'adresse correcte, tu peux la modifier directement comme tu le ferais pour des valeurs entières.

---

### Création d'un mini-jeu en Python

Je vais te créer un mini-jeu où tu cliques pour augmenter tes points avec des décimales. Tu pourras ensuite utiliser Cheat Engine pour t'entraîner à modifier les valeurs.

```python
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
```

### Explication :
- **Interface graphique avec Tkinter** : Le mini-jeu utilise une fenêtre Tkinter avec un bouton pour ajouter des points. Chaque clic ajoute **0.25 points** et la valeur est affichée avec **deux décimales**.
- **Fonctionnement des clics** : Chaque clic sur le bouton met à jour les points, qui sont affichés en temps réel.
- **Réinitialisation** : Un bouton de réinitialisation remet les points à zéro, ce qui est utile si tu veux tester plusieurs fois avec Cheat Engine.

### Comment utiliser Cheat Engine avec ce mini-jeu :
1. Lance le jeu en exécutant le script Python.
2. Ouvre Cheat Engine et attache-le au processus Python.
3. Cherche la valeur des points dans Cheat Engine en utilisant le type **"Float"**.
4. Modifie les points dans Cheat Engine et observe le changement dans le jeu.

Ce mini-jeu te permettra de t'exercer avec des valeurs à virgule flottante et de mieux comprendre comment les identifier et les manipuler dans Cheat Engine.