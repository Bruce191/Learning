import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "Score": [85, 90, 95, 80, 70]
}

df = pd.DataFrame(data)
print(df)
print("--------")

#ex 1
head = df.head(3)
tail = df.tail(2)
sample = df.sample()

#ex 2
first_row = df.iloc[0:1]
age_of_third_person = df.iloc[2,1]
david = df.loc[3]
name_score_3 = df.loc[0:2, ["Name", "Score"]]

#ex 3
sorted_age = df.sort_values(["Age"], ascending=True)
sorted_score = df.sort_values(["Score"], ascending=False)
only_over_80 = df.loc[df["Score"] > 80]
e 