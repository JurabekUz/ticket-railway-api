from django.db import models
from django.contrib.auth import  get_user_model

from trains.models import Voyage, City

User = get_user_model()
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ticket')
    voyage = models.ForeignKey(Voyage,on_delete=models.CASCADE, related_name='user_ticket')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE)
    to_city = models.ForeignKey(City, on_delete=models.CASCADE)
    wagon_number = models.IntegerField()
    seat_number = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    arrive_time = models.DateTimeField('jonash vaqti', null=True)
    leave_time = models.DateTimeField('borish vaqti', null=True)
    # vagon turi
    #
