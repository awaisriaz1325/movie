import streamlit as st
import pickle
import pandas as pd
import requests

similarity= pd.read_pickle('similarity.pkl')
movielist= pd.read_pickle('movies.pkl')

def fetch_poster(movie_id ):
  response= requests.get("https://api.themoviedb.org/3/movie/{}?api_key=aeaf42a57abdb02458ce13ff02ada312&language=en-US".format(movie_id))
  data= response.json()
  return "https://image.tmdb.org/t/p/w500"+data["poster_path"]

def recommend(movie):
  index= movielist[movielist['original_title']==movie].index[0]
  unsorted= list(enumerate(similarity[index]))
  sorted1= sorted(unsorted, key= lambda x: x[1], reverse=True)
  recommended=[]
  recommended_poster=[]
  for i in sorted1[1:6]:
    index1= i[0]
    #fetch poster from api
    recommended_poster.append(fetch_poster(movielist.iloc[i[0]].movie_id)) 
    
    recommended.append((movielist.iloc[i[0]].original_title))

  return recommended, recommended_poster

movie=movielist["original_title"].values

st.title("Movie Recommendation System")
selected= st.selectbox("Select a movie", movie)

if st.button("Predict"):
  final, final_poster= recommend(selected)
  col1, col2, col3,col4,col5 = st.columns(5)

  with col1:
      st.text(final[0])
      st.image(final_poster[0])

  with col2:
      st.text(final[1])
      st.image(final_poster[1])

  with col3:
      st.text(final[2])
      st.image(final_poster[2])

  with col4:
      st.text(final[3])
      st.image(final_poster[3])

  with col5:
      st.text(final[4])
      st.image(final_poster[4])
    
