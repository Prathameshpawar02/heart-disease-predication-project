@echo off
REM Heart Disease Prediction - Run Script for Windows
echo.
echo ========================================
echo Heart Disease Prediction System
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

echo Activating backend server...
echo.
echo Starting Flask server on http://localhost:5000
echo.
echo ========================================
echo Frontend: Open frontend/index.html in your browser
echo Backend: Running on port 5000
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
python app.py
