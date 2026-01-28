from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True)  # e.g. "Backend Developer"
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile/')  # stores image in MEDIA folder

    def __str__(self):
        return self.name + " " + self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title + " " + self.description

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    desc = models.TextField() 


class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title