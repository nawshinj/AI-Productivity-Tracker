"""
AI Productivity Tracker - Main Streamlit Application
A Knowledge-Based Expert System for personalized productivity recommendations
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import json

# Import custom modules
from knowledge_base import ProductivityRules
from inference_engine import InferenceEngine
from productivity import ProductivityAnalyzer
from recommendations import RecommendationSystem
from utils import save_productivity_report, get_productivity_history, get_weekly_productivity_stats
from charts import (
    create_productivity_gauge,
    create_focus_chart,
    create_task_completion_pie,
    create_weekly_trend,
    create_stress_level_chart,
    create_health_metrics
)
from history import ProductivityHistory


# Configure Streamlit
st.set_page_config(
    page_title="AI Productivity Tracker",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 30px;
    }
    .metric-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    .recommendation-box {
        padding: 15px;
        border-left: 4px solid #1f77b4;
        background-color: #f8f9fa;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)


def main():
    """Main application function"""
    
    # Initialize session state
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None
    
    # Header
    st.markdown("""
        <div class="header">
            <h1>🚀 AI Productivity Tracker</h1>
            <p>Knowledge-Based Expert System for Personalized Productivity Insights</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/rocket.png", width=80)
        st.title("Navigation")
        page = st.radio(
            "Select Page:",
            ["📊 Dashboard", "📝 Assessment", "📈 Analytics", "💡 Help"],
            index=0
        )
    
    # Page routing
    if page == "📊 Dashboard":
        show_dashboard()
    elif page == "📝 Assessment":
        show_assessment()
    elif page == "📈 Analytics":
        show_analytics()
    elif page == "💡 Help":
        show_help()


