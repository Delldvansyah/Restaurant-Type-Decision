import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

class Data:
    def _init_(self, tahun, berat, nilai, bongkar, muat, labelling):
        self.tahun = tahun
        self.berat = berat
        self.nilai = nilai
        self.bongkar = bongkar
        self.muat = muat
        self.labelling = labelling

# Load data from Excel file
def load_data(file_path):
    # Skip the first row which is not relevant, and use the second row as header
    df = pd.read_excel(file_path, skiprows=1)
    print("Columns in the dataframe:", df.columns)
    
    # Manually rename columns to match the expected names
    df.columns = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat', 'Labelling']
    
    dataset = []
    for _, row in df.iterrows():
        dataset.append(Data(row['Tahun'], row['Berat'], row['Nilai'], row['Bongkar'], row['Muat'], row['Labelling']))
    return dataset

# The rest of the functions remain the same...

def preprocess_data(dataset):
    cleaned_dataset = [data for data in dataset if not any(pd.isnull([data.tahun, data.berat, data.nilai, data.bongkar, data.muat, data.labelling]))]
    return cleaned_dataset

def count_missing_labels(dataset):
    return sum(1 for data in dataset if data.labelling == -1)

def dataset_to_dataframe(dataset):
    data_dict = {
        'Tahun': [data.tahun for data in dataset],
        'Berat': [data.berat for data in dataset],
        'Nilai': [data.nilai for data in dataset],
        'Bongkar': [data.bongkar for data in dataset],
        'Muat': [data.muat for data in dataset],
        'Labelling': [data.labelling for data in dataset]
    }
    return pd.DataFrame(data_dict)

def build_tree(train_data):
    features = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat']
    X_train = train_data[features]
    y_train = train_data['Labelling']
    tree = DecisionTreeClassifier(max_depth=5)
    tree.fit(X_train, y_train)
    return tree

def predict_tree(instance, tree):
    return tree.predict([instance])[0]

def evaluate_tree(test_data, tree):
    features = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat']
    X_test = test_data[features]
    y_test = test_data['Labelling']
    y_pred = tree.predict(X_test)
    return accuracy_score(y_test, y_pred)

def print_confusion_matrix(test_data, tree):
    features = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat']
    X_test = test_data[features]
    y_test = test_data['Labelling']
    y_pred = tree.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

def print_discrepancies(test_data, tree):
    features = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat']
    X_test = test_data[features]
    y_test = test_data['Labelling']
    y_pred = tree.predict(X_test)
    discrepancies = test_data[y_test != y_pred]['Tahun'].tolist()
    print("Discrepancies:")
    print(discrepancies)

def write_results_to_excel(file_path, test_data, tree):
    features = ['Tahun', 'Berat', 'Nilai', 'Bongkar', 'Muat']
    X_test = test_data[features]
    test_data['Prediksi'] = tree.predict(X_test)
    
    # Ensure the 'test_data' is a DataFrame
    test_data = pd.DataFrame(test_data)
    
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        test_data.to_excel(writer, sheet_name='Sheet1', index=False)

def main():
    file_path = "Labeling.xlsx"  # Adjust the path to your file
    dataset = load_data(file_path)
    cleaned_dataset = preprocess_data(dataset)
    print(f"Total rows after preprocessing: {len(cleaned_dataset)}")
    missing_labels = count_missing_labels(cleaned_dataset)
    print(f"Total rows with missing labels: {missing_labels}")

    df = dataset_to_dataframe(cleaned_dataset)
    train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)
    print(f"Training set size: {len(train_data)}, Test set size: {len(test_data)}")

    tree = build_tree(train_data)
    print("Decision tree built successfully.")

    accuracy = evaluate_tree(test_data, tree)
    print(f"Accuracy: {accuracy}")

    print_confusion_matrix(test_data, tree)
    print_discrepancies(test_data, tree)

    output_file_path = "output_prediksi_data.xlsx"
    write_results_to_excel(output_file_path, test_data, tree)
    print(f"Results have been written to {output_file_path}")

if __name__ == "__main__":
    main()