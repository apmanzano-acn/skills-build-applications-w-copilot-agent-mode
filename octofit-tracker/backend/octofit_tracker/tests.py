from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Team, User, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Team.objects.count(), 1)

class UserTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team1')
    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': self.team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

class ActivityTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team2')
        self.user = User.objects.create(name='User2', email='user2@example.com', team=self.team)
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user': self.user.id, 'type': 'run', 'duration': 30, 'date': '2024-01-01'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Activity.objects.count(), 1)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Pushups', 'description': 'Do pushups', 'suggested_for': 'all'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Workout.objects.count(), 1)

class LeaderboardTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team3')
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'team': self.team.id, 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Leaderboard.objects.count(), 1)
