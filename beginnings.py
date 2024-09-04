import pandas as pd

# Create a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Oscar'],
    'Age': [25, 30, 35, 40, 51],
    'City': ['New York', 'Los Angeles', 'Houston', 'Houston', 'Madrid']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
# print(df)

# print(df.sort_values(by='Age'))
# print(df.describe())
print(df.groupby('City')['Age'].mean())

grouped_data = df.groupby(['City']).size()

print(grouped_data)

# Group by 'City' and calculate multiple statistics for the 'Age' column
grouped_stats = df.groupby('City')['Age'].agg(['mean', 'min', 'max', 'count'])

print(grouped_stats)

# Iterate over each group
# for city, group in df.groupby('City'):
#     print(f"City: {city}")
#     print(group)

pi = -33333.14159
print(f"Pi rounded to 2 decimal places is {pi:+,.2f}")
