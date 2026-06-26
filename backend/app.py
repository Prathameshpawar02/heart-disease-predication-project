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
        # Get JSON data from request
        data = request.get_json()
        
        # Extract features in the correct order
        input_features = []
        for feature in feature_names:
            if feature not in data:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
            input_features.append(float(data[feature]))
        
        # Convert to numpy array and reshape
        input_array = np.array(input_features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0]
        
        result = {
            'prediction': int(prediction),
            'prediction_text': 'Heart Disease Detected' if prediction == 1 else 'No Heart Disease',
            'confidence': float(max(probability) * 100),
            'probability_no_disease': float(probability[0] * 100),
            'probability_disease': float(probability[1] * 100)
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
