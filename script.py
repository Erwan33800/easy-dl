import yt_dlp
import os

# Demander l'URL de la playlist YouTube à l'utilisateur
playlist_url = input("Veuillez entrer l'URL de la playlist YouTube : ").strip()

# Demander à l'utilisateur s'il souhaite utiliser un autre dossier que "music-mp3"
custom_directory = input("Souhaitez-vous créer un nouveau dossier pour enregistrer les fichiers MP3 ? (par défaut : 'music-mp3') [Oui/Non] : ").strip().lower()

# Déterminer le nom du dossier à utiliser
if custom_directory == 'oui':
    output_directory = input("Entrez le nom du nouveau dossier : ").strip()
    if not output_directory:
        output_directory = 'music-mp3'
else:
    output_directory = 'music-mp3'

# Créer le dossier spécifié s'il n'existe pas
os.makedirs(output_directory, exist_ok=True)

# Fonction pour vérifier si un fichier MP3 existe déjà
def file_exists(title):
    return os.path.isfile(os.path.join(output_directory, f"{title}"))

# Options de téléchargement
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
}

# Télécharger et convertir la playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    playlist_info = ydl.extract_info(playlist_url, download=False)
    
    for video in playlist_info['entries']:
        video_title = video['title']
        
        # Vérification avant téléchargement
        if file_exists(video_title):
            print(f"Le fichier '{video_title}' existe déjà, téléchargement ignoré.")
        else:
            # Téléchargement de la vidéo si elle n'existe pas
            ydl.download([video['webpage_url']])
            print(f"'{video_title}' téléchargé et converti avec succès.")

print("Téléchargement et conversion terminés pour toutes les vidéos non existantes.")
