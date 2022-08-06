import json
from datetime import datetime, timedelta

from .celery import app
from django_celery_beat.models import PeriodicTask, IntervalSchedule

# executes every 10 seconds.

from trains.models import Wagon

@app.task
def up_date_seats_count(wagon_id):
    wagon = Wagon.objects.get(id=wagon_id)
    wagon.seat_count -= 1
    wagon.save()

# schedule, created = IntervalSchedule.objects.get_or_create(
#     every=10,
#     period=IntervalSchedule.SECONDS,
# )
#
# PeriodicTask.objects.create(
#     interval=schedule,                  # we created this above.
#     name='Importing contacts',          # simply describes this periodic task.
#     task='config.tasks.up_date_seats_count',  # name of task.
#     args=json.dumps(['arg1', 'arg2']),
#     kwargs=json.dumps({
#        'be_careful': True,
#     }),
#     expires=datetime.utcnow() + timedelta(seconds=30)
# )


