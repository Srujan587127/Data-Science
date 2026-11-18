import pandas as pd

data = pd.read_csv("titanic.csv")

adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names)

print(data.iloc[9:25, 2:5])

data.iloc[0:3, 3] = "Amelie loconis"
print(data["Name"])

data.to_csv("changedData.csv")

data["Test"] = data["Fare"] + 2

data["Test2"] = data["Fare"] * data["Pclass"]

data_renamed = data.rename(columns={"Pclass": "Passanger Class", "SibSp":"Sibling"})

print(data_renamed.info())

print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())

print(data.agg({"Age": ["min", "max", "median"], "Fare": ["min", "max", "median"]}))

print(data[["Sex", "Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

print(data["Pclass"].value_counts())

print(data.groupby("Pclass")["Pclass"].count())

data = data.sort_values(by = "Age")

print(data[["Name", "Age"]].head())

data = data.sort_values(by = [ "Pclass", "Age"], ascending = False)

data["NameLowercase"] = data["Name"].str.lower()

print(data["NameLowercase"])

print(data["Name"].str.split(","))

data["Surname"] = data["Name"].str.split(",").str.get(0)

print(data["Surname"])

data["Sex_short"] = data["Sex"].replace({"Male": "M", "female": "F"})

print(data["Sex_short"])