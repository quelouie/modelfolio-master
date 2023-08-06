from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable = False)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    profilePicture = models.ImageField()
    info = models.TextField(max_length=1000, null=True, blank=True)
    edited = models.DateTimeField(auto_now_add=True)
    linkedin = models.CharField(max_length=200,null=True, blank=True)
    instagram = models.CharField(max_length=200,null=True, blank=True)
    email = models.CharField(max_length=200,null=True, blank=True)
    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email