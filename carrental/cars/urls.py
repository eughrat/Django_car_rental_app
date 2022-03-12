"""carrental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path
from .views import (car_list_view, car_view, BookingView, BookingListView, add_comment_to_car, AllCarsListView, CancelBookingView)

app_name = 'cars'

urlpatterns = [
    path('<int:pk>', car_view, name = "detail"),
    path('booking/<int:pk>', BookingView.as_view(), name = "booking"),
    path('booking_list', BookingListView.as_view(), name = "booking_list"),
    path('all_cars_list', AllCarsListView.as_view(), name = "all_cars_list"),
    path('car_list', car_list_view, name = "list"),
    path('<int:pk>/d+/comment/', add_comment_to_car, name='add_comment_to_car'),
    path('booking/cancel/<int:pk>',CancelBookingView.as_view(),name="CancelBookingView"),
]


