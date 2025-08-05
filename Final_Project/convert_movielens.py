import pandas as pd

# ratings.dat
ratings = pd.read_csv("ratings.dat", sep="::", engine="python", names=["UserID", "MovieID", "Rating", "Timestamp"])
ratings.to_csv("ratings.csv", index=False)

# users.dat
users = pd.read_csv("users.dat", sep="::", engine="python", names=["UserID", "Gender", "Age", "Occupation", "Zip-code"])
users.to_csv("users.csv", index=False)

# movies.dat
movies = pd.read_csv("movies.dat", sep="::", engine="python", names=["MovieID", "Title", "Genres"])
movies.to_csv("movies.csv", index=False)

print("The CSV is converted.")

