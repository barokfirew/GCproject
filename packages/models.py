from django.db import models
class Packages(models.Model):
    p_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    location = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    # staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    statusStartDate = models.DateField(null=True)
    statusEndDate = models.DateField(null=True)

    def __str__(self):
        return str(self.p_name)
    # id=models.IntegerField()