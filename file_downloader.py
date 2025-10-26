import os
import requests

def download_similarity_file():
    url = "https://drive.google.com/uc?export=download&id=1mWnd_QMj4OJuI0d1RAhNbtSObpGJ5FJw"
    local_path = "similarity.pkl"
    if not os.path.exists(local_path):
        print("Downloading similarity.pkl...")
        response = requests.get(url)
        with open(local_path, "wb") as f:
            f.write(response.content)
        print("Download complete.")