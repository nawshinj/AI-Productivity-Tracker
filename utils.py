"""
Utility functions for AI Productivity Tracker
"""

import os
import csv
from datetime import datetime


def ensure_data_directory():
    """Ensure data directory exists"""
    if not os.path.exists('data'):
        os.makedirs('data')


def ensure_reports_directory():
    """Ensure reports directory exists"""
    if not os.path.exists('reports'):
        os.makedirs('reports')


def save_productivity_report(user_data, analysis_result):
    """
    Save productivity report to CSV
    
    Args:
        user_data (dict): User input data
        analysis_result (dict): Analysis results
        
    Returns:
        str: File path
    """
    ensure_data_directory()
    
    filename = f'data/productivity_history.csv'
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow([
                'timestamp',
                'name',
                'productivity_score',
                'completed_percentage',
                'focus_level',
                'stress_level',
                'sleep_hours',
                'exercise_today'
            ])
        
        # Write data row
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            user_data.get('name', 'Unknown'),
            analysis_result.get('productivity_score', 0),
            user_data.get('completed_percentage', 0),
            user_data.get('focus_level', 0),
            user_data.get('stress_level', 'Unknown'),
            user_data.get('sleep_hours', 0),
            user_data.get('exercise_today', False)
        ])
    
    return filename


def get_productivity_history():
    """
    Get productivity history from CSV
    
    Returns:
        list: List of historical records
    """
    ensure_data_directory()
    
    filename = 'data/productivity_history.csv'
    if not os.path.exists(filename):
        return []
    
    history = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            history.append(row)
    
    return history


def get_weekly_productivity_stats():
    """
    Get weekly productivity statistics
    
    Returns:
        dict: Weekly stats
    """
    history = get_productivity_history()
    
    if not history:
        return {
            'average_score': 0,
            'best_day': 0,
            'worst_day': 0,
            'total_sessions': 0
        }
    
    scores = [float(record.get('productivity_score', 0)) for record in history[-7:]]
    
    return {
        'average_score': sum(scores) / len(scores) if scores else 0,
        'best_day': max(scores) if scores else 0,
        'worst_day': min(scores) if scores else 0,
        'total_sessions': len(scores)
    }


def format_time(hours):
    """Format hours to HH:MM format"""
    h = int(hours)
    m = int((hours - h) * 60)
    return f"{h}h {m}m"


def get_productivity_category(score):
    """
    Get productivity category based on score
    
    Args:
        score (int): Productivity score
        
    Returns:
        str: Category
    """
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 50:
        return "Average"
    elif score >= 40:
        return "Below Average"
    else:
        return "Needs Improvement"
