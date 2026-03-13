import pandas as pd

csv_path = "data.csv"

data = pd.read_csv(csv_path)

new_row = {
    "id": 4,
    "name": "Diana",
    "age": 31,
    "city": "Boston",
}

updated_data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
updated_data.to_csv(csv_path, index=False)

print("Added a new row to data.csv and saved the updated file.")
