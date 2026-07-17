"""
Knowledge Base for AI Productivity Tracker
Contains IF-THEN rules for productivity analysis
"""

class ProductivityRules:
    """Knowledge base with productivity rules"""
    
    def __init__(self):
        self.rules = []
        self._initialize_rules()
    
    def _initialize_rules(self):
        """Initialize all productivity rules"""
        
        # Rule 1: Low task completion with low focus
        self.rules.append({
            'id': 1,
            'name': 'Low Task Completion & Low Focus',
            'conditions': {
                'completed_percentage': ('<=', 70),
                'focus_level': ('<=', 4)
            },
            'recommendations': [
                '🎯 Reduce distractions - silence notifications',
                '⏱️ Use the Pomodoro Technique (25 min work, 5 min break)',
                '✂️ Break tasks into smaller, manageable parts',
                '📍 Set a single focus area for the day'
            ],
            'confidence': 'High'
        })
        
        # Rule 2: Insufficient sleep
        self.rules.append({
            'id': 2,
            'name': 'Insufficient Sleep',
            'conditions': {
                'sleep_hours': ('<', 6)
            },
            'recommendations': [
                '😴 Aim for 7-8 hours of sleep nightly',
                '🚫 Avoid working late into the night',
                '⏰ Maintain a consistent sleep schedule',
                '📱 Put devices away 30 minutes before bed'
            ],
            'confidence': 'High'
        })
        
        # Rule 3: High stress level
        self.rules.append({
            'id': 3,
            'name': 'High Stress Level',
            'conditions': {
                'stress_level': ('==', 'High')
            },
            'recommendations': [
                '☕ Take 5-minute break every hour',
                '🧘 Practice deep breathing (4-7-8 technique)',
                '❌ Avoid multitasking - focus on one task',
                '🚶 Go for a short walk to clear your mind'
            ],
            'confidence': 'High'
        })
        
        # Rule 4: High distraction level
        self.rules.append({
            'id': 4,
            'name': 'High Distraction Level',
            'conditions': {
                'distraction_level': ('==', 'High')
            },
            'recommendations': [
                '🔕 Turn off notifications completely',
                '📵 Enable Focus Mode on your device',
                '📱 Keep your phone in another room',
                '🤐 Work in a quiet environment'
            ],
            'confidence': 'High'
        })
        
        # Rule 5: Focus improvement needed with high screen time
        self.rules.append({
            'id': 5,
            'name': 'Screen Time Overload',
            'conditions': {
                'goal': ('==', 'Increase Focus'),
                'screen_time': ('>', 6)
            },
            'recommendations': [
                '📵 Limit social media to 30 minutes/day',
                '👀 Follow the 50/10 work-break rule',
                '👁️ Take a 20-second eye break every hour',
                '🌳 Look at something far away to relax eyes'
            ],
            'confidence': 'High'
        })
        
        # Rule 6: No exercise today
        self.rules.append({
            'id': 6,
            'name': 'No Exercise',
            'conditions': {
                'exercise_today': ('==', False)
            },
            'recommendations': [
                '🚶 Walk for 20-30 minutes during lunch',
                '🧘 Stretch for 5 minutes every hour',
                '🏃 Do light exercise to boost energy',
                '💪 Even a 10-minute walk helps'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 7: Excellent task completion
        self.rules.append({
            'id': 7,
            'name': 'Excellent Task Completion',
            'conditions': {
                'completed_percentage': ('>=', 90)
            },
            'recommendations': [
                '🎉 Great job! You\'re highly productive',
                '✨ Maintain this excellent momentum',
                '📈 Consider taking on more challenging tasks',
                '🏆 Share your productivity tips with others'
            ],
            'confidence': 'High'
        })
        
        # Rule 8: Very low focus
        self.rules.append({
            'id': 8,
            'name': 'Very Low Focus',
            'conditions': {
                'focus_level': ('<=', 3)
            },
            'recommendations': [
                '🎯 Your focus is critically low',
                '☕ Have a healthy snack and water',
                '🚶 Take a 15-minute walk outside',
                '🎧 Try focus music or white noise'
            ],
            'confidence': 'High'
        })
        
        # Rule 9: Low water intake
        self.rules.append({
            'id': 9,
            'name': 'Low Water Intake',
            'conditions': {
                'water_intake': ('<', 1.5)
            },
            'recommendations': [
                '💧 Drink at least 2-3 liters of water daily',
                '🚰 Set reminders to drink water every hour',
                '🥤 Keep a water bottle at your desk',
                '☕ Reduce caffeine and drink more water'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 10: Time management goal with low completion
        self.rules.append({
            'id': 10,
            'name': 'Time Management Needed',
            'conditions': {
                'goal': ('==', 'Improve Time Management'),
                'completed_percentage': ('<', 60)
            },
            'recommendations': [
                '📅 Use a time-blocking technique',
                '⏰ Allocate specific time for each task',
                '✅ Prioritize high-impact tasks first',
                '📋 Create a daily schedule the night before'
            ],
            'confidence': 'High'
        })
        
        # Rule 11: Procrastination goal with pending tasks
        self.rules.append({
            'id': 11,
            'name': 'Procrastination Pattern',
            'conditions': {
                'goal': ('==', 'Reduce Procrastination'),
                'pending_tasks': ('>', 5)
            },
            'recommendations': [
                '🚀 Start with the smallest task first',
                '⏱️ Use a timer - commit to just 5 minutes',
                '🎯 Break down big tasks into micro-tasks',
                '📝 Write down all tasks to reduce anxiety'
            ],
            'confidence': 'High'
        })
        
        # Rule 12: High workload with low focus
        self.rules.append({
            'id': 12,
            'name': 'High Workload Stress',
            'conditions': {
                'planned_tasks': ('>', 10),
                'focus_level': ('<', 5)
            },
            'recommendations': [
                '📊 Prioritize tasks - focus on top 3',
                '❌ It\'s okay to say no to new tasks',
                '💭 Reassess if you\'re overcommitted',
                '🗓️ Spread tasks across multiple days'
            ],
            'confidence': 'High'
        })
        
        # Rule 13: Night preference with high stress
        self.rules.append({
            'id': 13,
            'name': 'Night Work & Stress',
            'conditions': {
                'preferred_time': ('==', 'Night'),
                'stress_level': ('==', 'High')
            },
            'recommendations': [
                '🌙 Late-night work can increase stress',
                '🔄 Try shifting to earlier hours if possible',
                '😴 Prioritize sleep over late-night work',
                '⏰ Establish a consistent bedtime'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 14: Morning preference with low focus
        self.rules.append({
            'id': 14,
            'name': 'Morning Energy Boost Needed',
            'conditions': {
                'preferred_time': ('==', 'Morning'),
                'focus_level': ('<', 4),
                'sleep_hours': ('<', 7)
            },
            'recommendations': [
                '☀️ Get morning sunlight exposure',
                '🧘 Do a 10-minute morning meditation',
                '🍂 Eat a healthy breakfast',
                '💪 Morning exercise boosts focus'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 15: Extreme work hours
        self.rules.append({
            'id': 15,
            'name': 'Excessive Work Hours',
            'conditions': {
                'hours_worked': ('>', 10)
            },
            'recommendations': [
                '⚠️ Working over 10 hours is unsustainable',
                '🚫 Stop work and take a proper break',
                '📅 Redistribute work across more days',
                '🧘 Practice work-life balance'
            ],
            'confidence': 'High'
        })
        
        # Rule 16: Medium task completion
        self.rules.append({
            'id': 16,
            'name': 'Average Performance',
            'conditions': {
                'completed_percentage': ('>=', 60),
                'completed_percentage': ('<=', 80)
            },
            'recommendations': [
                '📈 You\'re doing well, keep improving!',
                '🎯 Focus on completing the remaining tasks',
                '💡 Identify what slowed you down today',
                '✨ Tomorrow aim for 85% completion'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 17: Good focus with poor completion
        self.rules.append({
            'id': 17,
            'name': 'Good Focus, Poor Task Completion',
            'conditions': {
                'focus_level': ('>=', 7),
                'completed_percentage': ('<', 50)
            },
            'recommendations': [
                '🤔 You focus well but complete few tasks',
                '📋 Re-evaluate task difficulty',
                '⏰ Tasks may take longer than estimated',
                '✂️ Break large tasks into smaller steps'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 18: Poor focus with good completion
        self.rules.append({
            'id': 18,
            'name': 'Poor Focus, Good Task Completion',
            'conditions': {
                'focus_level': ('<', 5),
                'completed_percentage': ('>=', 80)
            },
            'recommendations': [
                '💪 Despite low focus, you\'re completing tasks!',
                '📈 Imagine what you\'d achieve with better focus',
                '🎯 Focus on improving concentration',
                '🎉 You\'re naturally productive'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 19: Consistent performer
        self.rules.append({
            'id': 19,
            'name': 'Consistent Performer',
            'conditions': {
                'focus_level': ('>=', 7),
                'completed_percentage': ('>=', 80),
                'stress_level': ('==', 'Low')
            },
            'recommendations': [
                '⭐ You\'re an excellent performer!',
                '🏆 Your productivity system is working',
                '📚 Help others adopt your practices',
                '🚀 Consider tackling more ambitious goals'
            ],
            'confidence': 'High'
        })
        
        # Rule 20: Complete monotask
        self.rules.append({
            'id': 20,
            'name': 'Focus on One Task',
            'conditions': {
                'planned_tasks': ('>=', 5),
                'distraction_level': ('==', 'High')
            },
            'recommendations': [
                '🎯 Pick ONE task to complete first',
                '✅ Complete it 100% before starting another',
                '📍 This builds momentum and confidence',
                '🔄 Then move to the next task'
            ],
            'confidence': 'High'
        })
        
        # Rule 21: Burnout risk
        self.rules.append({
            'id': 21,
            'name': 'Burnout Risk Warning',
            'conditions': {
                'hours_worked': ('>', 9),
                'stress_level': ('==', 'High'),
                'exercise_today': ('==', False)
            },
            'recommendations': [
                '🚨 You\'re at risk of burnout!',
                '🛑 Stop working immediately',
                '🚶 Take a walk or exercise',
                '💆 Practice relaxation techniques today'
            ],
            'confidence': 'High'
        })
        
        # Rule 22: Mental clarity needed
        self.rules.append({
            'id': 22,
            'name': 'Low Mental Clarity',
            'conditions': {
                'focus_level': ('<', 4),
                'sleep_hours': ('<', 7),
                'water_intake': ('<', 2)
            },
            'recommendations': [
                '🧠 Your mental clarity is compromised',
                '💧 Drink water immediately',
                '☕ Have a light snack (nuts, fruit)',
                '😴 Get proper sleep tonight'
            ],
            'confidence': 'High'
        })
        
        # Rule 23: Afternoon slump
        self.rules.append({
            'id': 23,
            'name': 'Afternoon Productivity Dip',
            'conditions': {
                'preferred_time': ('==', 'Afternoon'),
                'focus_level': ('<=', 4)
            },
            'recommendations': [
                '☀️ Get some sunlight exposure',
                '🍎 Have a healthy snack',
                '💧 Drink water and walk around',
                '⏱️ Take a 20-minute power nap if possible'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 24: Task completion boost
        self.rules.append({
            'id': 24,
            'name': 'Task Completion Ready',
            'conditions': {
                'planned_tasks': ('<=', 3),
                'focus_level': ('>=', 8)
            },
            'recommendations': [
                '✨ Perfect conditions for task completion',
                '⚡ Start your work immediately',
                '🎯 Maintain this momentum',
                '🏆 You\'ll likely exceed your goals'
            ],
            'confidence': 'High'
        })
        
        # Rule 25: Stress recovery needed
        self.rules.append({
            'id': 25,
            'name': 'High Stress Recovery',
            'conditions': {
                'stress_level': ('==', 'High'),
                'hours_worked': ('>=', 8)
            },
            'recommendations': [
                '🧘 Do 10-minute meditation',
                '🎵 Listen to calming music',
                '🌿 Spend time in nature if possible',
                '🧖 Take a warm shower or bath'
            ],
            'confidence': 'High'
        })
        
        # Rule 26: Goal-specific - Complete More Tasks
        self.rules.append({
            'id': 26,
            'name': 'Complete More Tasks Strategy',
            'conditions': {
                'goal': ('==', 'Complete More Tasks'),
                'planned_tasks': ('>', 0)
            },
            'recommendations': [
                '📋 List all tasks with time estimates',
                '⏱️ Work on quick wins first (under 15 min)',
                '🔄 Build momentum with smaller tasks',
                '✅ Track each completion for motivation'
            ],
            'confidence': 'High'
        })
        
        # Rule 27: Maintain Productivity goal
        self.rules.append({
            'id': 27,
            'name': 'Maintain Current Productivity',
            'conditions': {
                'goal': ('==', 'Maintain Productivity'),
                'completed_percentage': ('>=', 75),
                'focus_level': ('>=', 6)
            },
            'recommendations': [
                '✨ Keep doing what you\'re doing!',
                '📊 Track your metrics weekly',
                '🎯 Set slightly higher goals',
                '🏅 Reward yourself for consistency'
            ],
            'confidence': 'High'
        })
        
        # Rule 28: Low task count with high focus
        self.rules.append({
            'id': 28,
            'name': 'Quality Over Quantity',
            'conditions': {
                'planned_tasks': ('<=', 3),
                'focus_level': ('>=', 7)
            },
            'recommendations': [
                '💎 Focus on high-quality work',
                '⚡ Depth is better than breadth',
                '🎯 Master these tasks completely',
                '📈 Quality builds reputation'
            ],
            'confidence': 'Medium'
        })
        
        # Rule 29: High pending tasks with low completion
        self.rules.append({
            'id': 29,
            'name': 'Backlog Buildup',
            'conditions': {
                'pending_tasks': ('>', 8),
                'completed_percentage': ('<', 50)
            },
            'recommendations': [
                '⚠️ You have a significant task backlog',
                '🗓️ Dedicate time tomorrow to clear it',
                '✂️ Break backlog into daily chunks',
                '🚀 Create a catch-up action plan'
            ],
            'confidence': 'High'
        })
        
        # Rule 30: Optimal productivity conditions
        self.rules.append({
            'id': 30,
            'name': 'Optimal Conditions',
            'conditions': {
                'focus_level': ('>=', 8),
                'stress_level': ('==', 'Low'),
                'sleep_hours': ('>=', 7),
                'distraction_level': ('==', 'Low')
            },
            'recommendations': [
                '🌟 All conditions are perfect for work!',
                '🚀 Tackle your most important task',
                '💪 This is your peak productivity window',
                '📈 Make the most of this time'
            ],
            'confidence': 'High'
        })
        
        # Rule 31: Energy management
        self.rules.append({
            'id': 31,
            'name': 'Energy Management',
            'conditions': {
                'sleep_hours': ('>=', 7),
                'exercise_today': ('==', True)
            },
            'recommendations': [
                '⚡ Your energy levels are optimal',
                '🏃 Exercise earlier in the day for best focus',
                '📈 You\'re set for peak performance',
                '💪 Maintain this healthy routine'
            ],
            'confidence': 'High'
        })

    def get_applicable_rules(self, user_data):
        """
        Get all applicable rules based on user data
        
        Args:
            user_data (dict): User input data
            
        Returns:
            list: List of applicable rules
        """
        applicable_rules = []
        
        for rule in self.rules:
            if self._check_conditions(rule['conditions'], user_data):
                applicable_rules.append(rule)
        
        return applicable_rules
    
    def _check_conditions(self, conditions, user_data):
        """
        Check if all conditions are met for a rule
        
        Args:
            conditions (dict): Rule conditions
            user_data (dict): User data
            
        Returns:
            bool: True if all conditions are met
        """
        for key, (operator, value) in conditions.items():
            user_value = user_data.get(key)
            
            if user_value is None:
                return False
            
            if operator == '==':
                if user_value != value:
                    return False
            elif operator == '>':
                if not (user_value > value):
                    return False
            elif operator == '<':
                if not (user_value < value):
                    return False
            elif operator == '>=':
                if not (user_value >= value):
                    return False
            elif operator == '<=':
                if not (user_value <= value):
                    return False
            elif operator == '!=':
                if user_value == value:
                    return False
        
        return True
    
    def get_rule_by_id(self, rule_id):
        """Get a rule by its ID"""
        for rule in self.rules:
            if rule['id'] == rule_id:
                return rule
        return None
