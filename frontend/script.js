// API Configuration
const API_URL = 'http://localhost:5000';

// DOM Elements
const form = document.getElementById('predictionForm');
const resultContainer = document.getElementById('resultContainer');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const errorText = document.getElementById('errorText');

// Form inputs
const inputs = {
    age: document.getElementById('age'),
    sex: document.getElementById('sex'),
    cp: document.getElementById('cp'),
    trestbps: document.getElementById('trestbps'),
    chol: document.getElementById('chol'),
    fbs: document.getElementById('fbs'),
    restecg: document.getElementById('restecg'),
    thalach: document.getElementById('thalach'),
    exang: document.getElementById('exang'),
    oldpeak: document.getElementById('oldpeak'),
    slope: document.getElementById('slope'),
    ca: document.getElementById('ca'),
    thal: document.getElementById('thal')
};

// Result elements
const predictionText = document.getElementById('predictionText');
const confidenceBar = document.getElementById('confidenceBar');
const confidenceValue = document.getElementById('confidenceValue');
const probNoDisease = document.getElementById('probNoDisease');
const probDisease = document.getElementById('probDisease');
const resultBox = document.getElementById('resultBox');
const resultIcon = resultBox.querySelector('.result-icon');
const resultSvg = document.getElementById('resultSvg');

// Form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    await makePrediction();
});

// Make prediction
async function makePrediction() {
    // Validate form
    if (!form.checkValidity()) {
        showError('Please fill all required fields');
        return;
    }

    // Prepare data
    const data = {
        age: parseInt(inputs.age.value),
        sex: parseInt(inputs.sex.value),
        cp: parseInt(inputs.cp.value),
        trestbps: parseInt(inputs.trestbps.value),
        chol: parseInt(inputs.chol.value),
        fbs: parseInt(inputs.fbs.value),
        restecg: parseInt(inputs.restecg.value),
        thalach: parseInt(inputs.thalach.value),
        exang: parseInt(inputs.exang.value),
        oldpeak: parseFloat(inputs.oldpeak.value),
        slope: parseInt(inputs.slope.value),
        ca: parseInt(inputs.ca.value),
        thal: parseInt(inputs.thal.value)
    };

    // Show loading
    showLoading();

    try {
        const response = await fetch(`${API_URL}/api/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Prediction failed');
        }

        const result = await response.json();
        displayResult(result);
    } catch (error) {
        showError(`Error: ${error.message}`);
        console.error('Prediction error:', error);
    }
}

// Display result
function displayResult(result) {
    const isDisease = result.prediction === 1;

    // Update text
    predictionText.textContent = result.prediction_text;

    // Update confidence bar
    confidenceValue.textContent = `${result.confidence.toFixed(1)}%`;
    confidenceBar.style.width = `${result.confidence}%`;
    
    if (isDisease) {
        confidenceBar.classList.add('disease');
    } else {
        confidenceBar.classList.remove('disease');
    }

    // Update probabilities
    probNoDisease.textContent = `${result.probability_no_disease.toFixed(1)}%`;
    probDisease.textContent = `${result.probability_disease.toFixed(1)}%`;

    // Update icon
    if (isDisease) {
        resultIcon.classList.add('disease');
        resultIcon.innerHTML = `
            <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z"/>
            </svg>
        `;
    } else {
        resultIcon.classList.remove('disease');
        resultIcon.innerHTML = `
            <svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
            </svg>
        `;
    }

    // Hide loading and error, show result
    hideLoading();
    hideError();
    showResult();
}

// Show/Hide functions
function showLoading() {
    loadingSpinner.classList.remove('loading-hidden');
    resultContainer.classList.add('result-hidden');
    errorMessage.classList.add('error-hidden');
}

function hideLoading() {
    loadingSpinner.classList.add('loading-hidden');
}

function showResult() {
    resultContainer.classList.remove('result-hidden');
}

function showError(message) {
    errorText.textContent = message;
    errorMessage.classList.remove('error-hidden');
    resultContainer.classList.add('result-hidden');
    hideLoading();
}

function hideError() {
    errorMessage.classList.add('error-hidden');
}

// Initialize
window.addEventListener('load', () => {
    console.log('Heart Disease Prediction System loaded');
    console.log('API URL:', API_URL);

    // Check API connection
    checkAPIConnection();
});

// Check API connection
async function checkAPIConnection() {
    try {
        const response = await fetch(`${API_URL}/api/health`);
        if (response.ok) {
            console.log('✓ Connected to backend API');
        } else {
            console.warn('⚠ Backend API connection issue');
        }
    } catch (error) {
        console.warn('⚠ Cannot connect to backend API at', API_URL);
        console.warn('Make sure the Flask server is running on port 5000');
    }
}

// Load sample data (for testing)
window.loadSampleData = function() {
    inputs.age.value = 70;
    inputs.sex.value = 1;
    inputs.cp.value = 0;
    inputs.trestbps.value = 145;
    inputs.chol.value = 174;
    inputs.fbs.value = 0;
    inputs.restecg.value = 1;
    inputs.thalach.value = 125;
    inputs.exang.value = 1;
    inputs.oldpeak.value = 2.6;
    inputs.slope.value = 0;
    inputs.ca.value = 0;
    inputs.thal.value = 3;
    console.log('Sample data loaded');
};
