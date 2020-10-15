import pandas as pd
import os

all_data = pd.DataFrame()

for file in os.listdir("./"):
    if file.endswith(".csv"):
        print(os.path.join("./", file))
        df = pd.read_csv("./" + file)
        all_data = pd.concat([all_data, df])

all_data.to_csv("all_data.csv", index=False)

df = pd.read_csv("all_data.csv")

new_df = df.loc[(df.iloc[:, 3] > 69.5) &
                (df.iloc[:, 3] < 78)]

new_df.to_csv("all_data_filtered.csv", index=False)
