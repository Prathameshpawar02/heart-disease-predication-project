import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'heart.csv'
MODELS_DIR = BASE_DIR / 'models'

# Load the CSV data
heart_data = pd.read_csv(DATA_PATH)

print("Dataset shape:", heart_data.shape)
print("\nChecking for missing values:")
print(heart_data.isnull().sum())

# Split features and target
x = heart_data.drop(columns='target')
y = heart_data['target']

print(f"\nFeatures shape: {x.shape}")
print(f"Target shape: {y.shape}")

# Split into training and test data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, stratify=y, random_state=2
)

print(f"\nTraining set size: {x_train.shape[0]}")
print(f"Test set size: {x_test.shape[0]}")

# Train Logistic Regression model
print("\nTraining the Logistic Regression model...")
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# Evaluate the model
x_train_prediction = model.predict(x_train)
training_accuracy = accuracy_score(x_train_prediction, y_train)

x_test_prediction = model.predict(x_test)
test_accuracy = accuracy_score(x_test_prediction, y_test)

print(f"\nTraining Accuracy: {training_accuracy:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# Save the model as pickle file
MODELS_DIR.mkdir(parents=True, exist_ok=True)

model_path = MODELS_DIR / 'heart_disease_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"\nModel saved successfully at: {model_path}")

# Save feature names for reference
features_path = MODELS_DIR / 'features.pkl'
with open(features_path, 'wb') as f:
    pickle.dump(x.columns.tolist(), f)

print(f"Features saved at: {features_path}")
