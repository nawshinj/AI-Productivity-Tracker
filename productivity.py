"""
Productivity calculation and analysis functions
"""

from inference_engine import InferenceEngine


class ProductivityAnalyzer:
    """Main productivity analysis class"""
    
    def __init__(self):
        self.engine = InferenceEngine()
    
    def analyze(self, user_data):
        """
        Analyze user productivity
        
        Args:
            user_data (dict): User input data
            
        Returns:
            dict: Analysis results
        """
        return self.engine.analyze_productivity(user_data)
    
    def get_quick_tips(self, user_data):
        """
        Get quick productivity tips
        
        Args:
            user_data (dict): User data
            
        Returns:
            list: Quick tips
        """
        tips = []
        
        # Focus tips
        if user_data.get('focus_level', 5) < 5:
            tips.append('🎯 Take a 15-minute break to refresh your focus')
        
        # Sleep tips
        if user_data.get('sleep_hours', 0) < 7:
            tips.append('😴 Prioritize 7-8 hours of sleep tonight')
        
        # Exercise tips
        if not user_data.get('exercise_today', False):
            tips.append('🏃 Get 30 minutes of exercise today')
        
        # Water tips
        if user_data.get('water_intake', 0) < 2:
            tips.append('💧 Increase your water intake to 2-3 liters')
        
        # Stress tips
        if user_data.get('stress_level') == 'High':
            tips.append('🧘 Practice meditation or deep breathing')
        
        # Task tips
        if user_data.get('completed_percentage', 0) < 50:
            tips.append('✅ Focus on completing your top 3 tasks first')
        
        return tips if tips else ['✨ You\'re doing great! Keep up the momentum!']
    
    def get_achievement_unlocked(self, analysis_result):
        """
        Check if any achievements are unlocked
        
        Args:
            analysis_result (dict): Analysis results
            
        Returns:
            list: Unlocked achievements
        """
        achievements = []
        score = analysis_result.get('productivity_score', 0)
        completion = analysis_result.get('completed_task_percentage', 0)
        focus = analysis_result.get('focus_score', 0)
        
        # Achievement conditions
        if score >= 90:
            achievements.append('🏆 Perfect Day - Scored 90+!')
        
        if completion >= 100:
            achievements.append('✅ All Tasks Complete - 100% Completion!')
        
        if focus >= 9:
            achievements.append('🎯 Laser Focus - 9/10 Focus Level!')
        
        if score >= 80 and completion >= 80 and focus >= 7:
            achievements.append('⭐ Triple Threat - Excellence Achieved!')
        
        if len(achievements) == 0:
            achievements.append('🌱 Keep Growing - You\'re Making Progress!')
        
        return achievements
