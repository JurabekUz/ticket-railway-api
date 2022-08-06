from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from config.tasks import up_date_seats_count
from trains.models import Voyage, City, Wagon

User = get_user_model()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport = models.CharField(max_length=20)

    voyage = models.ForeignKey(Voyage,on_delete=models.CASCADE, related_name='user_ticket')
    from_city = models.CharField(max_length=50)
    to_city = models.CharField(max_length=50)

    #wagon= models.ForeignKey(Wagon,on_delete=models.CASCADE)
    wagon = models.ForeignKey(Wagon, on_delete=models.CASCADE, related_name='ticket')
    seat_number = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    wagon_type = models.CharField(max_length=10)

    arrive_time = models.DateTimeField('jonash vaqti', null=True)
    leave_time = models.DateTimeField('borish vaqti', null=True)

    def clean(self):
        if self.wagon.seat_count < 1:
            raise ValidationError(
                {'Error': "bu vagonda bosh joylar qolmagan"})
    def save(self, *args, **kwargs):
        self.wagon.seat_count -= 1
        self.wagon.save()
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name

class TicketSlz(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'






