# Quick Start Guide

## Installation (5 minutes)

### 1. Prerequisites
```bash
# Check Python version (3.8+)
python --version
```

### 2. Setup Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
streamlit run app.py
```

### 5. Access Application
Open browser to: **http://localhost:8501**

---

## First Time Use

### Step 1: Load Sample Data
- Click "Assessment" tab
- Click "📥 Load Sample Data" button
- Report automatically generates

### Step 2: Explore Results
- View Productivity Score
- Check Top 5 Recommendations
- Review Daily Routine
- Check Focus & Stress Analysis

### Step 3: View Analytics
- Click "Analytics" tab
- See Weekly Statistics
- Review Monthly Trends
- Check Your Streaks

### Step 4: Create Your Own Assessment
- Fill in your personal information
- Enter today's metrics
- Specify your work style
- Select productivity goal
- Generate your report

---

## Features

✅ **Dashboard** - Overview of productivity metrics
✅ **Assessment** - Comprehensive daily evaluation
✅ **Analytics** - Track progress over time
✅ **Help** - System documentation

---

## Troubleshooting

### Issue: "Module not found"
**Solution:** Ensure virtual environment is activated and dependencies installed
```bash
pip install -r requirements.txt
```

### Issue: "Port 8501 already in use"
**Solution:** Streamlit will automatically use next available port

### Issue: "Data not saving"
**Solution:** Check that `data/` directory exists and is writable

---

## Contact & Support

For issues or questions, refer to the Help section in the application.
