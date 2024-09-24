[🔓 GODMODE]  

### Cheat Engine - Manipuler les Timers et la Vitesse du Jeu

**Clés principales** :
1. **Comprendre les timers dans les jeux** : De nombreux jeux utilisent des compteurs ou des timers pour gérer le temps de jeu, des actions comme le cooldown (délai) entre deux actions ou même le temps global (comme un chrono).
2. **Recherche de timers** : Les timers sont généralement stockés sous forme de **Float** ou **Double** (Double Recommander) (valeurs décimales) car ils doivent représenter des durées précises, souvent en secondes. Dans certains cas, ils peuvent être stockés sous forme d'entiers, mais cela dépend du jeu.
3. **Modification de la vitesse de jeu** : Tu peux utiliser Cheat Engine pour modifier directement les valeurs d'un timer (par exemple, réduire un délai d'attente) ou utiliser la fonction **Speedhack** intégrée pour accélérer ou ralentir globalement le jeu.

### Étapes pratiques :
1. **Identifier le timer** :
   - Si tu vois un décompte dans le jeu (par exemple un chrono), tu peux faire une première recherche en tant que **Float** ou **Double** avec la valeur exacte du timer (par exemple, "30.0").
   - Si tu ne connais pas la valeur exacte, commence par une **recherche de valeur inconnue**, puis affines les résultats en cherchant des valeurs **diminuées** (lorsque le timer diminue) ou **augmentées** (si le timer augmente).

2. **Modifier la vitesse du jeu** :
   - Une fois le timer trouvé, tu peux le modifier directement (par exemple passer un timer de 30 secondes à 1 seconde).
   - Alternativement, utilise la fonctionnalité **Speedhack** de Cheat Engine pour accélérer ou ralentir le jeu entier. Par exemple, passer à une vitesse de **0.5x** pour ralentir le jeu, ou à **2x** pour l’accélérer.

### Exemple d'utilisation dans Cheat Engine :
- **Cooldown sur une action** : Si tu as un jeu où tu dois attendre 5 secondes entre deux attaques, tu peux chercher ce délai de 5 secondes (en **Float**) et le modifier pour réduire ou éliminer le délai.
- **Chrono ou timer de jeu** : Si un niveau ou une mission a un temps limité (comme 2 minutes), tu peux chercher le chrono et soit le geler, soit l'augmenter pour te donner plus de temps.

---

### Création d'un mini-jeu en Python avec un Timer

Voici un mini-jeu avec un chrono pour que tu puisses t'entraîner à manipuler le temps avec Cheat Engine.

```python
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
```

### Explication du mini-jeu :
- **Chrono** : Le jeu commence avec un chrono de **30 secondes**, qui diminue progressivement. Tu peux démarrer, arrêter et réinitialiser le timer avec des boutons.
- **Mise à jour en temps réel** : Le timer se met à jour toutes les 100 millisecondes, et il réduit de **0.1 seconde** à chaque cycle.
- **Modification avec Cheat Engine** : Tu peux utiliser Cheat Engine pour rechercher la valeur du timer (qui commence à 30.00) en tant que **Float** et essayer de la modifier. Par exemple, passer de 30.0 à 5.0 pour accélérer la fin du chrono, ou même à un nombre négatif pour prolonger le temps de jeu.

### Comment utiliser Cheat Engine avec ce mini-jeu :
1. Lance le jeu en exécutant le script Python.
2. Ouvre Cheat Engine et attache-le au processus Python.
3. Recherchez la valeur **30.0** (le temps restant) en tant que **Float** dans Cheat Engine.
4. Modifiez la valeur du timer pour qu'il se réduise ou se prolonge comme tu le souhaites.
5. Tu peux également essayer d'utiliser la fonction **Speedhack** pour ralentir ou accélérer la vitesse de décompte du timer.