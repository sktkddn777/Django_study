from datetime import datetime
from django.db import models
from django.db.models.query_utils import Q
from django.utils import timezone


class Question(models.Model):

    def __str__(self) -> str:
        return super().__str__()+self.question_text

    def was_published_recently(self):
        return self.pub_date <= timezone.now()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):

    def __str__(self) -> str:
        return super().__str__()+self.choice_text

    question = models.ForeignKey(Question,
    on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
