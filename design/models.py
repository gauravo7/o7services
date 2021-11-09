from django.db import models

# Create your models here.


class Test(models.Model):
    question_text = models.CharField(max_length=200)
    qid = models.IntegerField()
    pub_date = models.DateTimeField('date published')

class Staff(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)