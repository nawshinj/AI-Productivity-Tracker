# AI Productivity Tracker

A comprehensive **Knowledge-Based Expert System** for personalized productivity recommendations using rule-based inference.

## 🎯 Project Overview

The AI Productivity Tracker is a web application that helps users improve their daily productivity by analyzing their work habits and providing personalized, data-driven recommendations. It uses a rule-based inference engine with 31+ IF-THEN rules to evaluate user inputs and generate insights without any machine learning or external AI services.

## ✨ Key Features

### Core Functionality
- ✅ **Rule-Based Inference Engine** with 31+ productivity rules
- ✅ **Personalized Recommendations** based on user habits
- ✅ **Productivity Scoring** (0-100 scale)
- ✅ **Comprehensive Analysis** of multiple productivity factors
- ✅ **Visual Analytics** with interactive Plotly charts
- ✅ **Historical Tracking** with CSV data storage
- ✅ **Daily Routine Generation** optimized for your work style
- ✅ **Achievement Badges** and Streak Tracking

### Analysis Metrics
1. **Productivity Score** - Combines task completion, focus, sleep, exercise, and stress
2. **Focus Analysis** - Evaluates concentration levels
3. **Stress Analysis** - Assesses stress and coping strategies
4. **Time Management** - Analyzes task completion efficiency
5. **Health & Wellness** - Tracks sleep, hydration, and exercise

## 📋 Knowledge Base

### 31 Productivity Rules Include:
1. Low task completion & low focus
2. Insufficient sleep
3. High stress level
4. High distraction level
5. Screen time overload
6. No exercise
7. Excellent task completion
8. Very low focus
9. Low water intake
10. Time management needed
...and 21 more rules

### Rule Confidence Levels
- **High**: Critical productivity factors
- **Medium**: Supporting factors
- **Low**: Secondary considerations

## 🛠️ Technology Stack

- **Python 3** - Core language
- **Streamlit** - Frontend web framework
- **Pandas** - Data analysis and CSV handling
- **Plotly** - Interactive visualizations
- **ReportLab** - PDF generation (optional)
- **No Machine Learning** - Pure rule-based system
- **No External APIs** - Fully offline

## 📦 Project Structure

```
AI_Productivity_Tracker/
├── app.py                      # Main Streamlit application
├── knowledge_base.py           # 31 productivity rules
├── inference_engine.py         # Rule evaluation engine
├── productivity.py             # Productivity analysis
├── recommendations.py          # Recommendation system
├── charts.py                   # Visualization functions
├── history.py                  # History tracking
├── utils.py                    # Utility functions
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── data/
│   ├── productivity_history.csv # Historical data
│   └── sample_data.csv         # Sample data
│
└── reports/
    └── (Generated PDF reports)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/nawshinj/AI-Productivity-Tracker.git
cd AI-Productivity-Tracker
```

#### 2. Create Virtual Environment

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

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Application
```bash
streamlit run app.py
```

The application will automatically open in your browser at:
```
http://localhost:8501
```

## 📖 How to Use

### 1. Complete Daily Assessment
- Navigate to **Assessment** tab
- Fill in your personal information
- Enter daily metrics (hours worked, tasks, focus level, etc.)
- Specify your work style and stress level
- Select your productivity goal

### 2. Generate Productivity Report
- Click **"Generate Productivity Report"** button
- Receive instant analysis and recommendations
- View detailed charts and insights

### 3. Review Results
- **Productivity Score** (0-100)
- **Focus & Stress Analysis**
- **Time Management Insights**
- **Top 5 Recommendations**
- **Suggested Daily Routine**
- **Motivation Quote**
- **Achievement Badge**

### 4. Track Progress
- Visit **Analytics** page
- View weekly/monthly statistics
- Monitor productivity streaks
- Identify improvement areas

## 📊 Inference Engine Logic

### How Rules Are Evaluated

1. **Input Collection** - User provides daily metrics
2. **Rule Matching** - Engine checks all 31 rules against user data
3. **Condition Evaluation** - Rules trigger based on IF conditions
4. **Recommendation Firing** - THEN recommendations are generated
5. **Prioritization** - Recommendations ranked by confidence
6. **Score Calculation** - Productivity score computed
7. **Insight Generation** - Actionable insights provided

### Example Rule Flow

```
IF (completed_percentage <= 70) AND (focus_level <= 4)
THEN recommend:
  - Reduce distractions
  - Use Pomodoro Technique
  - Break tasks into smaller parts
  - Set single focus area
CONFIDENCE: High
```

## 📈 Productivity Score Calculation

