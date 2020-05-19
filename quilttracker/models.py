from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime

# Create your models here.
class Customer(models.Model):
    # statuses
    ST_ACTIVE = "active"
    ST_ARCHIVED = "archived"
    STATUS_CHOICES = (
        (ST_ACTIVE, "Active"),
        (ST_ARCHIVED, "Archived"),
    )
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ST_ACTIVE)

    def __str__(self):
        return "{} {} ({})".format(self.firstname, self.lastname, self.email)

    createdOn = models.DateTimeField()
    modifiedOn = models.DateTimeField()
    def save(self, *args, **kwargs):
        """Update Time stamps on save"""
        if not self.id:
            self.createdOn = timezone.now()
        
        self.modifiedOn = timezone.now()
        return super(Customer, self).save(*args, **kwargs)


class Quilt(models.Model):
    # statuses
    ST_FORM_SUBMITTED = "form submitted"
    ST_RECEIVED = "received"
    ST_RETURNED = "returned"
    ST_CLOSED = "closed"

    STATUS_CHOICES = (
        (ST_FORM_SUBMITTED, "Form Submitted"),
        (ST_RECEIVED, "Received"),
        (ST_RETURNED, "Returned"),
        (ST_CLOSED, "Closed"),
    )

    nickname = models.CharField(max_length=64)
    width = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )
    length = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(144)]
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=ST_FORM_SUBMITTED
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({}x{})".format(self.nickname, self.width, self.length)

    createdOn = models.DateTimeField()
    modifiedOn = models.DateTimeField()
    def save(self, *args, **kwargs):
        """Update Time stamps on save"""
        if not self.id:
            self.createdOn = timezone.now()
        
        self.modifiedOn = timezone.now()
        return super(Quilt, self).save(*args, **kwargs)
    
    def get_area(self):
        return self.width * self.length
    
    def get_linear_length(self):
        return min(self.width, self.length)

class Batting(models.Model):
    name = models.CharField(max_length=64, unique=True)
    createdOn = models.DateTimeField()
    modifiedOn = models.DateTimeField()
    def save(self, *args, **kwargs):
        """Update Time stamps on save"""
        if not self.id:
            self.createdOn = timezone.now()
        
        self.modifiedOn = timezone.now()
        return super(Batting, self).save(*args, **kwargs)


class LongArmRates(models.Model):
    price = models.DecimalField(verbose_name="price per square inch",
        validators=[MinValueValidator(0.001), MaxValueValidator(.1)])

class BattingPrice(models.Model):
    batting = models.ForeignKey(to=Batting, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="price per linear inch",
        validators=[MinValueValidator(0), MaxValueValidator(2))
    applicable_date = models.DateTimeField()
    
    createdOn = models.DateTimeField()
    modifiedOn = models.DateTimeField()
    def save(self, *args, **kwargs):
        """Update Time stamps on save"""
        if not self.id:
            self.createdOn = timezone.now()
        
        self.modifiedOn = timezone.now()
        return super(BattingPrice, self).save(*args, **kwargs)
    
    def get_price_for_date(self, name, date):
        return BattingPrice.objects.filter(batting__name=name).
        filter(applicable_date__lte=date)[0].price