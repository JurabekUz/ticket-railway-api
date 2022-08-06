from rest_framework import serializers

from .models import Train, City, Wagon, StationPrice, Voyage, Station

class TrainSlz(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('name', 'type', 'number')

class CitySlz(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class WagonSlz(serializers.ModelSerializer):
    class Meta:
        model = Wagon
        fields = ("type", "seat_count", "number", "voyage",)

class WagonDetailSlz(serializers.ModelSerializer):
    pass_seats_list = serializers.ListField(required=False)
    class Meta:
        model = Wagon
        fields = ("type", "seat_count", "number", "voyage", 'pass_seats_list')

class StationPriceSlz(serializers.ModelSerializer):
    from_city = CitySlz()
    to_city = CitySlz()
    class Meta:
        model = StationPrice
        fields = ('from_city','to_city', 'wagon_type', 'price')

class VoyageSlz(serializers.ModelSerializer):
    train = TrainSlz()
    wagons = WagonSlz(many=True)
    price = StationPriceSlz(many=True)
    free_seats_count = serializers.IntegerField(required=False)
    class Meta:
        model = Voyage
        fields = '__all__'

class StationSlz(serializers.ModelSerializer):
    voyage = VoyageSlz()
    name = CitySlz(many=True)
    class Meta:
        model = Station
        fields = ('voyage', 'name', 'arrive_time', 'leave_time', 'number')

class OnlyVoyageSlz(serializers.ModelSerializer):
    train = TrainSlz()
    class Meta:
        model = Voyage
        fields = ( 'name', 'train' )



