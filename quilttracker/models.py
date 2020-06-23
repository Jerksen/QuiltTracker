from django.conf import settings
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_active_customers():
        # TODO: sort by names
        return Customer.objects.all()

    def is_active(self):
        return True


class Quilt(models.Model):
    customer = models.ForeignKey(Customer, models.PROTECT)
    nickname = models.CharField(max_length=64)
