# 🫀 Heart Disease Prediction System

A modern, full-stack machine learning application for predicting heart disease using AI and providing a beautiful, responsive web interface.

## 📋 Features

- **AI-Powered Prediction**: Uses Logistic Regression model trained on clinical heart disease data
- **Modern UI**: Sleek, responsive design with gradient backgrounds and smooth animations
- **Real-time Analysis**: Instant predictions with confidence scores and probability metrics
- **Professional Interface**: Desktop-optimized with form validation and error handling
- **Backend API**: RESTful API built with Flask for secure data processing
- **Model Persistence**: Trained model saved as pickle file for quick loading

## 📁 Project Structure

```
Heart-disease-project/
├── backend/
│   ├── app.py              # Flask API server
│   ├── train.py            # Model training script
│   └── __pycache__/
├── frontend/
│   ├── index.html          # Main HTML interface
│   ├── styles.css          # Modern CSS styling
│   └── script.js           # Frontend logic
├── models/
│   ├── heart_disease_model.pkl  # Trained ML model
│   └── features.pkl             # Feature names list
├── heart.csv               # Training dataset
├── heart- dieases.ipynb    # Original Jupyter notebook
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A modern web browser (Chrome, Firefox, Edge, Safari)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd Heart-disease-project
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   
   **On Windows**:
   ```bash
   venv\Scripts\activate
   ```
   
   **On macOS/Linux**:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

### Step 1: Train the Model (First Time Only)

```bash
cd backend
python train.py
```

This will:
- Load the heart disease dataset
- Train the Logistic Regression model
- Save the model as `../models/heart_disease_model.pkl`
- Save feature names as `../models/features.pkl`

Expected output:
```
Dataset shape: (303, 14)
Training Accuracy: 0.8522
Test Accuracy: 0.8525
Model saved successfully at: ../models/heart_disease_model.pkl
Features saved at: ../models/features.pkl
```

### Step 2: Start the Backend Server

```bash
cd backend
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

Keep this terminal open while using the application.

### Step 3: Open the Frontend

1. Open `frontend/index.html` in your web browser
2. Or open it using a local server for better performance:
   
   **Using Python (Windows)**:
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   Then visit `http://localhost:8000` in your browser

## 📊 How to Use

1. **Fill in Patient Information**: Enter the 13 clinical metrics in the form
   - Age, Sex, Chest Pain Type, Blood Pressure, etc.

2. **Click "Predict"**: The system analyzes the data

3. **View Results**: Get instant prediction with:
   - Diagnosis (Disease or No Disease)
   - Confidence percentage
   - Individual probabilities

4. **Important**: Always consult a medical professional for actual diagnosis

## 📈 Dataset Features

The model uses 13 clinical features:

| Feature | Description | Range |
|---------|-------------|-------|
| **age** | Age in years | 29-77 |
| **sex** | Sex (1=Male, 0=Female) | 0-1 |
| **cp** | Chest pain type | 0-3 |
| **trestbps** | Resting blood pressure (mmHg) | 94-200 |
| **chol** | Serum cholesterol (mg/dl) | 126-564 |
| **fbs** | Fasting blood sugar > 120 | 0-1 |
| **restecg** | Resting ECG results | 0-2 |
| **thalach** | Max heart rate achieved | 71-202 |
| **exang** | Exercise induced angina | 0-1 |
| **oldpeak** | ST depression (0-6.2) | 0-6.2 |
| **slope** | Slope of ST segment | 0-2 |
| **ca** | Coronary arteries | 0-3 |
| **thal** | Thalassemia type | 1-3 |

## 🔌 API Endpoints

### Health Check
```http
GET /api/health
```

### Get Features
```http
GET /api/features
```

### Make Prediction
```http
POST /api/predict
Content-Type: application/json

{
  "age": 70,
  "sex": 1,
  "cp": 0,
  "trestbps": 145,
  "chol": 174,
  "fbs": 0,
  "restecg": 1,
  "thalach": 125,
  "exang": 1,
  "oldpeak": 2.6,
  "slope": 0,
  "ca": 0,
  "thal": 3
}
```

**Response**:
```json
{
  "prediction": 1,
  "prediction_text": "Heart Disease Detected",
  "confidence": 87.5,
  "probability_no_disease": 12.5,
  "probability_disease": 87.5
}
```

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework for Python
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **scikit-learn**: Machine Learning library
- **pandas**: Data manipulation
- **numpy**: Numerical computing

### Frontend
- **HTML5**: Markup structure
- **CSS3**: Modern styling with gradients and animations
- **Vanilla JavaScript**: No dependencies required
- **Responsive Design**: Mobile-friendly

## 📊 Model Information

- **Algorithm**: Logistic Regression
- **Training Data**: 303 patient records with 13 features
- **Training Accuracy**: ~85.2%
- **Test Accuracy**: ~85.2%
- **Target Variable**: Heart disease presence (0 or 1)

## ⚠️ Disclaimer

This application is for **educational and informational purposes only**. It should NOT be used as a substitute for:
- Professional medical advice
- Diagnosis from a licensed physician
- Clinical judgment
- Medical testing

Always consult with a healthcare professional for actual medical diagnosis and treatment.

## 🐛 Troubleshooting

### Backend API not connecting
- Ensure Flask server is running: `python backend/app.py`
- Check that port 5000 is available
- Verify firewall settings

### Model not found
- Run `python backend/train.py` first to generate pickle files
- Ensure `models/` folder exists with `.pkl` files

### CORS errors
- Flask-CORS is installed and configured
- Make sure you're accessing from a web context

### Form validation errors
- Check all fields are filled correctly
- Age should be 0-120
- Numeric fields should contain valid numbers

## 📝 Files Description

| File | Purpose |
|------|---------|
| `backend/app.py` | Flask REST API server |
| `backend/train.py` | Model training and saving script |
| `frontend/index.html` | Main web interface |
| `frontend/styles.css` | Styling and animations |
| `frontend/script.js` | Frontend logic and API calls |
| `models/heart_disease_model.pkl` | Trained machine learning model |
| `requirements.txt` | Python package dependencies |

## 🎓 Learning Resources

- [scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 📧 Support

For issues or questions, review the code comments or consult the documentation.

## 📄 License

This project is for educational purposes.

---

**Created**: 2024
**Status**: Active
**Version**: 1.0.0

Made with ❤️ for health and technology
