from django.db import models
from django.utils import timezone

from accounts.models import Guest
from hotel.models import hotels

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = (
        ('King', 'King'),
        ('Luxury', 'Luxury'),
        ('Normal', 'Normal'),
        ('Economic', 'Economic'),

    )
    room_id = models.IntegerField(primary_key=True)
    capacity = models.SmallIntegerField()
    numberOfBeds = models.SmallIntegerField()
    roomType = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.FloatField()
    hotel = models.ForeignKey(hotels, on_delete=models.CASCADE)
    statusStartDate = models.DateField(null=True)
    statusEndDate = models.DateField(null=True)

    def __str__(self):
        return str(self.number)



class Booking(models.Model):
    roomNumber = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, null=True, on_delete=models.CASCADE)
    dateOfReservation = models.DateField(default=timezone.now)
    startDate = models.DateField()
    endDate = models.DateField()
    def numOfBooking(self):
        return Booking.objects.filter(guest=self).count()

    def numOfDays(self):
        totalDay = 0
        bookings = Booking.objects.filter(guest=self)
        for b in bookings:
            day = b.endDate - b.startDate
            totalDay += int(day.days)

        return totalDay

    def numOfLastBookingDays(self):
        try:
            return int((Booking.objects.filter(guest=self).last().endDate - Booking.objects.filter(guest=self).last().startDate).days)
        except:
            return 0

    def currentRoom(self):
        booking = Booking.objects.filter(guest=self).last()
        return booking.roomNumber




    def __str__(self):
        return str(self.roomNumber) + " " + str(self.guest)


class Dependees(models.Model):
    booking = models.ForeignKey(Booking,   null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def str(self):
        return str(self.booking) + " " + str(self.name)
    def numOfDep(self):
        return Dependees.objects.filter(booking=self).count()


class Refund(models.Model):
    guest = models.ForeignKey(Guest,   null=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Booking, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return str(self.guest)


class RoomServices(models.Model):
    SERVICES_TYPES = (
        ('Food', 'Food'),
        ('Cleaning', 'Cleaning'),
        ('Technical', 'Technical'),
    )

    curBooking = models.ForeignKey(
        Booking,   null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    createdDate = models.DateField(default=timezone.now)
    servicesType = models.CharField(max_length=20, choices=SERVICES_TYPES)
    price = models.FloatField()

    def str(self):
        return str(self.curBooking) + " " + str(self.room) + " " + str(self.servicesType)
