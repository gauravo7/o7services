from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Test(models.Model):
    question_text = models.CharField(max_length=200)
    qid = models.IntegerField()
    pub_date = models.DateTimeField('date published')

class Staff(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    c_name= models.CharField(max_length=255)

class Subcategory(models.Model):
    sid = models.AutoField(primary_key=True)
    cid = models.ForeignKey('category',on_delete=models.CASCADE)
    sname = models.CharField(max_length=255)