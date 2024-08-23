# Utiliser une image Python officielle comme base
FROM python:3.10-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y ffmpeg

# Copier le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Créer un répertoire de travail
WORKDIR /app

# Copier le script Python dans le conteneur
COPY . .

# Commande pour exécuter le script
CMD ["python", "script.py"]
