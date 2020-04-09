import pandas

filepath = "abitibi_climat.csv"

csv = pandas.read_csv(filepath)

print(csv.head())
