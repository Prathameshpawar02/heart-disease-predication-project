from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os
import json

app = Flask(__name__)
CORS(app)

# Load the trained model and features
model_path = os.path.join(os.path.dirname(__file__), '../models/heart_disease_model.pkl')
features_path = os.path.join(os.path.dirname(__file__), '../models/features.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

with open(features_path, 'rb') as f:
    feature_names = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Heart Disease Prediction API is running!'})

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not isinstance(data, dict):
            return jsonify({'error': 'Expected a JSON object'}), 400

        input_features = []
        for feature in feature_names:
            if feature not in data:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
            input_features.append(float(data[feature]))

        input_array = np.array(input_features).reshape(1, -1)

        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0]
        class_labels = list(model.classes_)

        if len(class_labels) != 2:
            return jsonify({'error': 'Model does not support binary classification'}), 400

        negative_class = 0 if 0 in class_labels else class_labels[0]
        positive_class = 1 if 1 in class_labels else class_labels[1]

        negative_index = class_labels.index(negative_class)
        positive_index = class_labels.index(positive_class)

        probability_no_disease = float(probability[negative_index] * 100)
        probability_disease = float(probability[positive_index] * 100)

        predicted_class = int(prediction)
        prediction_text = 'Heart Disease Detected' if predicted_class == positive_class else 'No Heart Disease'

        result = {
            'prediction': predicted_class,
            'prediction_text': prediction_text,
            'confidence': float(max(probability) * 100),
            'probability_no_disease': probability_no_disease,
            'probability_disease': probability_disease
        }

        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/features', methods=['GET'])
def get_features():
    return jsonify({'features': feature_names})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
