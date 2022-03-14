from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()


class CarMain(models.Model):
    brand = models.CharField(max_length=16)
    model = models.CharField(max_length=32)

class CarDetail(models.Model):
    CAR_COLORS = [
        ("RED", "Red"),
        ("BLU", "Blue"),
        ("YEL", "Yellow"),
        ("BLA", "Black"),
        ("WHI", "White")
    ]
    CAR_FUELS = [
        ("DIE", "Diesel"),
        ("PET", "Petrol"),
        ("HYB", "Hybrid"),
        ("LPG", "LPG"),
        ("ELE", "Electric"),
    ]
    production_date = models.DateField()
    color = models.CharField(max_length=3, choices=CAR_COLORS)
    seats = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])
    fuel = models.CharField(max_length=3, choices=CAR_FUELS)
    power = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])

class Car(models.Model):
    main = models.ForeignKey(CarMain, on_delete=models.CASCADE)
    detail = models.OneToOneField(CarDetail, on_delete=models.PROTECT)
    image = models.ImageField(blank=True, null=True)

    def delete(self):
        super(Car, self).delete()
        self.detail.delete()

    def __str__(self):
        return f"{self.main.brand} {self.main.model}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.user} has booked {self.car} from {self.check_in} to {self.check_out}"

    def get_cancel_booking_url(self):
        return reverse_lazy('cars:CancelBookingView',args=[self.pk])

class Comment(models.Model):
    car = models.ForeignKey('cars.Car', related_name='comment', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse('cars:list')

    def __str__(self):
        return self.text
