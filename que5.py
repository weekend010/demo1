import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the dataset
dataset_path = r"C:\Users\pujac\OneDrive\Desktop\dsml\Lipstick.csv"  # Replace with your dataset file path
data = pd.read_csv(dataset_path)

# Show the first few rows of the dataset to understand its structure
print(data.head())

# Handle Age (convert age categories into numerical values)
def convert_age(age):
    if age == '<21':
        return 20
    elif age == '21-35':
        return 28  # Midpoint of 21-35
    elif age == '>35':
        return 40  # Arbitrary value for '>35'
    return age

data['Age'] = data['Age'].apply(convert_age)

# Initialize label encoders for each column
label_encoder_gender = LabelEncoder()
label_encoder_ms = LabelEncoder()
label_encoder_income = LabelEncoder()
label_encoder_buys = LabelEncoder()

# Encode categorical columns into numerical values
data['Gender'] = label_encoder_gender.fit_transform(data['Gender'])
data['Ms'] = label_encoder_ms.fit_transform(data['Ms'])
data['Income'] = label_encoder_income.fit_transform(data['Income'])
data['Buys'] = label_encoder_buys.fit_transform(data['Buys'])

# Features and target column
features = ['Age', 'Income', 'Gender', 'Ms']
target = 'Buys'

# Split the dataset into features and target
X = data[features]
y = data[target]

# Split data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Define the test data point: [Age < 21, Income = Low, Gender = Female, Marital Status = Married]
test_data = [[20, label_encoder_income.transform(['Low'])[0], label_encoder_gender.transform(['Female'])[0], label_encoder_ms.transform(['Married'])[0]]]

# Make prediction
prediction = clf.predict(test_data)

# Decode the prediction back to the original value
prediction_decoded = label_encoder_buys.inverse_transform(prediction)

# Print the prediction
print(f"The predicted response for the test data [Age < 21, Income = Low, Gender = Female, Marital Status = Married] is: {prediction_decoded[0]}")