def show_assessment():
    """Show productivity assessment page"""
    st.markdown("### 📝 Daily Productivity Assessment")
    st.write("Please provide information about your daily productivity for personalized recommendations.")
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Personal Info", "📊 Daily Activity", "⚙️ Work Style", "🎯 Goals"])
    
    with tab1:
        st.subheader("Personal Information")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            name = st.text_input("Your Name", "User")
        with col2:
            age = st.number_input("Age", min_value=16, max_value=100, value=25)
        with col3:
            occupation = st.selectbox(
                "Occupation",
                ["Student", "Employee", "Freelancer", "Other"]
            )
    
    with tab2:
        st.subheader("Daily Activity Metrics")
        col1, col2 = st.columns(2)
        
        with col1:
            hours_worked = st.slider(
                "Hours Worked/Studied",
                min_value=0.0,
                max_value=16.0,
                value=8.0,
                step=0.5,
                help="Total productive work hours today"
            )
            
            planned_tasks = st.number_input(
                "Number of Planned Tasks",
                min_value=0,
                value=5,
                help="How many tasks did you plan to complete?"
            )
            
            completed_tasks = st.number_input(
                "Number of Completed Tasks",
                min_value=0,
                value=3,
                help="How many tasks did you complete?"
            )
        
        with col2:
            pending_tasks = st.number_input(
                "Number of Pending Tasks",
                min_value=0,
                value=2,
                help="How many tasks are still pending?"
            )
            
            focus_level = st.slider(
                "Average Focus Level (1-10)",
                min_value=1,
                max_value=10,
                value=6,
                help="Rate your average focus today"
            )
            
            sleep_hours = st.slider(
                "Sleep Hours Last Night",
                min_value=0.0,
                max_value=12.0,
                value=7.0,
                step=0.5,
                help="How many hours did you sleep?"
            )
        
        # Calculate completion percentage
        completed_percentage = (completed_tasks / planned_tasks * 100) if planned_tasks > 0 else 0
        
        col1, col2 = st.columns(2)
        with col1:
            water_intake = st.slider(
                "Water Intake (Liters)",
                min_value=0.0,
                max_value=5.0,
                value=2.0,
                step=0.25,
                help="How much water did you drink?"
            )
        
        with col2:
            exercise_today = st.checkbox(
                "Did you exercise today?",
                value=False,
                help="Check if you exercised today"
            )
    
    with tab3:
        st.subheader("Work Style & Environment")
        col1, col2 = st.columns(2)
        
        with col1:
            preferred_time = st.selectbox(
                "Preferred Working Time",
                ["Morning", "Afternoon", "Evening", "Night"],
                help="When do you work best?"
            )
            
            distraction_level = st.selectbox(
                "Distraction Level",
                ["Low", "Medium", "High"],
                help="How easily distracted were you today?"
            )
        
        with col2:
            stress_level = st.selectbox(
                "Stress Level",
                ["Low", "Medium", "High"],
                help="How stressed do you feel?"
            )
            
            screen_time = st.slider(
                "Screen Time (Hours)",
                min_value=0.0,
                max_value=16.0,
                value=6.0,
                step=0.5,
                help="Total screen time today"
            )
    
    with tab4:
        st.subheader("Productivity Goals")
        goal = st.selectbox(
            "Select Your Primary Goal",
            [
                "Increase Focus",
                "Improve Time Management",
                "Complete More Tasks",
                "Reduce Procrastination",
                "Maintain Productivity"
            ],
            help="What's your main focus area?"
        )
    
    # Generate Report Button
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎯 Generate Productivity Report", use_container_width=True):
            # Prepare user data
            user_data = {
                'name': name,
                'age': age,
                'occupation': occupation,
                'hours_worked': hours_worked,
                'planned_tasks': planned_tasks,
                'completed_tasks': completed_tasks,
                'pending_tasks': pending_tasks,
                'completed_percentage': completed_percentage,
                'focus_level': focus_level,
                'sleep_hours': sleep_hours,
                'water_intake': water_intake,
                'exercise_today': exercise_today,
                'preferred_time': preferred_time,
                'distraction_level': distraction_level,
                'stress_level': stress_level,
                'screen_time': screen_time,
                'goal': goal
            }
            
            # Store in session state
            st.session_state.user_data = user_data
            
            # Analyze productivity
            analyzer = ProductivityAnalyzer()
            analysis_result = analyzer.analyze(user_data)
            st.session_state.analysis_result = analysis_result
            
            # Save to history
            save_productivity_report(user_data, analysis_result)
            
            st.success("✅ Report generated successfully!")
            st.balloons()
    
    with col2:
        if st.button("🔄 Reset Form", use_container_width=True):
            st.session_state.user_data = None
            st.session_state.analysis_result = None
            st.rerun()
    
    with col3:
        if st.button("📥 Load Sample Data", use_container_width=True):
            # Load sample data
            sample_data = {
                'name': 'John Doe',
                'age': 28,
                'occupation': 'Employee',
                'hours_worked': 8.5,
                'planned_tasks': 6,
                'completed_tasks': 5,
                'pending_tasks': 1,
                'completed_percentage': 83.33,
                'focus_level': 7,
                'sleep_hours': 7.5,
                'water_intake': 2.5,
                'exercise_today': True,
                'preferred_time': 'Morning',
                'distraction_level': 'Low',
                'stress_level': 'Low',
                'screen_time': 5.5,
                'goal': 'Maintain Productivity'
            }
            st.session_state.user_data = sample_data
            analyzer = ProductivityAnalyzer()
            analysis_result = analyzer.analyze(sample_data)
            st.session_state.analysis_result = analysis_result
            st.success("✅ Sample data loaded!")
            st.rerun()
    
    # Show results if available
    if st.session_state.analysis_result:
        st.markdown("---")
        show_results(st.session_state.user_data, st.session_state.analysis_result)


