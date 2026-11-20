import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/chennai_data.csv")

# Display dataset
print(df)

# Filter Chennai records
chennai = df[df["City"] == "Chennai"]

print("\nChennai Records:")
print(chennai)

# Calculate average temperature
print("\nAverage Temperature:")
print(chennai["Temperature"].mean())

# Create graph
df.groupby("City")["Temperature"].mean().plot(kind="bar")

plt.title("Average Temperature by City")
plt.ylabel("Temperature")
plt.show()
