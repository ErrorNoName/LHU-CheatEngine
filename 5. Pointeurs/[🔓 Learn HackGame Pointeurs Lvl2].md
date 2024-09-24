[🔓 Learn HackGame Pointeurs Lvl2]  

### Cheat Engine - Manipuler des ressources et l'utilisation des pointeurs

**Clés principales** :
1. **Identifier les variables accumulables** : Les jeux utilisent souvent des variables pour stocker des ressources (argent, munitions, etc.). Ces valeurs peuvent être stockées en **entier (Integer)** ou en **Flottant (Float)**, selon le type de données.
2. **Recherche initiale** : Comme tu le fais déjà pour des valeurs simples (par exemple, de l'argent ou des points), tu peux utiliser une **recherche exacte** pour trouver la valeur actuelle de la ressource que tu veux modifier.
3. **Problème des valeurs dynamiques** : Parfois, une fois que tu trouves l'adresse, elle change lorsque tu redémarres le jeu ou passes à un autre niveau. Cela se produit parce que les jeux modernes allouent dynamiquement des variables en mémoire. Pour contourner cela, tu dois utiliser des **pointeurs**.
4. **Utilisation des pointeurs** : Un pointeur est une adresse en mémoire qui renvoie à une autre adresse où est réellement stockée la variable (comme de l'argent). Cheat Engine permet de "suivre" ces pointeurs pour identifier une adresse qui ne change pas entre les sessions de jeu.

### Étapes pratiques :
1. **Première recherche** :
   - Ouvre Cheat Engine et attache-le au processus du jeu.
   - Recherchez la valeur exacte de la ressource que tu souhaites modifier (par exemple, si tu as **500 pièces d'or**, recherche **500** en tant qu'entier).
   
2. **Modification de la ressource** :
   - Après avoir trouvé la valeur correcte, modifie-la directement dans Cheat Engine (par exemple, remplace les **500 pièces d'or** par **99999**).
   
3. **Utilisation de pointeurs** (si la valeur change à chaque redémarrage du jeu) :
   - Si l'adresse que tu as trouvée n'est pas permanente, fais un clic droit sur l'adresse et sélectionne **"Pointer scan for this address"**. Cela va rechercher toutes les adresses qui pointent vers cette valeur.
   - Tu devras parfois redémarrer le jeu ou changer de niveau et refaire la recherche de pointeurs pour affiner tes résultats.
   - Une fois que tu as trouvé un pointeur stable, tu peux l'utiliser pour modifier la valeur à chaque fois que tu joues, même après un redémarrage.

### Exemple d'application dans un jeu :
- **Argent** : Imagine que tu joues à un jeu de gestion où tu as 1000 unités d'or. En utilisant une recherche de valeur exacte (en tant qu'**Integer**), tu trouves l'adresse et modifie l'or à une valeur élevée, comme 999999.
- **Pointeur** : Si tu redémarres le jeu et que l'adresse change, utilise un pointeur pour trouver une adresse qui reste la même entre les sessions.

---

### Création d'un mini-jeu en Python avec des ressources modifiables

Pour t'entraîner, voici un mini-jeu simple où tu accumules des pièces d'or en cliquant, et tu peux ensuite utiliser Cheat Engine pour modifier la quantité d'or.

```python
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
```

### Explication du mini-jeu :
- **Accumulation de ressources** : Tu commences avec **100 pièces d'or**, et chaque clic sur le bouton ajoute **10 pièces d'or**.
- **Modification avec Cheat Engine** : Tu peux rechercher la valeur de **100** en tant qu'**Integer** dans Cheat Engine et la modifier (par exemple, passer à 10000 pièces d'or).
- **Réinitialisation** : Un bouton te permet de réinitialiser la quantité d'or à **100** pièces, utile pour refaire des tests avec Cheat Engine.

### Comment utiliser Cheat Engine avec ce mini-jeu :
1. Lance le mini-jeu en exécutant le script Python.
2. Ouvre Cheat Engine et attache-le au processus Python.
3. Recherchez la valeur **100** en tant qu'**Integer** pour représenter l'or.
4. Modifie cette valeur (par exemple, mets-la à **9999** pièces).
5. Teste à nouveau le mini-jeu pour voir si la valeur d'or a changé.
6. Si l'adresse change à chaque fois que tu réinitialises le jeu, utilise la méthode des **pointeurs** pour trouver une adresse stable.

---

### Manipuler les ressources dans un jeu réel :
- **Gestion des ressources** : La manipulation de l'argent, des munitions ou d'autres ressources est extrêmement puissante dans les jeux de gestion, de stratégie ou les RPG. Tu peux modifier tes ressources pour accélérer ta progression, supprimer des limitations artificielles ou simplement expérimenter.
- **Problème des valeurs dynamiques** : Dans les jeux plus modernes, les valeurs comme l'argent ou les munitions peuvent être stockées dynamiquement, nécessitant une utilisation intelligente des pointeurs pour assurer que les modifications persistent.