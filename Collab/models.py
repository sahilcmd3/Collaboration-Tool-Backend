from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=50)

class Role(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

class File(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)