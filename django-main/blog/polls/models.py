from django.db import models
QUESTION_TYPES = (
    (1, 'otwarte'),
    (2, 'zamknięte')
)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    type = models.IntegerField(choices=QUESTION_TYPES, default=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Answer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)