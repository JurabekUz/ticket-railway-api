from django.urls import path

from .views import VoyageListView, VoyageDetail, WagonDetail, BookedSeatNumbers

urlpatterns = [
    path('voyage/<str:from>/<str:to>/<str:date>/', VoyageListView.as_view()),
    path('voyage-detail/<int:pk>/', VoyageDetail.as_view()),
    path('voyage-wagon-data/<int:pk>/<int:number>/', WagonDetail.as_view()),
    path('voyage-wagon-booked-seats/<int:pk>/<int:number>/', BookedSeatNumbers.as_view()),

    # path('process/train/',VoyageAPIView.as_view() )
]