from django.db import models
from loginsystem.models import Course, User

class Chapters(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed_by = models.ManyToManyField(User, blank=True, null=True)
    path = models.CharField(max_length=100)

    def __str__(self):
        return f"Chapter: {self.name} from {self.course}"