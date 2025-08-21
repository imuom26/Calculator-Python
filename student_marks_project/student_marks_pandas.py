import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Math": [85, 72, 90, 60, 95],
    "Science": [88, 75, 92, 70, 98],
    "English": [78, 65, 85, 55, 90]
}
df = pd.DataFrame(data)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
high_achievers = df[df["Average"] > 80]
print("Student Scores with Averages: \n", df, "\n")
print("High Achievers (Average > 80): \n", high_achievers, "\n")
