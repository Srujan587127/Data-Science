import pandas as pd

data = pd.read_csv("mymoviedb.csv", engine = "python", on_bad_lines = "skip")

data["Vote_Average"] = pd.to_numeric(data["Vote_Average"], errors = "coerce")
data["Vote_Count"] = pd.to_numeric(data["Vote_Count"], errors = "coerce")

print(data.head())

print(data.info())

print(data.dtypes)

titleAndGenre = data[["Title", "Genre"]]

print(titleAndGenre.head())

print(titleAndGenre.shape)

above7 = data[data["Vote_Average"] > 7]

print(above7[["Title", "Vote_Average"]].head())

print(above7.shape)

englishAndKorean = data[data["Original_Language"].isin(["en", "ko"])]

print(englishAndKorean[["Title", "Orginal_Language"]].head())

print(englishAndKorean.shape)

englishOrKorean = data[
    (data["Original_Language"] == "en") | (data["Original_Language"] == "ko")
]

print(englishOrKorean[["Title", "Original_Language"]].head())

print(englishOrKorean.shape)

englishHighRated= data [
    (data["Original_Language"] == "en") & (data["Vote_Average"] > 7) 
]

print(
    englishHighRated[
        ["Title", "Original_Language", "Vote_Average", "Popularity"]
    ].head()
)

print(
    "Mean Popularity of English High Rated Movies:",
    englishHighRated["Popularity"].mean(),
)

englishMovies = data[(data["Original_Language"] == "en") & (data["Vote_Average"] > 7)]
koreanMovies = data[(data["Original_Language"] == "ko") & (data["Vote_Average"] > 7)]
japaneseMovies = data[(data["Original_Language"] == "ja") & (data["Vote_Average"] > 7)]
frenchMovies = data[(data["Original_Language"] == "fr") & (data["Vote_Average"] > 7)]
hindiMovies = data[(data["Original_Language"] == "hi") & (data["Vote_Average"] > 7)]

print("English Movies:", englishMovies["Popularity"].mean())
print("Korean Movies:", koreanMovies["Popularity"].mean())
print("Japanese Movies:", japaneseMovies["Popularity"].mean())
print("French Movies:", frenchMovies["Popularity"].mean())
print("Hindi Movies:", hindiMovies["Popularity"].mean())