# AI Productivity Tracker - System Architecture

## Overview

The AI Productivity Tracker is a rule-based expert system that analyzes user productivity data and generates personalized recommendations using IF-THEN rules.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    STREAMLIT USER INTERFACE                      │
│  ┌─────────────┬──────────────┬──────────────┬──────────────┐   │
│  │  Dashboard  │ Assessment   │  Analytics   │     Help     │   │
│  └─────────────┴──────────────┴──────────────┴──────────────┘   │
└─────────────────────┬──────────────────────────────────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │   USER DATA INPUT HANDLER  │
         │   (Personal Info, Metrics) │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │   INFERENCE ENGINE         │
         │  ┌──────────────────────┐  │
         │  │ Rule Evaluator       │  │
         │  │ (31 IF-THEN Rules)   │  │
         │  └──────────────────────┘  │
         │  ┌──────────────────────┐  │
         │  │ Score Calculator     │  │
         │  │ (Weighted Formula)   │  │
         │  └──────────────────────┘  │
         │  ┌──────────────────────┐  │
         │  │ Recommender          │  │
         │  │ (Priority Logic)     │  │
         │  └──────────────────────┘  │
         └────────────┬───────────────┘
                      │
                      ▼
         ┌────────────────────────────┐
         │  KNOWLEDGE BASE            │
         │  (31 Productivity Rules)   │
         └────────────┬───────────────┘
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
   ┌────────┐   ┌────────┐   ┌────────────┐
   │ Focus  │   │ Stress │   │ Time Mgmt  │
   │ Rules  │   │ Rules  │   │ Rules      │
   └────────┘   └────────┘   └────────────┘
        │             │              │
        └─────────────┼──────────────┘
                      ▼
         ┌────────────────────────────┐
         │   ANALYSIS RESULTS         │
         │  ┌──────────────────────┐  │
         │  │ Productivity Score   │  │
         │  │ Focus Analysis       │  │
         │  │ Stress Analysis      │  │
         │  │ Recommendations      │  │
         │  │ Daily Routine        │  │
         │  │ Achievement Badge    │  │
         │  └──────────────────────┘  │
         └────────────┬───────────────┘
                      │
        ┌─────────────┼──────────────┐
        ▼             ▼              ▼
   ┌────────┐   ┌────────┐   ┌────────────┐
   │Visuali-│   │Recommen-│  │ Historical │
   │zations │   │dations  │  │ Storage    │
   │(Plotly)│   │ (Text)  │  │ (CSV)      │
   └────────┘   └────────┘   └────────────┘
```

## Core Components

### 1. User Interface Layer (Streamlit)
- Dashboard for overview
- Assessment form for data collection
- Analytics for historical trends
- Help and documentation

### 2. Input Processing
- Form validation
- Data normalization
- Error handling
- Session management

### 3. Inference Engine
The heart of the system:
- **Rule Evaluator**: Checks conditions against user data
- **Score Calculator**: Weighted formula for productivity score
- **Recommender**: Prioritizes recommendations by confidence
- **Analyzer**: Generates insights and daily routine

### 4. Knowledge Base
31 IF-THEN rules covering:
- Focus and concentration
- Stress management
- Time management
- Health and wellness
- Work style matching
- Goal alignment

### 5. Output Generation
- Charts and visualizations
- Recommendations text
- Daily routine suggestions
- Achievement badges
- Motivation quotes

### 6. Data Persistence
- CSV file storage
- Session state management
- Historical data tracking
- Analytics computation

## Data Flow

```
1. USER INPUT
   ├─ Personal Info (name, age, occupation)
   ├─ Daily Metrics (hours, tasks, focus, sleep)
   ├─ Work Style (time, distraction, stress)
   └─ Goals (productivity objectives)
       ↓
2. VALIDATION & NORMALIZATION
   ├─ Check ranges
   ├─ Convert units
   ├─ Calculate derived values
   └─ Prepare for inference
       ↓
3. RULE EVALUATION
   ├─ Load 31 rules from knowledge base
   ├─ Check each rule's conditions
   ├─ Collect applicable rules
   └─ Extract recommendations
       ↓
4. SCORE CALCULATION
   ├─ Task Completion (40%)
   ├─ Focus Level (30%)
   ├─ Sleep Quality (15%)
   ├─ Exercise (10%)
   ├─ Stress Penalty (-5%)
   └─ Final Score (0-100)
       ↓
5. ANALYSIS GENERATION
   ├─ Focus Analysis
   ├─ Stress Analysis
   ├─ Time Management Insights
   ├─ Daily Routine Generation
   ├─ Achievement Badge Assignment
   └─ Confidence Level Calculation
       ↓
