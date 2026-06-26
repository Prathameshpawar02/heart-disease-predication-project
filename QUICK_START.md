## 🚀 QUICK START GUIDE

### For Windows Users

**Option 1: Automatic Setup (Recommended)**
1. Double-click `setup.bat` - This will install everything
2. Double-click `run_app.bat` - This will start the backend
3. Open `frontend/index.html` in your browser
4. Done! Start making predictions

**Option 2: Manual Setup**
```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
cd backend
python train.py
cd ..

# 5. Run the backend
cd backend
python app.py

# In another terminal, open the frontend
frontend/index.html
```

### For macOS/Linux Users

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the model
cd backend
python train.py
cd ..

# 5. Run the backend
cd backend
python app.py

# In another terminal, open the frontend
open frontend/index.html
# or
firefox frontend/index.html
```

### Test the System

Once everything is running:
1. Fill in the form with patient data
2. Click "Predict"
3. View the diagnosis with confidence scores

### Default Test Data
You can use the example from the notebook:
- Age: 70
- Sex: Male (1)
- Chest Pain: Typical Angina (0)
- Resting BP: 145
- Cholesterol: 174
- Fasting Sugar: No (0)
- Resting ECG: Normal (1)
- Max Heart Rate: 125
- Exercise Angina: Yes (1)
- Old Peak: 2.6
- Slope: Upsloping (0)
- Coronary Vessels: 0
- Thalassemia: Reversible Defect (3)

### Files Generated

After setup, you'll have:
- ✅ `models/heart_disease_model.pkl` - Trained model
- ✅ `models/features.pkl` - Feature names
- ✅ Virtual environment in `venv/` folder

### Troubleshooting

**Port 5000 already in use?**
```bash
cd backend
python app.py --port 5001
```
Then update `script.js` API_URL to `http://localhost:5001`

**Missing dependencies?**
```bash
pip install -r requirements.txt --upgrade
```

**Model not found?**
```bash
cd backend
python train.py
```

### Questions?
See `README.md` for complete documentation.

Happy predicting! 🫀
