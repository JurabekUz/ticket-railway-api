from django.db.models import Count, Sum, Value, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import BaseFilterBackend, OrderingFilter

from .serializers import VoyageSlz, StationSlz, StationPriceSlz, WagonSlz, TrainSlz,  OnlyVoyageSlz
from .models import Voyage, Station, StationPrice, Wagon
from datetime import datetime

WAGON_TYPES = ('PK','KP', 'LK', 'ST', 'CM', 'BN')

class VoyageListView(ListAPIView):
    '''
        - vagonlar va orindiqlar va narx lari chiqishi kk
        -  from city va to city chiqishi kerak
    '''
    serializer_class = VoyageSlz
    queryset = Voyage.objects.all()
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['satation__name', '']

    def get_queryset(self):
        fromm = self.kwargs['from']
        to = self.kwargs['to']
        date = self.kwargs['date']
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        print(fromm)
        print(to)
        print(date)
        result = self.queryset.filter(
            station__name__name__in = [fromm, to],
            station__leave_time__date=date_obj
        ).annotate(
            free_seats_count= Sum('wagons__seat_count'),
        )
        return result

        # tarvel_time = self.station.arrive_time - self.station.leave_time
        #.annotate(pass_count = Count('user_ticket'), wagon_count = )
        #.annotate(wagon = price.filter(from_city=from_city, to_city=to_city) )

class VoyageDetail(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, pk, *args, **kwargs):
        voyage = Voyage.objects.get(pk=pk)
        serializer = VoyageSlz(voyage)

        # train data
        train = voyage.train
        train_slz = TrainSlz(train)
        # wagons data
        wagons = voyage.wagons.all()
        type_groups = {}
        for type in WAGON_TYPES:
            type_groups[type] = [ wagon.number for wagon in wagons.filter(type=type) ]
        wagons_slz = WagonSlz(wagons, many=True)

        return Response(data = {
            'train': train_slz.data,
            'wagons': wagons_slz.data,
            'type_groups' : type_groups
        })

class BookedSeatNumbers(APIView): #vagondagi band joylar listi
    def get(self, request, pk, number, *args, **kwargs):
        voyage = Voyage.objects.get(pk=pk)
        # current wagon data
        wagon = voyage.wagons.get(number=number)
        seats_list = wagon.seats_list()
        print(seats_list)

        return Response(data = {
            'seats_list' : seats_list,
        })


class WagonDetail(APIView): # reys wagon ni haqida batafsil malumot #adminlar uchun
    permission_classes = [IsAdminUser,]
    def get(self, request, pk, number, *args, **kwargs):
        voyage = Voyage.objects.get(pk=pk)
        # current wagon data
        wagon = voyage.wagons.get(number=number)
        wagon_type = wagon.type
        wagon_seat_count = wagon.seat_count
        pass_seats_list = wagon.pass_seats_list()
        #wagon_price = voyage.price_data()

        return Response(data = {
            'voyage_id': pk,
            'wagon_type' : wagon_type,
            'wagon_seat_count' : wagon_seat_count,
            #'wagon_price' : wagon_price,
            'pass_seats_list' : pass_seats_list
        })
