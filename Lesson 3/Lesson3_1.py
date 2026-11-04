import pandas as pd

weather_data = {
    "City": ["New York", "London", "Los Angles", "Manchester",
    "Chicago"],
    "Temperature": [32, 18, 30, 15, 27],
    "Humidity": [65, 80, 55, 85, 70],
    "Rainfall": [120, 180, 50, 200, 100],
}

df = pd.DataFrame(weather_data)

print("City Weather Dataset")
print(df)

max_temp = df["Temperature"].max()

hottest_city = df[df["Temperature"] == max_temp]

print("\nHottest City:")
print(hottest_city[["City", "Temperature"]])

avg_rainfall = df["Rainfall"].mean()

print("\nAverage Rainfall:", avg_rainfall)

hot_cities= df[df["Temperature"] > 30]

print("\nCities with Temperature Greater Than 30 degrees celsius")
print(hot_cities)
