from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Questions

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email'] 

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['id', 'type', 'difficulty', 'category', 'question', 'correct_answer', 'incorrect_answer_0', 'incorrect_answer_1', 'incorrect_answer_2']
