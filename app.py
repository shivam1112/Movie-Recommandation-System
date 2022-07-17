import streamlit as st
import pickle
import pandas as pd
import requests
st.write("movie recommandation system created by Nishkarsh Aggarwal")
st.title("Movie Recommandation System")

# movies= pickle.load(open(movies.pkl,"rb"))
movie_dict = pickle.load(open("movies_dict.pkl", "rb"))
movie_list = pd.DataFrame(movie_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

option = st.selectbox(
    'Select Movie',
    movie_list["title"].values)

st.write('You selected:', option)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    main_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return main_path



def recommend(movie):
    movie_index = movie_list[movie_list["title"] == movie].index[0]
    recommend_movie = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for j in recommend_movie:
        movie_id = movie_list.iloc[j[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movie_list.iloc[j[0]].title)

    return recommended_movies,recommended_movies_poster


if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])