def show_results(user_data, analysis_result):
    """Display analysis results"""
    st.markdown("### 📊 Productivity Analysis Results")
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Productivity Score",
            f"{analysis_result.get('productivity_score', 0)}/100",
            delta=f"{analysis_result.get('productivity_score', 0) - 70}"
        )
    
    with col2:
        st.metric(
            "Productivity Level",
            analysis_result.get('productivity_level', 'Unknown'),
        )
    
    with col3:
        st.metric(
            "Focus Score",
            f"{analysis_result.get('focus_score', 0)}/10",
        )
    
    with col4:
        st.metric(
            "Badge",
            analysis_result.get('badge', 'Learning'),
        )
    
    # Charts section
    st.markdown("#### 📈 Visual Analytics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(
            create_productivity_gauge(analysis_result.get('productivity_score', 0)),
            use_container_width=True
        )
    
    with col2:
        st.plotly_chart(
            create_focus_chart(user_data.get('focus_level', 5)),
            use_container_width=True
        )
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            create_task_completion_pie(
                user_data.get('completed_tasks', 0),
                user_data.get('pending_tasks', 0),
                user_data.get('planned_tasks', 0)
            ),
            use_container_width=True
        )
    
    with col2:
        st.plotly_chart(
            create_health_metrics(
                user_data.get('sleep_hours', 0),
                user_data.get('water_intake', 0),
                user_data.get('exercise_today', False)
            ),
            use_container_width=True
        )
    
    # Detailed analysis
    st.markdown("#### 📋 Detailed Analysis")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["🎯 Focus", "😰 Stress", "⏰ Time Mgmt", "📝 Priority", "☕ Breaks"]
    )
    
    with tab1:
        focus_analysis = analysis_result.get('focus_analysis', {})
        st.markdown(f"**{focus_analysis.get('level', 'Unknown')}**")
        st.write(focus_analysis.get('message', ''))
        st.markdown("**Tips:**")
        for tip in focus_analysis.get('tips', []):
            st.write(f"• {tip}")
    
    with tab2:
        stress_analysis = analysis_result.get('stress_analysis', {})
        st.markdown(f"**{stress_analysis.get('level', 'Unknown')}**")
        st.write(stress_analysis.get('message', ''))
        st.markdown("**Coping Strategies:**")
        for strategy in stress_analysis.get('coping_strategies', []):
            st.write(f"• {strategy}")
    
    with tab3:
        time_mgmt = analysis_result.get('time_management', {})
        st.write(f"**Planned Tasks:** {time_mgmt.get('planned', 0)}")
        st.write(f"**Completed Tasks:** {time_mgmt.get('completed', 0)}")
        st.write(f"**Pending Tasks:** {time_mgmt.get('pending', 0)}")
        st.write(f"**Efficiency:** {time_mgmt.get('efficiency', 0)}%")
        st.markdown("**Suggestions:**")
        for suggestion in time_mgmt.get('suggestions', []):
            st.write(f"• {suggestion}")
    
    with tab4:
        task_priority = analysis_result.get('task_priority', {})
        st.markdown(f"**{task_priority.get('strategy', 'Unknown')}**")
        for order in task_priority.get('priority_order', []):
            st.write(f"• {order}")
        st.info(task_priority.get('quick_tip', ''))
    
    with tab5:
        break_recs = analysis_result.get('break_recommendations', {})
        st.write(f"**Frequency:** {break_recs.get('frequency', 'Unknown')}")
        st.write(f"**Duration:** {break_recs.get('duration', 'Unknown')}")
        st.markdown("**Recommended Activities:**")
        for activity in break_recs.get('activities', []):
            st.write(f"• {activity}")
    
    # Top recommendations
    st.markdown("#### 🎯 Top 5 Recommendations")
    for i, rec in enumerate(analysis_result.get('recommendations', [])[:5], 1):
        st.markdown(f"**{i}. {rec}**")
    
    # Daily routine
    st.markdown("#### 📅 Recommended Daily Routine")
    routine = analysis_result.get('daily_routine', [])
    routine_text = "\n".join(routine)
    st.code(routine_text, language="text")
    
    # Motivation
    st.markdown("#### 💪 Daily Motivation")
    st.info(analysis_result.get('motivation_quote', 'Keep going!'))
    
    # Confidence level
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Confidence Level", analysis_result.get('confidence_level', 'Unknown'))
    with col2:
        st.metric("Applicable Rules", analysis_result.get('applicable_rules', 0))
    with col3:
        st.metric("Insights Found", len(analysis_result.get('insights', [])))


def show_dashboard():
    """Show main dashboard"""
    st.markdown("### 📊 Productivity Dashboard")
    
    # Quick stats
    history = get_productivity_history()
    if history:
        weekly_stats = get_weekly_productivity_stats()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Weekly Average Score",
                f"{weekly_stats.get('average_score', 0):.1f}",
                delta="+5"
            )
        
        with col2:
            st.metric(
                "Best Day",
                f"{weekly_stats.get('best_day', 0):.0f}",
            )
        
        with col3:
            st.metric(
                "Total Sessions",
                weekly_stats.get('total_sessions', 0),
            )
        
        with col4:
            st.metric(
                "Consistency",
                f"{(weekly_stats.get('total_sessions', 0) / 7 * 100):.0f}%",
            )
        
        # Charts
        st.markdown("---")
        st.plotly_chart(create_weekly_trend(), use_container_width=True)
        
        # Recent history
        st.markdown("#### 📝 Recent Sessions")
        recent_df = pd.DataFrame(history[-5:])
        if len(recent_df) > 0:
            st.dataframe(
                recent_df[['timestamp', 'name', 'productivity_score', 'completed_percentage']],
                use_container_width=True
            )
    else:
        st.info("📊 No productivity data yet. Complete an assessment to see your dashboard!")
        if st.button("📝 Start Assessment"):
            st.switch_page("pages/assessment.py")


