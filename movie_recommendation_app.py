from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("MovieRecommendationApp") \
    .getOrCreate()

# Load Dataset
movies_path = "./Data_Sets/movies.csv"
ratings_path = "./Data_Sets/ratings.csv"

movies = spark.read.csv(movies_path, header=True, inferSchema=True)
ratings = spark.read.csv(ratings_path, header=True, inferSchema=True)

# Preview datasets
movies.show(5)
ratings.show(5)

# Preprocess Data
ratings = ratings.select(ratings["userId"].cast("int"),
                         ratings["movieId"].cast("int"),
                         ratings["rating"].cast("float"))

# Split Dataset
(training, test) = ratings.randomSplit([0.8, 0.2])

#  Build ALS Model
als = ALS(maxIter=10, regParam=0.1, userCol="userId", itemCol="movieId", ratingCol="rating",
          coldStartStrategy="drop")
model = als.fit(training)

# Evaluate Model
predictions = model.transform(test)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print(f"Root-mean-square error = {rmse}")

#  Generate Recommendations
user_recs = model.recommendForAllUsers(10)
movie_recs = model.recommendForAllItems(10)

# Show sample recommendations
user_recs.show(5, truncate=False)
movie_recs.show(5, truncate=False)

# Stop Spark Session
spark.stop()

