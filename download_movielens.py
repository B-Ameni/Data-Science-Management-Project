"""
Télécharger et préparer MovieLens 100K
"""
import os
import urllib.request
import zipfile
import pandas as pd

# Répertoire de destination
data_dir = "movielensData"
os.makedirs(data_dir, exist_ok=True)

# URL du dataset
url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
zip_file = os.path.join(data_dir, "ml-100k.zip")

print("📥 Téléchargement de MovieLens 100K...")
print(f"   URL: {url}")

try:
    urllib.request.urlretrieve(url, zip_file)
    print(f"✅ Téléchargement réussi : {zip_file}")
    
    # Extraire
    print("📦 Extraction...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    print(f"✅ Extraction réussie dans {data_dir}/")
    
    # Vérifier les fichiers
    extracted_path = os.path.join(data_dir, "ml-100k")
    files = os.listdir(extracted_path)
    print(f"\n📂 Fichiers disponibles dans {extracted_path}:")
    for f in sorted(files)[:10]:
        print(f"   • {f}")
    
    # Charger et afficher des infos
    print("\n📊 Chargement des données...")
    ratings = pd.read_csv(
        os.path.join(extracted_path, "u.data"),
        sep='\t',
        names=['user_id', 'item_id', 'rating', 'timestamp'],
        encoding='latin-1'
    )
    
    movies = pd.read_csv(
        os.path.join(extracted_path, "u.item"),
        sep='|',
        names=['item_id', 'title', 'release_date', 'video_release_date', 'imdb_url'] + 
              ['unknown', 'action', 'adventure', 'animation', 'childrens', 'comedy', 
               'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 
               'musical', 'mystery', 'romance', 'sci_fi', 'thriller', 'war', 'western'],
        encoding='latin-1'
    )
    
    print(f"\n STATISTIQUES MOVIELENS 100K:")
    print(f"   • Utilisateurs: {ratings['user_id'].nunique()}")
    print(f"   • Films: {ratings['item_id'].nunique()}")
    print(f"   • Notes: {len(ratings)}")
    print(f"   • Densité: {100 * len(ratings) / (ratings['user_id'].nunique() * ratings['item_id'].nunique()):.2f}%")
    
    print(f"\n📽️  Premiers films:")
    print(movies[['item_id', 'title']].head(10).to_string(index=False))
    
except Exception as e:
    print(f" Erreur: {e}")
    print("\n Alternative manuelle:")
    print("   1. Allez sur: https://grouplens.org/datasets/movielens/100k/")
    print("   2. Téléchargez ml-100k.zip")
    print("   3. Extraire dans le dossier 'movielensData/'")