def show_analytics():
    """Show analytics page"""
    st.markdown("### 📈 Advanced Analytics")
    
    history = get_productivity_history()
    
    if not history:
        st.info("No data available. Complete assessments to see analytics.")
        return
    
    tab1, tab2, tab3 = st.tabs(["📊 Weekly Stats", "📅 Monthly Stats", "🏆 Streaks"])
    
    with tab1:
        weekly = ProductivityHistory.get_weekly_stats()
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Average Score", f"{weekly.get('avg_score', 0):.1f}")
        with col2:
            st.metric("Best Score", f"{weekly.get('best_score', 0):.0f}")
        with col3:
            st.metric("Avg Completion", f"{weekly.get('avg_completion', 0):.0f}%")
        with col4:
            st.metric("Sessions", weekly.get('total_sessions', 0))
    
    with tab2:
        monthly = ProductivityHistory.get_monthly_stats()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Score", f"{monthly.get('avg_score', 0):.1f}")
        with col2:
            st.metric("Best Score", f"{monthly.get('best_score', 0):.0f}")
        with col3:
            st.metric("Trend", monthly.get('trending', 'stable').capitalize())
    
    with tab3:
        streaks = ProductivityHistory.get_streaks()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Streak", f"{streaks.get('current_streak', 0)} days")
        with col2:
            st.metric("Best Streak", f"{streaks.get('best_streak', 0)} days")


def show_help():
    """Show help and information page"""
    st.markdown("### 💡 Help & Information")
    
    tab1, tab2, tab3 = st.tabs(["❓ About", "📖 How to Use", "⚙️ System Info"])
    
    with tab1:
        st.markdown("""
        ## About AI Productivity Tracker
        
        This is a Knowledge-Based Expert System designed to help you improve your daily productivity
        through personalized recommendations based on your work habits and lifestyle.
        
        ### Key Features:
        - **Rule-Based Inference Engine** with 31+ productivity rules
        - **Personalized Recommendations** based on your daily metrics
        - **Comprehensive Analysis** of productivity, focus, stress, and time management
        - **Historical Tracking** to monitor your progress
        - **Visual Analytics** with interactive charts
        
        ### Technology:
        - Python 3
        - Streamlit for frontend
        - Pandas for data analysis
        - Plotly for visualizations
        - No Machine Learning or external AI APIs
        """)
    
    with tab2:
        st.markdown("""
        ## How to Use
        
        1. **Complete Assessment**: Go to the Assessment page and fill in your daily metrics
        2. **Get Analysis**: Click "Generate Productivity Report" to get personalized insights
        3. **Review Recommendations**: Check your top recommendations and daily routine
        4. **Track Progress**: Visit the Analytics page to see your productivity trends
        5. **Repeat Daily**: Complete assessments daily to build a comprehensive profile
        
        ### Tips:
        - Be honest with your metrics for accurate recommendations
        - Focus on one or two areas at a time
        - Review your daily routine suggestions
        - Track your streaks for motivation
        """)
    
    with tab3:
        st.markdown("""
        ## System Information
        
        ### Knowledge Base:
        - **31 IF-THEN Rules** for productivity analysis
        - Rules cover: focus, stress, sleep, exercise, hydration, workload, goals
        - Rules have High/Medium confidence levels
        
        ### Analysis Metrics:
        - **Productivity Score** (0-100): Task completion (40%) + Focus (30%) + Sleep (15%) + Exercise (10%) + Stress (-5%)
        - **Focus Analysis**: Excellent, Good, Moderate, or Low
        - **Stress Analysis**: Low, Moderate, or High
        - **Time Management**: Efficiency calculation based on task completion
        - **Confidence Level**: High, Medium, or Low
        
        ### Data Storage:
        - All data saved locally in CSV format
        - No cloud storage or external APIs
        - Full privacy and offline capability
        """)


if __name__ == "__main__":
    main()
