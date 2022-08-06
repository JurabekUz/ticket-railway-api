# bu yonalish

'''

class Direction(models.Model):
    name = models.CharField(max_length=50) #toshkent-urganch yo'nalishi
    way = models.CharField(max_length=10) # 076F (bu o'zgarmas, kalit sozga oxshaydi)

class Station(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
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

# def __repr__(self):
#     rep = ''
#     for city in self.stations.all():
#         rep += f"{city.name} - "
#     rep += f"{self.wagon_type}"
#     #cities = [ city for city in self.stations.all()]
#     #return  f"{cities[0]}-{cities[1]} {self.wagon_type}"
#     return rep

# @property
# def set_prce(self):
#     price = Voyage.price.
#     return price

class VoyageDetail(APIView):
    def get(self, request, pk, *args, **kwargs):

        voyage = Voyage.objects.get(pk=pk)

        # train data
        train = voyage.train
        train_slz = TrainSlz(train)

        # wagons data
        wagons = voyage.wagons.all().annotate(
            #pass_seats_list = Value('ticket__seat_number')
        )
        wagons_slz = WagonSlz(wagons, many=True)
        serializer = VoyageSlz(voyage)

        # wagon_number =
        # type =
        # price =
        # free_seats_count =

        return Response(data = {
            'train': train_slz.data,
            'wagons': wagons_slz.data,

        }
                        )
        # return Response(data = serializer.data)


class VoyageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        f = request.GET.get('f')
        t = request.GET.get('t')
        d = request.GET.get('date')
        date_obj = datetime.strptime(d, '%Y-%m-%d')

        result = Voyage.objects.filter(
            Q(station__name__name__in=[f, t]) & Q(station__leave_time__date=date_obj)
        )
        print(result)
        print(type(result))
        for voyage in result:
            from_station = voyage.station.get(name__name__contains=f)
            to_station = voyage.station.get(name__name__contains=t)

            # if from_station.number > to_station.number:
            #     result.exclude()

        serializer = OnlyVoyageSlz(result, many=True)

        wagons = Wagon.objects.filter(voyage__in=result).group_by('type')
        print(wagons)

        return Response(data=serializer.data)