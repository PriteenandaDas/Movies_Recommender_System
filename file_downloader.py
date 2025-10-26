import os
import gdown

def download_similarity_file():
    url = "https://drive.google.com/uc?id=1mWnd_QMj4OJuI0d1RAhNbtSObpGJ5FJw"
    output = "similarity.pkl"
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)