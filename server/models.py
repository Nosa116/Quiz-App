from django.db import models

class Questions(models.Model):
    question = models.TextField()
    correct_answer = models.TextField()
    incorrect_answer_0 = models.TextField()
    incorrect_answer_1 = models.TextField()
    incorrect_answer_2 = models.TextField()
    DIFFICULTY_CHOICES = [
        ('E', 'easy'),
        ('M', 'medium'),
        ('H', 'hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='E')
    CATEGORY_CHOICES =[
        ('GK', 'General Knowledge')
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='GK')
    TYPE_CHOICES = [
        ('MC', 'multiple'),
        ('TF', 'boolean'),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='MC')