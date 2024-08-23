README
Présentation
Ce projet permet de télécharger toutes les vidéos d'une playlist YouTube spécifiée, de les convertir au format MP3 avec un débit de 320 kilobits par seconde, et de stocker les fichiers MP3 dans un dossier spécifique. Le tout est exécuté dans un conteneur Docker pour garantir l'isolation et la reproductibilité.

Prérequis
Avant de commencer, assurez-vous que les éléments suivants sont installés sur votre système :

Docker : Pour construire et exécuter le conteneur.

1. Préparer l'environnement
Le script up-env.sh automatisera les étapes de configuration. Il vous guidera à travers la construction de l'image Docker, et le lancement du conteneur.

a. Rendre le script exécutable
Avant de lancer le script, assurez-vous qu'il est exécutable :

bash
Copier le code
chmod +x up-env.sh
b. Exécuter le script
Ensuite, lancez le script pour configurer et lancer le projet :

bash
Copier le code
./up-env.sh
Le script effectuera les étapes suivantes :

Demander l'URL de la playlist YouTube : Si le fichier .env n'existe pas, il sera créé avec l'URL fournie.
Construire l'image Docker : Crée une image Docker nommée youtube-to-mp3.
Créer le dossier music-mp3 : Si le dossier n'existe pas, il sera créé pour stocker les fichiers MP3.
Lancer le conteneur Docker : Exécute le conteneur avec les variables d'environnement et le volume appropriés.

Notes
Fichier .env : Ce fichier doit contenir la variable URL_PLAYLIST_YOUTUBE avec l'URL de votre playlist YouTube. Le script up-env.sh créera ce fichier pour vous s'il n'existe pas.
Dépôt Git : Assurez-vous que le dépôt Git que vous clonez contient le fichier script.py et le Dockerfile.
Dépannage
Si vous rencontrez des problèmes lors de l'exécution du script ou du conteneur Docker, vérifiez les messages d'erreur affichés dans le terminal et assurez-vous que toutes les dépendances sont correctement installées et configurées.


// TODO faire de l'éxecutable dans windows avec python