# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess the Kaggle dataset
data = pd.read_csv('Breastcancer.csv')  # Update the dataset filename

# Replace 'diagnosis' with the actual column name that contains the diagnosis information
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Feature scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Create and train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Create a function to predict diagnoses for new patient data
def predict_diagnosis(new_patient_data):
    diagnosis = model.predict([new_patient_data])
    if diagnosis[0] == 'B':
        return "Benign"
    else:
        return "Malignant"

# Command-line interface to take patient data and make predictions
while True:
    print("Enter patient data:")
    mean_radius = float(input("Mean Radius: "))
    mean_texture = float(input("Mean Texture: "))
    mean_perimeter = float(input("Mean Perimeter: "))
    mean_area = float(input("Mean Area: "))
    mean_smoothness = float(input("Mean Smoothness: "))

    input_data = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]

    result = predict_diagnosis(input_data)
    print(f"Predicted Diagnosis: {result}")

    # Data Visualization for Input
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    plt.title("Input Data Visualization")

    # Create a bar plot to visualize the entered input data
    plt.bar(
        ["Mean Radius", "Mean Texture", "Mean Perimeter", "Mean Area", "Mean Smoothness"],
        input_data,
        color=['blue', 'green', 'red', 'purple', 'orange']
    )
    plt.ylabel("Value")
    plt.xticks(rotation=45)

    plt.show()
