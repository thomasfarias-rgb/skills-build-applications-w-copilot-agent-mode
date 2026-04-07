from django.test import TestCase
from .models import User, Team, Workout, Activity, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_workout(self):
        self.assertEqual(self.activity.workout.name, 'Test Workout')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
