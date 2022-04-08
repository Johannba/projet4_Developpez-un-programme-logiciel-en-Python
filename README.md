# P4_johann_bacha

Développez un programme logiciel en Python

Projet consistant à créer une application permettant de créer la structure d'un tournoi d'échecs, permettant d'ajouter des joueurs dans une base de données. Le programme utilise un algorithme permettant de calculer la rotation des joueurs afin que les matchs soit équitables et ne se reproduisent pas (algorithme suisse de tournois).


Le programme utilise le design pattern MVC (Modèles - Vues - Controlleurs), et utilise la librairie TinyDB pour sauvegarder les joueurs et les tournois.

Il permet de :

- Créer et sauvegarder des joueurs.
- Mettre à jour le classement d'un joueur.
- Créer et sauvegarder des tournois.
- Lancer des tournois.
- Arrêter un tournoi en cours et le reprendre plus tard.


L'ensemble des données sont enregisté dans un fichier json.
Nous pouvons sauvegarder et charger l'état du programme à tout moment entre deux actions de l'utilisateur.
Nous pouvons aussi afficher des rapports dans le programme.

la structure du programme suit le modèle de conception modèle-vue-controlleur.En d'autres termes, le programme est divisé en trois paquets : modèles, vues et contrôleurs.

Pour effectuer le peluchage du code, on utilisent flake8 avec l'option de longueur de ligne maximale fixée à 119. Nous avons également un rapport généré par flake8-html.

Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme.

Pré-requis:

Python 3 installé (https://www.python.org/downloads/)
Savoir naviguer dans les dossiers et fichiers à partir d'un terminal.

Mode d'emploi:

Lancer le programme depuis le terminal:

Depuis votre terminal, placez vous à l'endroit souhaité:
cd [chemin d'accès]

Creer un nouveau dossier:
mkdir [nom de votre dossier]

Copier le programme source:
git clone https://github.com/Johannba/projet4_johann.git

Vous devez voir (depuis votre explorateur) les fichiers suivants: 
README.md*flake-report*models*controllers*main.py*views

Creer un environnement virtuel:

Depuis windows/mac/linux: python3 -m venv env

Activer l'environnement:

Depuis windows: env\Scripts\activate.bat

Depuis mac/linux: source env/bin/activate

Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:

https://docs.python.org/fr/3/library/venv.html?highlight=venv

Lancement du programme:

pyhton main.py

Ensuite suivez les instructions du menu



Générer un nouveau fichier flake8-html:

Lancer le programme depuis le terminal:

Depuis votre terminal, placez vous à l'endroit souhaité:
cd [chemin d'accès]

Installer flake8-html :

pip installer flake8-html

Ensuite, exécutez flake8 en passant l' option --format=html et un --htmldir :

flake8 --format = html --htmldir = flake-rapport


Fabriqué avec:

[Visual Studio Code] (https://code.visualstudio.com/download) - Editeur de textes

Auteurs:

Johann Bacha

Remerciements:

Merci à Ranga Gonnage pour ses conseils, ça pédagogie et sa diplomatie.