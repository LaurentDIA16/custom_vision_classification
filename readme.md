Sur MacOS
Installation
Installer un environnement virtuel : "python3 -m venv .env"
Lancer l'environnement virtuel : "source .env/bin/activate"
Installer packages:
    - pip install --upgrade pip
    - pip install django
    - pip install psycopg2-binary (pour lien avec PostgreSql)
    - pip install azure-cognitiveservices-vision-customvision (IA)
Enregistrer les packages:
    - pip freeze > requirements.txt
Installer les différents packages (Django, ...) : "pip install -r requirements.txt"


Créer la base de donnée sur postgres avec les infos disponible dans le fichier settings.py
Créer un nouveau login dans postgres avec nom moni et mdp moni, mettre tout les privilèges
Effectuer les premières migrations, dans le terminal taper : "cd src" puis "python manage.py makemigrations" et "python manage.py migrate"