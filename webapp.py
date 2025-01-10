import streamlit as st
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALSModel
from distutils.version import LooseVersion
import pandas as pd

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("MovieRecommendationApp") \
    .getOrCreate()

movies = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("./Data_Sets/movies.csv")
moviesDF = movies.toPandas()
recommendations = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("./Data_Sets/recommendations/part-00007-02223bfc-4883-4bdc-83e8-3bd09830d981-c000.csv")
recommendationsDF = recommendations.toPandas()

# Streamlit UI
st.title("🎬Movie Recommendation System")
st.subheader("Get personalized movie recommendations!")

# Input: User ID
user_id = st.number_input("👤Enter User ID:", min_value=1, step=1)

st.markdown("""
<style>.element-container:has(#button-after) + div button {
 background-color: green;
 p{
 color : white;
  }
 }</style>""", unsafe_allow_html=True)
st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)

if st.button('Recommend Movies'):
    recommendation = recommendationsDF.query(f'userId=={user_id}')
    movies = pd.merge(recommendation, moviesDF, on='movieId', how='inner')
    st.success(f"### Movie Recommendation for the users are")
    st.dataframe(movies)


