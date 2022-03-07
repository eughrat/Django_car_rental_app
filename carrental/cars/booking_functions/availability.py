import datetime
from cars.models import Car, Booking

def check_availability(car, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(car=car)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
