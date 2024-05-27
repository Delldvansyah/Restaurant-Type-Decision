Decision Tree Classifier for Restaurant Types
Overview
This program is an implementation of the Decision Tree algorithm used to classify types of restaurants based on several attributes: rating, number of ratings, average cost, online ordering availability, and table booking availability.

Detailed Workflow
Reading Data from Excel:
The program reads restaurant data from an Excel file using pandas and converts it into a list of dictionaries (data rows).

Data Preprocessing:
Convert the values of the online_order and table_booking attributes from text format ("Yes"/"No") to binary (1/0).

Calculating Gini Impurity:
Gini impurity is used to measure the heterogeneity of a node. Low impurity values mean the node is more homogeneous. The gini_impurity function calculates the impurity of a set of data rows.

Splitting the Dataset:
The split_dataset function divides the dataset into two subsets based on a certain attribute value. The first subset contains rows with attribute values >= a certain value, and the second subset contains rows with attribute values < that value.

Finding the Best Split:
The find_best_split function searches for the best attribute and value that provide the highest gain in dataset division. Gain is the reduction in impurity from dividing the dataset.

Building the Decision Tree:
The build_tree function recursively constructs the decision tree by selecting the best division at each step. Decision nodes are created for each division, and leaf nodes are created when no further gain can be obtained.

Classification:
The classify function classifies a new data row based on the constructed decision tree. If a node is a leaf, it returns a prediction based on the majority type of restaurants in that leaf.

User Input:
The get_user_input function prompts the user to input attributes of a new restaurant to be predicted.

Prediction:
The predict function classifies the user input using the constructed decision tree and returns the predicted restaurant type.

Reasons for Using This Approach
Decision Tree: This algorithm is easy to understand and interpret. It works well on data with many categorical and numerical features. Additionally, it does not require extensive data preprocessing.
Gini Impurity: Used as the metric for best selection because it is easy to compute and commonly used in decision trees.
Recursive: The recursive approach facilitates the formation of a decision tree that can continuously divide the dataset until optimal results are achieved.
Requirements
Python:
Python 3.x Installation
Pandas:
Used to read and process data from Excel files.
Installation: pip install pandas
OpenPyXL:
Used by pandas to read Excel files.
Installation: pip install openpyxl
Python Program (Code):
This program requires access to an Excel file containing restaurant data. You need to ensure the Excel file is in the correct location and has appropriate column formatting.
