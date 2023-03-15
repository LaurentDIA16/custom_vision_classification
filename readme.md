# Application de classification d'images pour un end-user

## Contexte du projet

L’entreprise Classifr souhaite vous engager en tant que freelance pour une mission d’amélioration d’une application de classification d’images.

Leur algorithme fonctionne correctement, mais ils aimeraient ajouter deux catégories d'images qui ne sont pas prises en charge actuellement.
De plus, ils aimeraient que l’application à destination des utilisateur·rice·s permettant d’interagir avec cette IA de classification soit monitorée.

Présentez un de vos fameux lab prouvant votre savoir faire en IA : N’ayant pas encore accès à leur algorithme, vous vous baserez sur un algorithme connu et un modèle pré entrainé du marché.

Votre tâche est alors la suivante :

ajouter 2 nouvelles catégories au classificateur : 2 catégories suggérées : gâteau et pizza
introduire un système de monitoring de l’application afin de détecter les bugs et être proactif sur la maintenance du modèle
clarifier la démarche complète que vous souhaitez mettre en oeuvre dans une application démo destinée à un·e utilisateur·rice
présenter la conception de cette application démo : elle doit assurer la classification d’images et son monitoring
réaliser les prémices de cette application de démo

## Livrables

    - Upload attendu sur SOL :
        - Votre démarche projet commentée (PDF)
        - Dossier de conception technique de l’application démo à réaliser (PDF)

    - Review :
        - Votre démarche projet : labos, choix effectués, principes retenus pour le monitoring
        - La conception technique envisagée : architecture, maquettes et/ou graphe de dialogue, process ML embarqué, …
        - Démos dès que possible : labos, nouveaux datasets, prémices de l’application …etc..


## Sur VS Code

  - Windows :
    `py -m venv .env`

  - Linux ou Mac OS :

    `python3 -m venv .env` ou `python -m venv .env`

- Lancer l'environnement virtuel :

  - Windows :

    `.env\Scripts\activate`

  - Linux ou Mac OS :

    `source .env/bin/activate`

- Installer les différents packages (Django, ...) :

  `pip install -r requirements.txt`
  
  `pip install azure-cognitiveservices-vision-customvision` (Azure custom vision)
  
- Enregistrer les packages:

  `pip freeze > requirements.txt`
