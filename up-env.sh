#!/bin/bash

# Construire l'image Docker
echo "Construction de l'image Docker..."
docker build -t youtube-to-mp3 .

# Créer le dossier music-mp3 si inexistant
if [ ! -d "music-mp3" ]; then
    mkdir music-mp3
fi

# Lancer le conteneur Docker
echo "Lancement du conteneur Docker..."
docker run --rm -it -v "$(pwd):/app" youtube-to-mp3

echo "Le projet a été lancé avec succès."
