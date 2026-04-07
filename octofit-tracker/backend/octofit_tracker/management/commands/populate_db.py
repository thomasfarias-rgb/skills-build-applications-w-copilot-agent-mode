from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', team=dc),
        ]

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Running', description='Cardio')

        # Activities
        Activity.objects.create(user=users[0], workout=w1, duration=30)
        Activity.objects.create(user=users[1], workout=w2, duration=45)
        Activity.objects.create(user=users[2], workout=w1, duration=20)
        Activity.objects.create(user=users[3], workout=w2, duration=50)

        # Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=80)
        Leaderboard.objects.create(user=users[2], points=90)
        Leaderboard.objects.create(user=users[3], points=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
