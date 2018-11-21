from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project,Profile,Vote

# Create your tests here.
class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(user = self.user)
        self.profile.save()
        self.project = Project(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/project',screenshot='path/to/screenshot',user=self.user,profile=self.profile)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(id=1,profile_photo='path/to/photo',user = self.user,bio='test bio',contacts='test contact')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class VoteTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.profile = Profile(user = self.user)
        self.profile.save()
        self.project = Project(id=1, image = 'path/to/image',title='test',description='test caption',url='path/to/project',screenshot='path/to/screenshot',user=self.user,profile=self.profile)
        self.project.save()
        self.vote = Vote(id=1,project=self.project,design=10,usability=10,content=10,profile=self.profile)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.vote,Vote))
