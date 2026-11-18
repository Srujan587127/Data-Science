import pandas as pd

data = pd.read_csv("mymoviedb.csv", engine = "python", on_bad_lines = "skip")

data["Vote_Average"] = pd.to_numeric(data["Vote_Average"], erros = "coerce")

data["Vote_Count"] = pd.to_numeric(data["Vote_Count"], erros = "coerce")

print("First 5 rows of the dataset:")
print(data.head())

print("\nRows 5 to 9 and Coulmns 1 to 3:")
print(data.iloc[5:10, 1:4])

print("\nMovies with Vote Average greater than 8:")
print(data.loc[data["Vote_Average"] > 8, ["Title", "Vote_Average"]])

