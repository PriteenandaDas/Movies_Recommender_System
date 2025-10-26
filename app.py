import streamlit as st
import pickle
import pandas as pd
import json
from omdb_utils import get_movie_details
from file_downloader import download_similarity_file
#import joblib


config = json.load(open("config.json"))
OMDB_API_KEY = config["OMDB_API_KEY"]

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distance=similarity[movies_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:11]
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

movies=pd.DataFrame(movies_dict)

download_similarity_file()
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="centered"
)
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox("🎬 Select a movie:",movies['title'].values)

# if st.button('Recommend'):
#     recommendations = recommend(selected_movie)
#     for i in recommendations:
#         st.write(i)

if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend(selected_movie)

        if recommendations is None or not recommendations:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for movie_title in recommendations:
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)

                col1, col2 = st.columns([1, 3])
                with col1:
                    if poster != "N/A":
                        st.image(poster, width=100)
                    else:
                        st.write("❌ No Poster Found")
                with col2:
                    st.markdown(f"### {movie_title}")
                    st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")