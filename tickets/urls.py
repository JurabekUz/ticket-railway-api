from django.urls import path

from .views import TicketsListAPIView
urlpatterns = [
    path('voyage/<int:pk>/<int:user_id>/', TicketsListAPIView.as_view()),
]