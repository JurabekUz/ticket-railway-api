from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import TicketSlz, Ticket

class TicketsListAPIView(ListCreateAPIView):
    serializer_class = TicketSlz
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


