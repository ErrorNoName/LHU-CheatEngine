[🔓 Learn HackGame Text Lvl1]

### Cheat Engine - Changer un texte en direct dans un jeu

**Clés principales** :
1. **Stockage des textes** : Les textes sont généralement stockés sous forme de chaînes de caractères en mémoire. Ils peuvent être encodés en **ASCII** (chaque caractère est représenté par un byte) ou en **UTF-8**/**UTF-16** (chaque caractère peut utiliser plus d'un byte, surtout pour les caractères spéciaux).
2. **Recherche de chaînes de caractères** : Contrairement aux valeurs numériques, tu devras rechercher la chaîne de caractères en tant que **"String"** dans Cheat Engine. Si le jeu utilise des encodages spécifiques, tu devras ajuster la recherche pour correspondre à l'encodage (ex: "Array of bytes" pour UTF-8).
3. **Modifier la longueur du texte** : Si tu modifies un texte en direct, il est préférable de garder la même longueur de chaîne (par exemple, changer "Bonjour" par "Bonsoir" au lieu de "Salut"), sinon cela peut provoquer des corruptions dans la mémoire du jeu.

### Étapes pratiques :
1. **Démarrer une recherche** :
   - Lance Cheat Engine et attache-le au processus du jeu.
   - Mettez le type de recherche sur **"String"** ou **"Array of Bytes"** si tu penses que le texte est en UTF-8 ou UTF-16.
   - Recherchez le texte que tu vois affiché dans le jeu (par exemple, "Score: 0").
   
2. **Trouver le texte** :
   - Si le texte change dans le jeu (par exemple, le score qui passe de "Score: 0" à "Score: 1"), tu peux affiner ta recherche en modifiant la chaîne et en effectuant une nouvelle recherche.
   
3. **Modifier le texte** :
   - Une fois l'adresse trouvée, tu peux éditer la chaîne directement dans Cheat Engine.
   - Veille à ce que la nouvelle chaîne ait la même longueur ou ajuste correctement les bytes si nécessaire.

### Création d'un mini-jeu en Python pour modifier du texte en direct

Voici un mini-jeu en Python où tu pourras t'entraîner à modifier du texte. Le jeu affiche un message à l'écran que tu peux essayer de changer via Cheat Engine.

```python
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
```

### Explication du mini-jeu :
- **Message initial** : Le jeu affiche un message de bienvenue ("Bienvenue dans le jeu !"). Tu peux utiliser Cheat Engine pour rechercher cette chaîne de caractères dans la mémoire du jeu et essayer de la modifier en direct.
- **Changement du message** : Il y a un bouton pour changer le texte du message avec différentes options comme "C'est trop cool !" et "Cheat Engine en action". Ce changement de texte te permet aussi d'entraîner ta recherche sur différentes chaînes de caractères dans le jeu.
- **Listes de messages** : Le programme utilise une liste de chaînes pour changer le message affiché à chaque clic.

### Comment utiliser Cheat Engine avec ce mini-jeu :
1. Lance le jeu en exécutant le script Python.
2. Ouvre Cheat Engine et attache-le au processus Python.
3. Cherche le texte "Bienvenue dans le jeu !" en utilisant une recherche de **"String"**.
4. Modifie la chaîne pour autre chose de la même longueur, par exemple "Salut à toi !".
5. Clique sur le bouton dans le jeu pour voir si la modification reste ou se réinitialise.