```
Total Score = (Task Completion × 40%) + 
              (Focus Level × 30%) + 
              (Sleep Quality × 15%) + 
              (Exercise × 10%) - 
              (Stress Penalty × 5%)

Max: 100 | Min: 0
```

### Score Levels
- **85-100** ⭐ Excellent
- **70-84** ✨ Very Good
- **60-69** 👍 Good
- **50-59** 👌 Average
- **40-49** 📈 Below Average
- **0-39** ⚠️ Needs Improvement

## 🎮 Features Overview

### Dashboard
- Weekly productivity average
- Best day performance
- Total sessions tracked
- Consistency percentage
- Weekly trend visualization

### Assessment
- 4-tab interface for easy data entry
- Personal information section
- Daily activity metrics
- Work style analysis
- Productivity goal selection
- Sample data loader for testing

### Analytics
- Weekly statistics
- Monthly trends
- Productivity streaks
- Improvement area identification
- Historical data visualization

### Help
- System overview
- Usage instructions
- Technical information
- Rule explanations

## 💾 Data Management

### CSV Storage
- All data saved locally in `data/productivity_history.csv`
- Automatic backup of each assessment
- No cloud uploads or external storage
- Full privacy guaranteed

### Data Fields Tracked
- Timestamp
- User name
- Productivity score
- Task completion percentage
- Focus level
- Stress level
- Sleep hours
- Exercise status

## 🎓 Example Usage Scenario

### John's Workflow
1. **Morning Assessment**: Logs sleep (7h), water (2L), plans 5 tasks
2. **Midday Update**: Completes 3 tasks, focus is 6/10
3. **Report Generation**: Gets score of 72 (Good)
4. **Recommendations**: "Take a 15-min break", "Reduce screen time"
5. **Progress Tracking**: Trends show improvement over 4 weeks

## 📱 System Requirements

### Minimum Requirements
- Python 3.8+
- 100MB disk space
- 2GB RAM
- Windows 7+ / macOS 10.12+ / Linux

### Recommended
- Python 3.10+
- 500MB disk space
- 4GB RAM
- Modern web browser (Chrome, Firefox, Edge)

## 🔒 Privacy & Security

- ✅ **Fully Offline** - No internet required
- ✅ **Local Storage** - Data never leaves your computer
- ✅ **No Cloud Services** - No external APIs
- ✅ **No Tracking** - No telemetry or analytics
- ✅ **Open Source** - Transparent code

## 🚀 Future Enhancements

Potential features for future versions:
- [ ] PDF report generation
- [ ] Multi-user support
- [ ] Custom rule creation
- [ ] Advanced data export
- [ ] Team productivity dashboard
- [ ] Mobile app version
- [ ] Voice input for assessments
- [ ] Smart goal recommendations
- [ ] Habit tracking integration
- [ ] Calendar synchronization

## 📝 Sample Workflow

### Day 1: Initial Assessment
```
Input: 8 hours work, 5 planned tasks, 4 completed, 7/10 focus, 7h sleep
Output: Score 75 (Good), Recommendations: Improve focus
```

### Day 2: Progress Tracking
```
Input: 8.5 hours work, 6 planned tasks, 5 completed, 8/10 focus, 7.5h sleep
Output: Score 82 (Very Good), Badge: Rising Star
```

### Week 1 Review
```
Analytics: Average 76, Best 85, Streak 5 days
Insights: Improving focus, better time management needed
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional productivity rules
- New visualization types
- Performance optimizations
- Documentation improvements
- Bug fixes

## 📞 Support

For issues or questions:
1. Check the Help section in-app
2. Review the README documentation
3. Check requirements.txt for dependency versions
4. Verify Python version compatibility

## 📄 License

MIT License - Feel free to use, modify, and distribute

## 🙏 Acknowledgments

- Built with Streamlit
- Visualizations by Plotly
- Data analysis with Pandas
- Inspired by productivity science

## 📚 References

### Productivity Research
- Pomodoro Technique
- Eisenhower Matrix
- Work-life balance principles
- Sleep science
- Stress management techniques

### Technical Stack
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Python Official Documentation](https://docs.python.org/)

## ✅ Verification Checklist

- ✅ All files created and properly organized
- ✅ 31 productivity rules implemented
- ✅ Rule-based inference engine functional
- ✅ Streamlit UI complete and responsive
- ✅ Data storage working locally
- ✅ Analytics and charts rendering
- ✅ Comprehensive help documentation
- ✅ No machine learning or external APIs
- ✅ Runs on localhost:8501
- ✅ Works completely offline

---

**Happy Productivity Tracking!** 🚀

*Last Updated: 2024*
*Version: 1.0*
