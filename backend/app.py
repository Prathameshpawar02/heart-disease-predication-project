import os
import pickle
from pathlib import Path

import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)
CORS(app)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "heart.csv"
MODELS_DIR = BASE_DIR / "models"
MODEL_PATH = MODELS_DIR / "heart_disease_model.pkl"
FEATURES_PATH = MODELS_DIR / "features.pkl"


def train_and_save_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Training data not found at {DATA_PATH}")

    heart_data = pd.read_csv(DATA_PATH)
    X = heart_data.drop(columns=["target"])
    y = heart_data["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=2
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    with MODEL_PATH.open("wb") as model_file:
        pickle.dump(model, model_file)

    with FEATURES_PATH.open("wb") as features_file:
        pickle.dump(X.columns.tolist(), features_file)

    training_accuracy = accuracy_score(model.predict(X_train), y_train)
    test_accuracy = accuracy_score(model.predict(X_test), y_test)

    return model, X.columns.tolist(), training_accuracy, test_accuracy


def load_model_and_features():
    if not MODEL_PATH.exists() or not FEATURES_PATH.exists():
        return train_and_save_model()

    try:
        with MODEL_PATH.open("rb") as model_file:
            model = pickle.load(model_file)
        with FEATURES_PATH.open("rb") as features_file:
            feature_names = pickle.load(features_file)
        return model, feature_names, None, None
    except Exception:
        return train_and_save_model()


model, feature_names, training_accuracy, test_accuracy = load_model_and_features()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Heart Disease Prediction API is running!"})


@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Expected a JSON object"}), 400

        missing_features = [feature for feature in feature_names if feature not in data]
        if missing_features:
            return jsonify({"error": f"Missing feature(s): {', '.join(missing_features)}"}), 400

        input_features = [float(data[feature]) for feature in feature_names]
        input_array = np.array(input_features, dtype=float).reshape(1, -1)

        prediction = int(model.predict(input_array)[0])
        probability = model.predict_proba(input_array)[0]
        class_labels = list(model.classes_)

        if len(class_labels) != 2:
            return jsonify({"error": "Model does not support binary classification"}), 400

        negative_class = 0 if 0 in class_labels else class_labels[0]
        positive_class = 1 if 1 in class_labels else class_labels[1]

        negative_index = class_labels.index(negative_class)
        positive_index = class_labels.index(positive_class)

        probability_no_disease = float(probability[negative_index] * 100)
        probability_disease = float(probability[positive_index] * 100)

        predicted_class = int(prediction)
        prediction_text = "Heart Disease Detected" if predicted_class == positive_class else "No Heart Disease"

        result = {
            "prediction": predicted_class,
            "prediction_text": prediction_text,
            "confidence": float(max(probability) * 100),
            "probability_no_disease": probability_no_disease,
            "probability_disease": probability_disease,
        }
        return jsonify(result)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/api/features", methods=["GET"])
def get_features():
    return jsonify({"features": feature_names})


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify(
        {
            "status": "healthy",
            "model_loaded": model is not None,
            "training_accuracy": training_accuracy,
            "test_accuracy": test_accuracy,
        }
    )


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("DEBUG", "false").lower() in {"1", "true", "yes", "on"}
    app.run(host=host, port=port, debug=debug)
