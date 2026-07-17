"""
Rule-Based Inference Engine for AI Productivity Tracker
Evaluates user inputs against knowledge base and generates recommendations
"""

from knowledge_base import ProductivityRules


class InferenceEngine:
    """Rule-based inference engine for productivity analysis"""
    
    def __init__(self):
        self.knowledge_base = ProductivityRules()
    
    def analyze_productivity(self, user_data):
        """
        Analyze user productivity based on input data
        
        Args:
            user_data (dict): User input data
            
        Returns:
            dict: Analysis results with score, recommendations, and insights
        """
        # Get applicable rules
        applicable_rules = self.knowledge_base.get_applicable_rules(user_data)
        
        # Calculate productivity score
        productivity_score = self._calculate_productivity_score(user_data)
        
        # Determine productivity level
        productivity_level = self._get_productivity_level(productivity_score)
        
        # Generate recommendations from applicable rules
        all_recommendations = self._generate_recommendations(applicable_rules)
        
        # Get top recommendations
        top_recommendations = self._prioritize_recommendations(all_recommendations, applicable_rules)
        
        # Calculate confidence level
        confidence_level = self._calculate_confidence(applicable_rules)
        
        # Generate insights
        insights = self._generate_insights(user_data, applicable_rules)
        
        # Generate daily routine
        daily_routine = self._generate_daily_routine(user_data)
        
        # Get motivation quote
        motivation_quote = self._get_motivation_quote(productivity_level, user_data)
        
        return {
            'productivity_score': productivity_score,
            'productivity_level': productivity_level,
            'completed_task_percentage': user_data.get('completed_percentage', 0),
            'applicable_rules': len(applicable_rules),
            'recommendations': top_recommendations,
            'all_recommendations': all_recommendations,
            'focus_analysis': self._analyze_focus(user_data),
            'stress_analysis': self._analyze_stress(user_data),
            'time_management': self._analyze_time_management(user_data),
            'task_priority': self._suggest_task_priority(user_data),
            'break_recommendations': self._generate_break_recommendations(user_data),
            'daily_routine': daily_routine,
            'motivation_quote': motivation_quote,
            'confidence_level': confidence_level,
            'insights': insights,
            'focus_score': user_data.get('focus_level', 5),
            'badge': self._assign_badge(productivity_level, user_data)
        }
    
    def _calculate_productivity_score(self, user_data):
        """
        Calculate overall productivity score (0-100)
        
        Args:
            user_data (dict): User data
            
        Returns:
            int: Productivity score
        """
        score = 0
        
        # Task completion (40%)
        completion = user_data.get('completed_percentage', 0)
        score += (completion * 0.40)
        
        # Focus level (30%)
        focus = user_data.get('focus_level', 5)
        score += (focus * 3)  # Convert 0-10 to 0-30
        
        # Sleep quality (15%)
        sleep = user_data.get('sleep_hours', 0)
        if sleep >= 7:
            score += 15
        elif sleep >= 6:
            score += 10
        elif sleep >= 5:
            score += 5
        
        # Exercise (10%)
        exercise = 10 if user_data.get('exercise_today', False) else 0
        score += exercise
        
        # Stress reduction (-5%)
        if user_data.get('stress_level') == 'High':
            score -= 5
        elif user_data.get('stress_level') == 'Medium':
            score -= 2
        
        return min(100, max(0, int(score)))
    
    def _get_productivity_level(self, score):
        """
        Determine productivity level based on score
        
        Args:
            score (int): Productivity score
            
        Returns:
            str: Productivity level
        """
        if score >= 85:
            return "🌟 Excellent"
        elif score >= 70:
            return "✨ Very Good"
        elif score >= 60:
            return "👍 Good"
        elif score >= 50:
            return "👌 Average"
        elif score >= 40:
            return "📈 Below Average"
        else:
            return "⚠️ Needs Improvement"
    
    def _generate_recommendations(self, applicable_rules):
        """
        Generate recommendations from applicable rules
        
        Args:
            applicable_rules (list): List of applicable rules
            
        Returns:
            list: All recommendations
        """
        all_recommendations = []
        seen = set()
        
        for rule in applicable_rules:
            for rec in rule['recommendations']:
                if rec not in seen:
                    all_recommendations.append(rec)
                    seen.add(rec)
        
        return all_recommendations
    
    def _prioritize_recommendations(self, recommendations, applicable_rules):
        """
        Prioritize recommendations based on rule confidence
        
        Args:
            recommendations (list): All recommendations
            applicable_rules (list): Applicable rules with confidence levels
            
        Returns:
            list: Top 5 prioritized recommendations
        """
        # Create a mapping of recommendations to their highest confidence
        rec_confidence = {}
        for rule in applicable_rules:
            confidence_score = 2 if rule['confidence'] == 'High' else 1
            for rec in rule['recommendations']:
                if rec not in rec_confidence:
                    rec_confidence[rec] = 0
                rec_confidence[rec] += confidence_score
        
        # Sort by confidence score
        sorted_recs = sorted(rec_confidence.items(), key=lambda x: x[1], reverse=True)
        
        # Return top 5
        return [rec[0] for rec in sorted_recs[:5]]
    
    def _calculate_confidence(self, applicable_rules):
        """
        Calculate overall confidence level
        
        Args:
            applicable_rules (list): Applicable rules
            
        Returns:
            str: Confidence level
        """
        if not applicable_rules:
            return "Low"
        
        high_confidence_rules = sum(1 for r in applicable_rules if r['confidence'] == 'High')
        
        if high_confidence_rules >= 3:
            return "High"
        elif high_confidence_rules >= 1:
            return "Medium"
        else:
            return "Low"
    
    def _analyze_focus(self, user_data):
        """Generate focus analysis"""
        focus_level = user_data.get('focus_level', 5)
        
        if focus_level >= 8:
            return {
                'level': '🎯 Excellent Focus',
                'message': 'Your focus is outstanding. Utilize this for your most challenging tasks.',
                'tips': [
                    'Tackle complex problems now',
                    'Deep work is at its peak',
                    'Minimize any distractions'
                ]
            }
        elif focus_level >= 6:
            return {
                'level': '✨ Good Focus',
                'message': 'You have solid focus. Work on important tasks.',
                'tips': [
                    'Manage medium complexity tasks',
                    'Maintain your current environment',
                    'Take short breaks as needed'
                ]
            }
        elif focus_level >= 4:
            return {
                'level': '⚠️ Moderate Focus',
                'message': 'Your focus needs attention. Consider taking a break.',
                'tips': [
                    'Work on routine tasks',
                    'Reduce decision-making',
                    'Take a 15-minute break'
                ]
            }
        else:
            return {
                'level': '🚨 Low Focus',
                'message': 'Your focus is significantly impaired. Stop and refresh.',
                'tips': [
                    'Take a 30-minute break',
                    'Go for a walk',
                    'Return with fresh perspective'
                ]
            }
    
    def _analyze_stress(self, user_data):
        """Generate stress analysis"""
        stress_level = user_data.get('stress_level', 'Low')
        
        if stress_level == 'High':
            return {
                'level': '🚨 High Stress',
                'message': 'You\'re experiencing high stress. Prioritize relaxation.',
                'coping_strategies': [
                    'Deep breathing exercises',
                    'Progressive muscle relaxation',
                    'Short meditation session',
                    'Brief walk outside'
                ]
            }
        elif stress_level == 'Medium':
            return {
                'level': '⚠️ Moderate Stress',
                'message': 'You\'re under moderate stress. Manage it with breaks.',
                'coping_strategies': [
                    'Regular breaks (5 min every hour)',
                    'Light exercise',
                    'Hydration and healthy snacks',
                    'Social interaction'
                ]
            }
        else:
            return {
                'level': '✨ Low Stress',
                'message': 'Great! Your stress levels are under control.',
                'coping_strategies': [
                    'Maintain current habits',
                    'Continue your routine',
                    'Stay consistent'
                ]
            }
    
    def _analyze_time_management(self, user_data):
        """Generate time management analysis"""
        planned = user_data.get('planned_tasks', 0)
        completed = user_data.get('completed_tasks', 0)
        pending = user_data.get('pending_tasks', 0)
        
        return {
            'planned': planned,
            'completed': completed,
            'pending': pending,
            'efficiency': self._calculate_efficiency(planned, completed),
            'suggestions': self._get_time_management_suggestions(planned, completed, pending)
        }
    
    def _calculate_efficiency(self, planned, completed):
        """Calculate time management efficiency"""
        if planned == 0:
            return 0
        return min(100, int((completed / planned) * 100))
    
    def _get_time_management_suggestions(self, planned, completed, pending):
        """Get time management suggestions"""
        suggestions = []
        
        if pending > completed:
            suggestions.append('📋 More tasks pending than completed. Prioritize!')
        if planned < 3:
            suggestions.append('📈 Consider planning more tasks for better productivity.')
        if completed == 0:
            suggestions.append('🚀 Start your first task immediately!')
        
        return suggestions if suggestions else ['✅ Your time management looks good!']
    
    def _suggest_task_priority(self, user_data):
        """Suggest task priority strategy"""
        return {
            'strategy': 'Eisenhower Matrix (Urgent-Important)',
            'priority_order': [
                '1️⃣ Urgent & Important - Do First',
                '2️⃣ Important but Not Urgent - Schedule',
                '3️⃣ Urgent but Not Important - Delegate',
                '4️⃣ Neither - Eliminate'
            ],
            'quick_tip': 'Start with 1-2 high-priority tasks for maximum impact.'
        }
    
    def _generate_break_recommendations(self, user_data):
        """Generate break recommendations"""
        hours_worked = user_data.get('hours_worked', 0)
        
        if hours_worked >= 8:
            return {
                'frequency': '⏰ Every 50 minutes',
                'duration': '10 minutes',
                'activities': [
                    'Walk around',
                    'Stretch muscles',
                    'Hydrate',
                    'Eye rest (look away from screen)',
                    'Brief meditation'
                ]
            }
        else:
            return {
                'frequency': '⏰ Every 60 minutes',
                'duration': '5-10 minutes',
                'activities': [
                    'Stretch',
                    'Brief walk',
                    'Grab water',
                    'Eye exercises',
                    'Mental break'
                ]
            }
    
    def _generate_daily_routine(self, user_data):
        """Generate optimized daily routine"""
        preferred_time = user_data.get('preferred_time', 'Morning')
        
        routines = {
            'Morning': [
                '6:00-6:30 🛏️ Wake up & Morning routine',
                '6:30-7:00 🧘 Meditation/Exercise',
                '7:00-7:30 🍽️ Breakfast',
                '7:30-10:30 🎯 Peak focus - Most important tasks',
                '10:30-10:40 ☕ Break',
                '10:40-12:30 📋 Medium priority tasks',
                '12:30-1:00 🍽️ Lunch',
                '1:00-3:00 📊 Administrative tasks/Meetings',
                '3:00-3:10 🚶 Break',
                '3:10-4:30 📈 Continue important work',
                '4:30-6:00 📱 Emails/Low priority tasks',
                '6:00+ 🌙 Evening/Personal time'
            ],
            'Afternoon': [
                '12:00-1:00 🍽️ Lunch & rest',
                '1:00-2:00 📊 Administrative tasks',
                '2:00-4:00 🎯 Peak focus - Important tasks',
                '4:00-4:10 ☕ Break',
                '4:10-6:00 📋 Continued focus work',
                '6:00+ 🌙 Evening tasks'
            ],
            'Evening': [
                '6:00-7:00 📊 Review & planning',
                '7:00-8:00 🎯 Focused work session',
                '8:00-8:30 ☕ Break',
                '8:30-10:00 📋 Continued work',
                '10:00-11:00 🧘 Wind down',
                '11:00+ 😴 Sleep'
            ],
            'Night': [
                '8:00-9:00 📋 Evening work start',
                '9:00-10:30 🎯 Focused work',
                '10:30-10:40 ☕ Break',
                '10:40-12:00 📊 Continued work',
                '12:00+ 😴 Sleep (⚠️ Get 7-8 hours!)'
            ]
        }
        
        return routines.get(preferred_time, routines['Morning'])
    
    def _get_motivation_quote(self, productivity_level, user_data):
        """Get motivational quote based on productivity"""
        quotes_by_level = {
            '🌟 Excellent': [
                '🏆 You\'re crushing it! Keep up this momentum!',
                '⭐ Excellence is a habit, not an act.',
                '🚀 You\'re in the zone - make the most of it!'
            ],
            '✨ Very Good': [
                '👏 Great work today! You\'re on track.',
                '📈 Keep pushing! You\'re close to peak performance.',
                '✨ Small improvements lead to big results!'
            ],
            '👍 Good': [
                '💪 Good effort! You can do better tomorrow.',
                '📊 Consistency is key to success.',
                '🎯 You\'re making progress!'
            ],
            '👌 Average': [
                '🔄 Every day is a chance to improve.',
                '📈 Focus on one thing - master it.',
                '🚀 Today is just the beginning!'
            ],
            '📈 Below Average': [
                '💭 Tomorrow is a new opportunity!',
                '🌱 Growth starts with small steps.',
                '✨ You\'ve got this! One task at a time.'
            ],
            '⚠️ Needs Improvement': [
                '🆘 It\'s okay to have tough days. Rest and recover.',
                '🔄 Reset your focus and try again tomorrow.',
                '💪 One small win can change everything!'
            ]
        }
        
        quotes = quotes_by_level.get(productivity_level, ['Keep going!'])
        return quotes[0]
    
    def _assign_badge(self, productivity_level, user_data):
        """Assign achievement badge"""
        completion = user_data.get('completed_percentage', 0)
        focus = user_data.get('focus_level', 5)
        
        if completion >= 90 and focus >= 8:
            return '🏆 Productivity Master'
        elif completion >= 80 and focus >= 7:
            return '⭐ High Achiever'
        elif completion >= 70 and focus >= 6:
            return '👏 Consistent Performer'
        elif completion >= 60:
            return '📈 Rising Star'
        else:
            return '🌱 Learning'
    
    def _generate_insights(self, user_data, applicable_rules):
        """Generate actionable insights"""
        insights = []
        
        if user_data.get('completed_percentage', 0) > 80:
            insights.append('✅ Excellent task completion! Maintain this pace.')
        
        if user_data.get('focus_level', 5) < 4:
            insights.append('⚠️ Low focus detected. Take a break and refresh.')
        
        if user_data.get('sleep_hours', 0) < 6:
            insights.append('😴 Insufficient sleep. Prioritize rest tonight.')
        
        if len(applicable_rules) > 5:
            insights.append('🎯 Multiple concerns detected. Focus on top 3 actions.')
        
        if user_data.get('stress_level') == 'High':
            insights.append('💆 High stress detected. Practice relaxation techniques.')
        
        return insights if insights else ['✨ You\'re doing great! Keep up the good work!']
