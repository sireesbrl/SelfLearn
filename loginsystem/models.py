from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    students = models.ManyToManyField(User, blank=True, null=True, name="students")

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")
    courses = models.ManyToManyField(Course, blank=True, name="courses")

    def __str__(self):
        return f"{self.user.username}"