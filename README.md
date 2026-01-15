🎯 Jeu du Pendu — Python & API Externe
Description
Un jeu du Pendu développé en Python qui utilise une API externe pour récupérer dynamiquement des mots réels et valides. Contrairement aux versions classiques, ce projet ne nécessite aucune liste locale ni fichier dictionnaire.

🧠 Concept innovant
❌ Sans liste de mots locale — Plus de fichiers .txt statiques

❌ Sans dictionnaire intégré — Tout est récupéré en temps réel

✅ Mots réels via API — Des mots authentiques et variés

✅ Parties uniques — Chaque exécution est différente

✨ Fonctionnalités principales
🔤 Génération de mots réels en français

🌐 Intégration avec API externe

❤️ Système de vies avec affichage progressif

⌨️ Interface en ligne de commande intuitive

♻️ Boucle de jeu dynamique et fluide

🧩 Code clair, commenté et pédagogique

🛠️ Technologies utilisées
Python 3 — Langage principal

requests — Pour les appels HTTP

Random Word API — Source des mots aléatoires

📦 Installation
Prérequis
Python 3.x installé

Connexion Internet active

Pip pour installer les dépendances

Étapes d'installation
bash
# 1. Cloner le projet
git clone https://github.com/TON_USERNAME/hangman-python-api.git
cd hangman-python-api

# 2. Installer la dépendance
pip install requests
▶️ Lancement du jeu
bash
python main.py
🌍 API utilisée
Nom : Random Word API

Fonction : Fournit des mots aléatoires réels

Langue : Français supporté

Accès : Libre, sans clé API requise

Important : Connexion Internet obligatoire

Cette API est utilisée pour illustrer l'intégration de services externes dans une application Python.

🎮 Comment jouer
Le programme récupère un mot aléatoire

Devinez les lettres une par une

Vous avez 5 vies au total

Gagnez en trouvant toutes les lettres

Perdez si vos vies atteignent 0

🧪 Exemple de partie
text
Mot : _ _ _ _ _
Vies restantes : 5
Lettre proposée : a
====================
Mot : _ a _ _ _
Vies restantes : 5
📁 Structure du projet
text
hangman-python-api/
├── main.py          # Code principal du jeu
└── README.md        # Documentation
🎓 Objectifs pédagogiques
Ce projet permet de développer les compétences suivantes :

Boucles — Maîtrise des structures while

Conditions — Gestion logique avec if/else

Chaînes de caractères — Manipulation avancée

Listes — Utilisation et modification

API externes — Appels HTTP avec requests

Logique de jeu — Architecture d'une application interactive

⚠️ Notes importantes
Une connexion Internet est nécessaire au fonctionnement

En cas d'indisponibilité de l'API, le jeu ne pourra pas démarrer

Le jeu est sensible à la casse (minuscules uniquement)

🔧 Personnalisation
Vous pouvez modifier :

Le nombre de vies initiales

Le style d'affichage du pendu

Les messages de l'interface

L'API utilisée pour les mots
