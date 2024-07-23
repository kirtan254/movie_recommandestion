import streamlit as st
import pickle
import difflib
import pandas as pd
import requests
    



def f_poster(movie_id):
    respones=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c51df04cb9731df64c88e1b21df18962&language=en-US'.format(movie_id))
    data=respones.json()
  
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(selected_movie_name):
    list_of_all_title=movies['original_title'].tolist()
    find_close_match=difflib.get_close_matches(selected_movie_name,list_of_all_title)
    close_match=find_close_match[0]
    index_of_movie=movies[movies.original_title==close_match]['level_0'].values[0]
    similarity_score=list(enumerate(similarity[index_of_movie]))
    sorted_similer_movies=sorted(similarity_score,reverse = True,key=lambda x:x[1])[1:12]
    recommanded_movies=[]
    recommanded_poster=[]
    for i in sorted_similer_movies:
        movie_id=int(movies.iloc[i[0]]['id'])
        recommanded_movies.append(movies.iloc[i[0]].original_title)
        recommanded_poster.append(f_poster(movie_id))
    return recommanded_movies,recommanded_poster   


movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommandetion System")

selected_movie_name=st.selectbox(
    'Enter Your Favourite Movie Name!!',
    movies['title'].values
)
if st.button('recommend'):
    names,poster=recommend(selected_movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    
   
    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])

    with col1:
        st.text(names[5])
        st.image(poster[5])

    with col2:
        st.text(names[6])
        st.image(poster[6])

    with col3:
        st.text(names[7])
        st.image(poster[7])

    with col4:
        st.text(names[8])
        st.image(poster[8])

    with col5:
        st.text(names[9])
        st.image(poster[9])


       
       

       
    