from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.models import Guest, Employee
class Announcement(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.sender)


class Event(models.Model):
    EVENT_TYPES = (
        ('Movie', 'Movie'),
        ('Theater', 'Theater'),
        ('Conference', 'Conference'),
        ('Concert', 'Concert'),
        ('Entertainment', 'Entertainment'),
        ('Live Music', 'Live Music'),
    )

    eventType = models.CharField(max_length=20, choices=EVENT_TYPES)
    location = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    explanation = models.TextField()

    def __str__(self):
        return str(self.eventType)


class EventAttendees(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    numberOfDependees = models.IntegerField(default=0)
    guest = models.ForeignKey(Guest,   null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + " " + str(self.guest)


class Bills(models.Model):
    guest = models.ForeignKey(Guest,   null=True, on_delete=models.CASCADE)
    totalAmount = models.FloatField()
    summary = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.guest) + " " + str(self.summary) + " " + str(self.totalAmount)


class FoodMenu(models.Model):
    FOOD_TYPES = (
        ('appetizer', 'appetizer'),
        ('entree', 'entree'),
        ('dessert', 'dessert'),
    )

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FOOD_TYPES)

    def __str__(self):
        return str(self.menuItems) + " " + str(self.startDate)


class Report(models.Model):
    date = models.DateField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return str(self.content) + " " + str(self.date)


class Storage(models.Model):
    ITEM_TYPES = (
        ('Kitchen', 'kitchen'),
        ('Cleaning', 'cleaning'),
        ('Electronic', 'Electronic'),
        ('Textile ', 'textile '),
        ('Other', 'other'),
    )
    itemName = models.CharField(max_length=100)
    itemType = models.CharField(max_length=20, choices=ITEM_TYPES)
    quantitiy = models.IntegerField()

    def __str__(self):
        return str(self.itemName)
class hotels(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=200)

    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)

    p_pic = models.ImageField(upload_to='hotel_pic/hotel profile/', null=True, blank=True)


    def __str__(self):
        return str(self.name)
