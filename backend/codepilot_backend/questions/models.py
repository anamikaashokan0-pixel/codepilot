from django.db import models

# Create your models here.


class Question(models.Model):

    assessment = models.ForeignKey(Assessment,
                                   on_delete=models.CASCADE,
                                   related_name="questions")

    prompt = models.TextField()

    PROGRAMMING_LANGUAGE_CHOICES =  LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('java', 'Java'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('javascript', 'JavaScript'),
    ]
    programming_language = models.CharField(max_length=20,choices=PROGRAMMING_LANGUAGE_CHOICES)

    maximum_marks = models.PositiveIntegerField()

    display_order = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prompt