"""
History tracking for AI Productivity Tracker
"""

import pandas as pd
import os
from datetime import datetime, timedelta
from utils import get_productivity_history


class ProductivityHistory:
    """Track and analyze productivity history"""
    
    @staticmethod
    def get_daily_summary(days=7):
        """
        Get daily productivity summary
        
        Args:
            days (int): Number of days to retrieve
            
        Returns:
            list: Daily summaries
        """
        history = get_productivity_history()
        
        if not history:
            return []
        
        # Get last N days
        return history[-days:]
    
    @staticmethod
    def get_weekly_stats():
        """
        Get weekly productivity statistics
        
        Returns:
            dict: Weekly stats
        """
        history = get_productivity_history()
        
        if not history:
            return {
                'avg_score': 0,
                'best_score': 0,
                'worst_score': 0,
                'avg_completion': 0,
                'total_sessions': 0
            }
        
        # Get last 7 days
        recent = history[-7:]
        
        scores = [float(r.get('productivity_score', 0)) for r in recent]
        completions = [float(r.get('completed_percentage', 0)) for r in recent]
        
        return {
            'avg_score': sum(scores) / len(scores) if scores else 0,
            'best_score': max(scores) if scores else 0,
            'worst_score': min(scores) if scores else 0,
            'avg_completion': sum(completions) / len(completions) if completions else 0,
            'total_sessions': len(recent)
        }
    
    @staticmethod
    def get_monthly_stats():
        """
        Get monthly productivity statistics
        
        Returns:
            dict: Monthly stats
        """
        history = get_productivity_history()
        
        if not history:
            return {
                'avg_score': 0,
                'best_score': 0,
                'trending': 'stable',
                'total_sessions': 0
            }
        
        # Get last 30 days
        recent = history[-30:]
        
        scores = [float(r.get('productivity_score', 0)) for r in recent]
        
        # Calculate trend
        if len(scores) >= 2:
            first_half = sum(scores[:len(scores)//2]) / (len(scores)//2)
            second_half = sum(scores[len(scores)//2:]) / (len(scores) - len(scores)//2)
            
            if second_half > first_half * 1.05:
                trending = 'improving'
            elif second_half < first_half * 0.95:
                trending = 'declining'
            else:
                trending = 'stable'
        else:
            trending = 'stable'
        
        return {
            'avg_score': sum(scores) / len(scores) if scores else 0,
            'best_score': max(scores) if scores else 0,
            'trending': trending,
            'total_sessions': len(recent)
        }
    
    @staticmethod
    def get_streaks():
        """
        Get productivity streaks
        
        Returns:
            dict: Streak information
        """
        history = get_productivity_history()
        
        if not history:
            return {'current_streak': 0, 'best_streak': 0}
        
        # Count consecutive high productivity days (score >= 70)
        current_streak = 0
        best_streak = 0
        temp_streak = 0
        
        for record in history:
            score = float(record.get('productivity_score', 0))
            if score >= 70:
                temp_streak += 1
                current_streak = temp_streak
            else:
                if temp_streak > best_streak:
                    best_streak = temp_streak
                temp_streak = 0
        
        if temp_streak > best_streak:
            best_streak = temp_streak
        
        return {
            'current_streak': current_streak,
            'best_streak': best_streak
        }
    
    @staticmethod
    def get_improvement_areas(user_data, analysis_result):
        """
        Identify areas for improvement
        
        Args:
            user_data (dict): User data
            analysis_result (dict): Analysis results
            
        Returns:
            list: Improvement areas
        """
        areas = []
        
        # Check completion
        if analysis_result.get('completed_task_percentage', 0) < 70:
            areas.append({
                'area': 'Task Completion',
                'priority': 'High',
                'current': f"{analysis_result.get('completed_task_percentage', 0)}%",
                'target': '80%+'
            })
        
        # Check focus
        if user_data.get('focus_level', 5) < 6:
            areas.append({
                'area': 'Focus Level',
                'priority': 'High',
                'current': user_data.get('focus_level', 5),
                'target': '8/10'
            })
        
        # Check sleep
        if user_data.get('sleep_hours', 0) < 7:
            areas.append({
                'area': 'Sleep',
                'priority': 'High',
                'current': f"{user_data.get('sleep_hours', 0)}h",
                'target': '7-8h'
            })
        
        # Check stress
        if user_data.get('stress_level') == 'High':
            areas.append({
                'area': 'Stress Management',
                'priority': 'High',
                'current': 'High',
                'target': 'Low'
            })
        
        # Check exercise
        if not user_data.get('exercise_today', False):
            areas.append({
                'area': 'Physical Activity',
                'priority': 'Medium',
                'current': 'None',
                'target': '30+ mins'
            })
        
        # Check hydration
        if user_data.get('water_intake', 0) < 2:
            areas.append({
                'area': 'Hydration',
                'priority': 'Medium',
                'current': f"{user_data.get('water_intake', 0)}L",
                'target': '2-3L'
            })
        
        return areas
