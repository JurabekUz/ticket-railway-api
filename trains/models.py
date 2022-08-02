from django.db import models

WAGON_TYPE = [
        ('PK', 'plasskart'),
        ('KP' ,'puke'),
        ('LK', 'lyuks'),
        ( 'ST', 'seat'),
        ( 'CM', 'comfort'),
        ( 'BN', 'business')
    ]

class City(models.Model):
    name = models.CharField(max_length=50)

class Train(models.Model):

    NAME = [
        ('AF', 'Afrosiyob'),
        ('SH', 'Sharq'),
        ('PS', 'Oddiy')
    ]

    TYPE = [
        ('CK', 'CK'),
        ('PASS', 'PASS'),
        ('CKPCT', 'CKPCT')
    ]

    name = models.CharField(max_length=2, choices=NAME)
    type = models.CharField(max_length=5, choices=TYPE)
    number = models.CharField(max_length=10) #key

    def __str__(self):
        return f"{self.name} ({self.type})"

class Wagon(models.Model):
    way = models.CharField(max_length=10)
    type =  models.CharField(max_length=5, choices=WAGON_TYPE)
    number = models.IntegerField()

    def __str__(self):
        return  f"{self.way}: {self.number}-{self.type}"

class StationPrice(models.Model):
    stations = models.ManyToManyField('City')
    wagon_type = models.CharField(max_length=5, choices=WAGON_TYPE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return  f"{self.stations.name} {self.wagon_type}"

class Voyage(models.Model):
    train = models.ForeignKey(Train, on_delete=models.SET_NULL, null=True)
    price = models.ManyToManyField(StationPrice)
    wagons = models.ManyToManyField(Wagon)


class Station(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    name = models.ForeignKey(City, on_delete=models.CASCADE)
    arrive_time = models.DateTimeField('kelish vaqti', null=True)
    leave_time = models.DateTimeField('ketish vaqti', null=True)
    number = models.PositiveSmallIntegerField()


# bu yonalish

'''

class Direction(models.Model):
    name = models.CharField(max_length=50) #toshkent-urganch yo'nalishi
    way = models.CharField(max_length=10) # 076F (bu o'zgarmas, kalit sozga oxshaydi)

class Station(models.Model):
    station = models.ForeignKey(City, on_delete=models.CASCADE)
    arrive_time = models.TimeField('kelish vaqti')
    leave_time = models.TimeField('ketish vaqti')
    number = models.PositiveSmallIntegerField()

class Voyage(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    date = models.DateField('reys kuni')
    train = models.ForeignKey(Train, on_delete=models.SET_NULL, null=True)
    price = models.ManyToManyField(StationPrice)
    wagons = models.ManyToManyField(Wagon)

    # muammo 
    # station dagi time bilan voyage dagi date ni birlashtirib  datetime ni hosil qilish kerak

'''






