@echo off
REM Heart Disease Prediction - Frontend Server (Optional)
echo.
echo ========================================
echo Starting Frontend Development Server
echo ========================================
echo.
echo The frontend will be available at: http://localhost:8000
echo Make sure the backend (app.py) is already running!
echo.
echo Press Ctrl+C to stop the server
echo.

cd frontend
python -m http.server 8000
