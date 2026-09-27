from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    experience_level = models.CharField(max_length=50)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.user.username

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=50)
    posted_date = models.DateField()
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    applied_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.user.username + " - " + self.job.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
