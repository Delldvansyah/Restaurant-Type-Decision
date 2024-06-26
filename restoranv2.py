import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import numpy as np

# Fungsi Read data excel
def read_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    data = df.to_dict(orient='records')
    return data

# Baca data excel
file_path = 'zomato3.xlsx'
data = read_data_from_excel(file_path)

# Convert jika Yes = 1, No = 0
for row in data:
    row["online_order"] = 1 if row["online_order"] == "Yes" else 0
    row["table booking"] = 1 if row["table booking"] == "Yes" else 0

# Calculate Gini Impurity
def gini_impurity(rows):
    counts = Counter(row["restaurant type"] for row in rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl ** 2
    return impurity

# Fungsi buat split dataset
def split_dataset(rows, attribute, value):
    left = [row for row in rows if row[attribute] >= value]
    right = [row for row in rows if row[attribute] < value]
    return left, right

# Cari split yang terbaik
def find_best_split(rows):
    best_gain = 0
    best_attribute = None
    best_value = None
    current_impurity = gini_impurity(rows)
    n_features = len(rows[0]) - 1 

    for col in rows[0]:
        if col == "restaurant type":
            continue
        values = set(row[col] for row in rows)

        for val in values:
            left, right = split_dataset(rows, col, val)
            if not left or not right:
                continue

            p = float(len(left)) / len(rows)
            gain = current_impurity - p * gini_impurity(left) - (1 - p) * gini_impurity(right)

            if gain > best_gain:
                best_gain, best_attribute, best_value = gain, col, val

    return best_gain, best_attribute, best_value

class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

class Leaf:
    def __init__(self, rows):
        self.predictions = Counter(row["restaurant type"] for row in rows)

def build_tree(rows):
    gain, attribute, value = find_best_split(rows)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = split_dataset(rows, attribute, value)

    true_branch = build_tree(true_rows)
    false_branch = build_tree(false_rows)

    return DecisionNode((attribute, value), true_branch, false_branch)

def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions

    if row[node.question[0]] >= node.question[1]:
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

# Shuffle dataset
np.random.shuffle(data)

# Split the data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Build the tree using the training set
my_tree = build_tree(train_data)

# Fungsi Prediksi
def predict(query):
    query = query.copy()
    query["online_order"] = 1 if query["online_order"] == "Yes" else 0
    query["table booking"] = 1 if query["table booking"] == "Yes" else 0
    prediction = classify(query, my_tree)
    return prediction.most_common(1)[0][0]

# Akurasinya
correct_predictions = 0
for row in test_data:
    if row["restaurant type"] == predict(row):
        correct_predictions += 1

accuracy = correct_predictions / len(test_data) * 100

# User inputnya
def get_user_input():
    rate = float(input("Enter the rate : "))
    num_ratings = int(input("Enter the number of ratings : "))
    avg_cost = int(input("Enter the average cost for two people : "))
    online_order = input("Is online order available? (Yes/No) : ")
    table_booking = input("Is table booking available? (Yes/No) : ")

    query = {
        "rate (out of 5)": rate,
        "num of ratings": num_ratings,
        "avg cost (two people)": avg_cost,
        "online_order": online_order,
        "table booking": table_booking
    }
    return query

# Ambil user input
query = get_user_input()

# Buat Prediksi
predicted_type = predict(query)
print("Predicted restaurant type:", predicted_type)
print(f"Model Accuracy: {accuracy:.2f}%")
