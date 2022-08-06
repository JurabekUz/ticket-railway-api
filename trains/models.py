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

    def __str__(self):
        return self.name

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

class StationPrice(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='st_price')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE)
    #stations = models.ManyToManyField('City')
    wagon_type = models.CharField(max_length=5, choices=WAGON_TYPE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.from_city}-{self.to_city}, {self.wagon_type}"

class Voyage(models.Model):
    name = models.CharField(max_length=100)
    train = models.ForeignKey(Train, on_delete=models.SET_NULL, null=True)
    price = models.ManyToManyField(StationPrice)
    # station, wagons,
    @property
    def wagon_count(self):
        return self.wagons.count()
    wagon_counts = wagon_count

    def __str__(self):
        return f"{self.name}"

    def price_data(self, from_city, to_city, type):
        #result = self.station__name__name in [from_city, to_city])
        result = self.price.filter(from_city=from_city, to_city=to_city, wagon_type=type)
        return result

    def get_wagon_data(self, number): #with wagon number
        return self.wagons.get(number=number)

    def pass_count(self):
        return self.user_ticket.count()

    # def voyage_free_seats_data(self):
    #     data = {}
    #     for wagon in self.wagons.all():
    #         wagon_number = wagon.number
    #         wagon_type = wagon.type
    #         #free_seats_count = wagon.seat_count - self.user_ticket.fiter(wagon_number=wagon_number).count()
    #         free_seats_count = wagon.free_seat_count
    #         data[wagon_number] = free_seats_count
    #     return data

    def wagon_free_seats_data(self):
        data = {}
        print(self.wagons.all().values_list('type'))
        for type in set(self.wagons.all().values_list('type')):
            print(type)
            free_seats_count = 0
            for wagon in self.wagons.filter(type=type):
                free_seats_count += wagon.seat_count
            data[type] = free_seats_count
        return data


class Station(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='station')
    name = models.ForeignKey(City, on_delete=models.CASCADE)
    arrive_time = models.DateTimeField('kelish vaqti', null=True)
    leave_time = models.DateTimeField('ketish vaqti', null=True)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('number',)

class Wagon(models.Model):
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name='wagons')
    type =  models.CharField(max_length=5, choices=WAGON_TYPE)
    seat_count = models.IntegerField() #free_seat_count
    number = models.IntegerField()

    def __str__(self):
        return  f"{self.voyage}: {self.number}-{self.type}"

    class Meta:
        ordering = ['number']

    def tikckets_count(self):
        return self.ticket.count()

    def free_seat_count(self):
        return self.seat_count

    def seats_list(self):
        result = self.ticket.all().values('seat_number')
        print(result)
        return result

    def pass_seats_list(self):
        result = self.ticket.all().values('seat_number', 'user')
        print(result)
        return result




