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
        fields = ('way', 'type', 'number')

class StationPriceSlz(serializers.ModelSerializer):
    stations = CitySlz(many=True)
    class Meta:
        model = StationPrice
        fields = ('stations', 'wagon_type', 'price')

class VoyageSlz(serializers.ModelSerializer):
    train = TrainSlz()
    wagons = WagonSlz(many=True)
    price = StationPriceSlz(many=True)
    class Meta:
        model = Voyage
        fields = ('train', 'wagons', 'price')

class StationSlz(serializers.ModelSerializer):
    voyage = VoyageSlz()
    name = CitySlz(many=True)
    class Meta:
        model = Station
        fields = ('voyage', 'name', 'arrive_time', 'leave_time', 'number')



