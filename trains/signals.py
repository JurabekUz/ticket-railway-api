
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# @receiver(pre_save, sender=Ticket)
# def valid_order(sender, instance, **kwargs):
#     if instance.wagon.seat_count < 1:
#         raise ValidationError(
#             {'Error': "bu vagonda bosh joylar qolmagan"})
#
# @receiver(post_save, sender = Ticket)
# def vali(sender, instance, **kwargs):
#     wagon = instance.wagon
#     wagon_id = wagon.id
#     up_date_seats_count.delay(wagon_id)