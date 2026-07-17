"""
Chart generation for AI Productivity Tracker
"""

import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
from utils import get_productivity_history


def create_productivity_gauge(score):
    """
    Create a gauge chart for productivity score
    
    Args:
        score (int): Productivity score (0-100)
        
    Returns:
        plotly.graph_objects.Figure: Gauge chart
    """
    fig = go.Figure(data=[go.Indicator(
        mode="gauge+number+delta",
        value=score,
        title={'text': "Productivity Score"},
        delta={'reference': 80},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 40], 'color': "lightgray", 'label': "Needs Improvement"},
                {'range': [40, 60], 'color': "lightyellow", 'label': "Average"},
                {'range': [60, 80], 'color': "lightgreen", 'label': "Good"},
                {'range': [80, 100], 'color': "lightblue", 'label': "Excellent"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    )])
    fig.update_layout(height=400, margin=dict(l=10, r=10, t=50, b=10))
    return fig


def create_focus_chart(focus_level, target=8):
    """
    Create a focus level chart
    
    Args:
        focus_level (int): Current focus level (1-10)
        target (int): Target focus level
        
    Returns:
        plotly.graph_objects.Figure: Bar chart
    """
    fig = go.Figure(data=[
        go.Bar(name='Current', x=['Focus Level'], y=[focus_level], marker_color='indianred'),
        go.Bar(name='Target', x=['Focus Level'], y=[target], marker_color='lightgreen')
    ])
    fig.update_layout(
        title="Focus Level vs Target",
        barmode='group',
        height=300,
        showlegend=True,
        yaxis_range=[0, 10]
    )
    return fig


def create_task_completion_pie(completed, pending, planned):
    """
    Create a pie chart for task completion
    
    Args:
        completed (int): Completed tasks
        pending (int): Pending tasks
        planned (int): Planned tasks
        
    Returns:
        plotly.graph_objects.Figure: Pie chart
    """
    fig = go.Figure(data=[
        go.Pie(
            labels=['Completed', 'Pending'],
            values=[completed, pending],
            marker=dict(colors=['#2ecc71', '#e74c3c'])
        )
    ])
    fig.update_layout(
        title=f"Task Completion (Planned: {planned})",
        height=300
    )
    return fig


def create_weekly_trend():
    """
    Create a weekly productivity trend chart
    
    Returns:
        plotly.graph_objects.Figure: Line chart
    """
    history = get_productivity_history()
    
    if not history:
        # Create empty chart
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=[], mode='lines+markers', name='Productivity'))
        fig.update_layout(title="Weekly Productivity Trend", height=300)
        return fig
    
    # Get last 7 days
    recent_history = history[-7:]
    
    dates = [record.get('timestamp', '').split(' ')[0] for record in recent_history]
    scores = [float(record.get('productivity_score', 0)) for record in recent_history]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=scores,
        mode='lines+markers',
        name='Productivity Score',
        line=dict(color='#3498db', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title="Weekly Productivity Trend",
        xaxis_title="Date",
        yaxis_title="Productivity Score",
        height=300,
        hovermode='x unified'
    )
    
    return fig


def create_stress_level_chart(current_stress, stress_history=None):
    """
    Create a stress level visualization
    
    Args:
        current_stress (str): Current stress level (Low/Medium/High)
        stress_history (list): Historical stress levels
        
    Returns:
        plotly.graph_objects.Figure: Chart
    """
    stress_values = {'Low': 1, 'Medium': 2, 'High': 3}
    stress_colors = {'Low': '#2ecc71', 'Medium': '#f39c12', 'High': '#e74c3c'}
    
    current_value = stress_values.get(current_stress, 2)
    color = stress_colors.get(current_stress, '#3498db')
    
    fig = go.Figure(data=[go.Indicator(
        mode="gauge+number",
        value=current_value,
        title={'text': "Stress Level"},
        gauge={
            'axis': {'range': [0, 3]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 1], 'color': "lightgreen", 'label': "Low"},
                {'range': [1, 2], 'color': "lightyellow", 'label': "Medium"},
                {'range': [2, 3], 'color': "lightcoral", 'label': "High"}
            ]
        },
        tickvals=[0, 1, 2, 3],
        ticktext=['None', 'Low', 'Medium', 'High']
    )])
    fig.update_layout(height=300, margin=dict(l=10, r=10, t=50, b=10))
    return fig


def create_health_metrics(sleep_hours, water_intake, exercise):
    """
    Create a health metrics radar chart
    
    Args:
        sleep_hours (float): Hours of sleep
        water_intake (float): Liters of water
        exercise (bool): Exercise today
        
    Returns:
        plotly.graph_objects.Figure: Radar chart
    """
    # Normalize values to 0-10 scale
    sleep_score = min(10, (sleep_hours / 8) * 10)
    water_score = min(10, (water_intake / 3) * 10)
    exercise_score = 10 if exercise else 3
    
    fig = go.Figure(data=go.Scatterpolar(
        r=[sleep_score, water_score, exercise_score, 7],
        theta=['Sleep', 'Hydration', 'Exercise', 'Balance'],
        fill='toself',
        name='Health Score'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        title="Health & Wellness Metrics",
        height=400
    )
    
    return fig