6. VISUALIZATION
   ├─ Productivity Gauge Chart
   ├─ Focus Level Chart
   ├─ Task Completion Pie Chart
   ├─ Health Metrics Radar
   └─ Weekly Trend Line
       ↓
7. DATA PERSISTENCE
   ├─ Save to productivity_history.csv
   ├─ Update session state
   └─ Prepare for future analysis
```

## Rule Evaluation Algorithm

```python
For each rule in knowledge_base:
    conditions_met = True
    for condition in rule.conditions:
        if not evaluate_condition(condition, user_data):
            conditions_met = False
            break
    
    if conditions_met:
        applicable_rules.append(rule)
        for recommendation in rule.recommendations:
            add_to_recommendations(recommendation)

return applicable_rules, recommendations
```

## Productivity Score Formula

```
Score = (Completion% × 0.40) +
        (Focus_Level × 3) +
        (Sleep_Score × 0.15) +
        (Exercise × 0.10) -
        (Stress_Penalty × 0.05)

Where:
- Completion% = (Completed / Planned) × 100
- Focus_Level = 1-10 scale
- Sleep_Score = 15 if ≥7h, 10 if ≥6h, 5 if ≥5h, else 0
- Exercise = 10 if True, else 0
- Stress_Penalty = 5 if High, 2 if Medium, 0 if Low

Min: 0, Max: 100
```

## File Structure

```
app.py
├─ main() - Application entry point
├─ show_assessment() - Assessment page
├─ show_dashboard() - Dashboard page
├─ show_analytics() - Analytics page
├─ show_results() - Display results
└─ show_help() - Help page

knowledge_base.py
└─ ProductivityRules
   ├─ _initialize_rules() - Load 31 rules
   ├─ get_applicable_rules() - Evaluate rules
   └─ _check_conditions() - Condition evaluation

inference_engine.py
└─ InferenceEngine
   ├─ analyze_productivity() - Main analysis
   ├─ _calculate_productivity_score() - Score calc
   ├─ _generate_recommendations() - Rec generation
   ├─ _analyze_focus() - Focus analysis
   ├─ _analyze_stress() - Stress analysis
   └─ _generate_daily_routine() - Routine gen

productivity.py
└─ ProductivityAnalyzer
   ├─ analyze() - Main analysis method
   ├─ get_quick_tips() - Quick tips generation
   └─ get_achievement_unlocked() - Badge logic

recommendations.py
└─ RecommendationSystem
   ├─ get_time_management_recommendations()
   ├─ get_health_recommendations()
   ├─ get_focus_recommendations()
   └─ get_stress_management_recommendations()

charts.py
├─ create_productivity_gauge()
├─ create_focus_chart()
├─ create_task_completion_pie()
├─ create_weekly_trend()
├─ create_stress_level_chart()
└─ create_health_metrics()

history.py
└─ ProductivityHistory
   ├─ get_daily_summary()
   ├─ get_weekly_stats()
   ├─ get_monthly_stats()
   ├─ get_streaks()
   └─ get_improvement_areas()

utils.py
├─ ensure_data_directory()
├─ save_productivity_report()
├─ get_productivity_history()
├─ get_weekly_productivity_stats()
└─ format_time()
```

## Knowledge Base Structure

Each rule contains:
```python
{
    'id': int,
    'name': str,
    'conditions': {
        'metric_name': (operator, value)
    },
    'recommendations': [str],
    'confidence': str  # 'High' or 'Medium'
}
```

Example:
```python
{
    'id': 1,
    'name': 'Low Task Completion & Low Focus',
    'conditions': {
        'completed_percentage': ('<=', 70),
        'focus_level': ('<=', 4)
    },
    'recommendations': [
        '🎯 Reduce distractions',
        '⏱️ Use Pomodoro Technique',
        '✂️ Break tasks into smaller parts',
        '📍 Set single focus area'
    ],
    'confidence': 'High'
}
```

## Performance Characteristics

- **Rule Evaluation**: O(n) where n = 31 rules
- **Score Calculation**: O(1) - constant time
- **Report Generation**: < 1 second
- **CSV Operations**: < 100ms
- **Chart Rendering**: < 2 seconds

## Scalability Considerations

Current design supports:
- ✅ Single user unlimited assessments
- ✅ Up to 10,000+ historical records
- ✅ Real-time analysis
- ✅ Responsive UI with Streamlit

Future improvements:
- Multi-user support with database
- Custom rule creation UI
- Rule machine learning optimizer
- Mobile application

## Security & Privacy

- ✅ All data stored locally
- ✅ No internet required
- ✅ No external APIs
- ✅ No cloud uploads
- ✅ User controls all data

---

*System Architecture v1.0*
