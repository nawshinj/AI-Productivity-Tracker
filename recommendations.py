"""
Recommendation system for AI Productivity Tracker
"""


class RecommendationSystem:
    """Generate personalized recommendations"""
    
    @staticmethod
    def get_time_management_recommendations(user_data):
        """
        Get time management recommendations
        
        Args:
            user_data (dict): User data
            
        Returns:
            list: Recommendations
        """
        recommendations = []
        
        # Analyze time management
        planned = user_data.get('planned_tasks', 0)
        completed = user_data.get('completed_tasks', 0)
        pending = user_data.get('pending_tasks', 0)
        
        if planned < 3:
            recommendations.append({
                'title': '📋 Plan More Tasks',
                'description': 'Consider planning 5-7 tasks daily for better structure',
                'action': 'Set specific, measurable goals for tomorrow'
            })
        
        if pending > completed:
            recommendations.append({
                'title': '⏰ Prioritize Your Workload',
                'description': 'You have more pending than completed tasks',
                'action': 'Use the Eisenhower Matrix to prioritize'
            })
        
        if completed == planned and planned > 0:
            recommendations.append({
                'title': '🎉 Perfect Completion',
                'description': 'You completed all planned tasks!',
                'action': 'Plan more ambitious tasks for tomorrow'
            })
        
        return recommendations
    
    @staticmethod
    def get_health_recommendations(user_data):
        """
        Get health and wellness recommendations
        
        Args:
            user_data (dict): User data
            
        Returns:
            list: Recommendations
        """
        recommendations = []
        
        # Sleep recommendations
        sleep = user_data.get('sleep_hours', 0)
        if sleep < 6:
            recommendations.append({
                'title': '😴 Critical Sleep Deficit',
                'description': f'You only slept {sleep} hours. Target 7-8 hours.',
                'action': 'Go to bed 30 minutes earlier tonight'
            })
        elif sleep < 7:
            recommendations.append({
                'title': '😴 Insufficient Sleep',
                'description': f'You slept {sleep} hours. Aim for 7-8 hours.',
                'action': 'Establish a consistent bedtime'
            })
        else:
            recommendations.append({
                'title': '😴 Good Sleep',
                'description': f'Excellent! You slept {sleep} hours.',
                'action': 'Maintain this sleep schedule'
            })
        
        # Exercise recommendations
        if not user_data.get('exercise_today', False):
            recommendations.append({
                'title': '🏃 No Exercise Today',
                'description': 'Physical activity boosts productivity',
                'action': 'Take a 20-30 minute walk today'
            })
        else:
            recommendations.append({
                'title': '🏃 Great Exercise',
                'description': 'You exercised today!',
                'action': 'Keep up this healthy habit'
            })
        
        # Water recommendations
        water = user_data.get('water_intake', 0)
        if water < 1.5:
            recommendations.append({
                'title': '💧 Increase Hydration',
                'description': f'You drank {water}L. Target 2-3L daily.',
                'action': 'Set hourly reminders to drink water'
            })
        else:
            recommendations.append({
                'title': '💧 Good Hydration',
                'description': f'Excellent hydration! You drank {water}L.',
                'action': 'Maintain consistent hydration'
            })
        
        return recommendations
    
    @staticmethod
    def get_focus_recommendations(user_data):
        """
        Get focus improvement recommendations
        
        Args:
            user_data (dict): User data
            
        Returns:
            list: Recommendations
        """
        recommendations = []
        
        focus = user_data.get('focus_level', 5)
        distraction = user_data.get('distraction_level', 'Low')
        screen_time = user_data.get('screen_time', 0)
        
        if focus < 4:
            recommendations.append({
                'title': '🎯 Critical Focus Loss',
                'description': 'Your focus is severely impaired',
                'action': 'Take a 30-minute break and reset'
            })
        elif focus < 6:
            recommendations.append({
                'title': '⚠️ Low Focus',
                'description': 'Your concentration needs improvement',
                'action': 'Use Pomodoro technique (25 min focus, 5 min break)'
            })
        
        if distraction == 'High':
            recommendations.append({
                'title': '📵 High Distraction',
                'description': 'You\'re easily distracted',
                'action': 'Turn off notifications and silence your phone'
            })
        
        if screen_time > 6:
            recommendations.append({
                'title': '👁️ Excessive Screen Time',
                'description': f'You\'ve been on screen for {screen_time} hours',
                'action': 'Take a 20-minute screen break with eye exercises'
            })
        
        if focus >= 8:
            recommendations.append({
                'title': '✨ Excellent Focus',
                'description': 'Your focus is outstanding',
                'action': 'Tackle your most challenging tasks now'
            })
        
        return recommendations
    
    @staticmethod
    def get_stress_management_recommendations(user_data):
        """
        Get stress management recommendations
        
        Args:
            user_data (dict): User data
            
        Returns:
            list: Recommendations
        """
        recommendations = []
        
        stress = user_data.get('stress_level', 'Low')
        
        if stress == 'High':
            recommendations.append({
                'title': '🚨 High Stress Alert',
                'description': 'Your stress levels are critically high',
                'action': 'Practice 10-minute meditation or breathing exercises'
            })
            recommendations.append({
                'title': '🧘 Stress Relief',
                'description': 'Implement immediate stress reduction',
                'action': 'Go for a walk or engage in a calming activity'
            })
        elif stress == 'Medium':
            recommendations.append({
                'title': '⚠️ Moderate Stress',
                'description': 'Your stress is building up',
                'action': 'Take regular breaks throughout the day'
            })
        else:
            recommendations.append({
                'title': '✨ Low Stress',
                'description': 'Great! Your stress levels are under control',
                'action': 'Maintain your current stress management practices'
            })
        
        return recommendations
