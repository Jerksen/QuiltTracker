import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return (
            timezone.now() - datetime.timedelta(days=1)
            <= self.pub_date
            <= timezone.now()
        )

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


""" class Customer(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=70, unique=True)
    # status = models.IntegerField(min_value=0,max_value=1,default=1)


class Quilt(models.Model):
    quilter = models.ForeignKey(Customer, on_delete=models.PROTECT) # , limit_choices_to={'is_active': True})
    nickname = models.CharField(max_length=64)
    width = models.IntegerField()
    length = models.IntegerField()
 """
