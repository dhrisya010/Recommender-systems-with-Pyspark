# Movie Recommendation System


## The Mission

The project is based on  Internet Movie Database (IMDB). The  task is to create a recommendation tool for movies and TV shows that an user can interact with. 

The tool will take as input the user's favorite movies and shows and recommend new ones in a user friendly manner. You are allowed to use additional resources and incorporate other features that are interesting for users.

The goal is to have a working minimum viable product (MVP) by the end of the project. 

### The Data

The data set is from:

* [MovieLens](https://grouplens.org/datasets/movielens/). 

### The Model 

There are three especially common methods to design a recommender system: Collaborative Filtering, Content-based Filtering and hybrid techniques. Content-based systems aim to make recommendations based on some previous information about the customer and the products. For instance, if Netflix knows you like drama movies, it might recommend you movies of this type. 

However, in a collaborative filtering approach, it might simply ignore the type of the film. The features used in this case are exclusively users rating patterns. For instance, if you watched five different series on Netflix and have rated five each of them, just like some other random user, then you might be interested to know what else he has rated as five stars. Hybrid systems make use of both techniques.

In this project, we will use of Alternating Least Square (ALS) Matrix Factorization, a Collaborative Filtering algorithm that is already implemented in the ML Pyspark library. 

### The Mission objective:

* Create a simple movie recommendation app using Pyspark in the backend. 
* Deploy app locally (streamlit recommended!). 

### Resources on PySpark:

* [Movie Recommendation System Using Spark MLlib](https://medium.com/edureka/spark-mllib-e87546ac268) (See this article for a sample pipeline)
* [Pyspark Tutorial: Getting Started with Pyspark](https://www.datacamp.com/tutorial/pyspark-tutorial-getting-started-with-pyspark)
* [Building Recommendation Engines with PySpark (Chapter 3)](https://www.datacamp.com/courses/recommendation-engines-in-pyspark)

## 📦 Repo structure
```.
├── RECOMMENDER-SYSTEMS-WITH-PYSPARK
│ └── Data_Sets
├   │  ──recommendations
├   │  ── movies.csv
├   │  ── ratings.csv
├ ── movie_recommendation.ipynb
├ ── movie_recommendation_app.py
├    │ ── webapp.py    
├  ── .gitignore
├  ── requirements.txt
├  ── README.md
 
```

### Streamlit application

Create a small web application using Streamlit that will allow non-technical people to use your API.

First we want to install Streamlit

```bash
# Install Streamlit
pip install streamlit

# Run the streamlit command
streamlit run webapp.py

```

## ⏱️ Project Timeline
The initial setup of this project was completed in 5 days.

The project was completed as part of my 7-month AI training bootcamp at BeCode in Ghent, Belgium.




