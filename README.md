# TP1 : Sécurité des systèmes d'informations

Ce programme est un formulaire de connexion avec des fonctionnalités de création de compte, conçu dans le cadre du TP1 sur la sécurité des systèmes d'informations.

## Informations techniques

Ce programme est écrit en Python et utilise les bibliothèques suivantes :
- tkinter : pour l'interface graphique
- PIL (Python Imaging Library) : pour manipuler des images
- csv : pour la manipulation des fichiers CSV
- os : pour les opérations sur le système d'exploitation
- hashlib : pour le hachage sécurisé des mots de passe

## Comment utiliser

1. Assurez-vous d'avoir Python installé sur votre système.
2. Exécutez le programme en exécutant le fichier `TP1.py`.
3. Un formulaire de connexion s'affichera.
4. Si vous avez déjà un compte, entrez votre identifiant et votre mot de passe, puis cliquez sur le bouton "Se connecter".
5. Si vous n'avez pas de compte, cliquez sur le bouton "Ajout compte" pour créer un nouveau compte en remplissant les champs requis.
6. Les mots de passe sont hachés avec l'algorithme SHA-256 pour assurer la sécurité.
7. Vous pouvez réinitialiser les champs en cliquant sur le bouton "Réinitialiser".

## Remarques

- Assurez-vous de respecter les exigences de sécurité lors de la création de votre mot de passe.
- Les informations d'identification sont stockées dans un fichier CSV localement sur votre système.

