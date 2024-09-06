import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

print(f"Chemin Python : {sys.executable}")
print(f"Répertoire de travail actuel : {os.getcwd()}")
print(f"Contenu du répertoire actuel : {os.listdir()}")

def generate_image(prompt, output_path):
    client = OpenAI()
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    image_url = response.data[0].url
    
    # Télécharger et sauvegarder l'image
    import requests
    img_data = requests.get(image_url).content
    with open(output_path, 'wb') as handler:
        handler.write(img_data)

def process_file(file_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    image_count = 1
    
    print(f"Tentative d'ouverture du fichier : {file_path}")
    print(f"Le fichier existe-t-il ? {os.path.exists(file_path)}")
    print(f"Chemin absolu du fichier : {os.path.abspath(file_path)}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if "--ar" in line:
                    prompt = line.strip().replace('"', '')
                    output_path = f"images/{base_name}_{image_count}.png"
                    
                    generate_image(prompt, output_path)
                    print(f"Image générée : {output_path}")
                    
                    image_count += 1
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    input_file = "concepts/voices_of_the_circuits.md"
    
    # Créer le dossier 'aider/images' s'il n'existe pas
    os.makedirs("images", exist_ok=True)
    
    process_file(input_file)
