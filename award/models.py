from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 60)
    image = models.ImageField(upload_to = 'images/',blank=True)
    url = models.URLField(max_length = 40)
    description = models.TextField()
    screenshot = models.ImageField(upload_to = 'screenshots/',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/')
    bio = models.TextField()
    projects = models.ManyToManyField(Project,blank=True,related_name='profile_projects')
    contacts = models.CharField(max_length = 40)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username

class Vote(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
