from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic import ListView, FormView
from .models import Car, Booking
from .forms import AvailabilityForm, CarForm, CarDetailForm, CarMainForm, CommentForm
from .booking_functions.availability import check_availability

from django.contrib.auth.decorators import login_required

def car_list_view(request):
    context = {}
    template = "car_list.html"
    if request.method == 'GET':
        car_detail_form = CarDetailForm(prefix='detail')
        car_main_form = CarMainForm(prefix='main')
        context["car_detail_form"] = car_detail_form
        context["car_main_form"] = car_main_form
        return render(request, template, context)
    if request.method == "POST":
        cars = Car.objects.select_related("main").select_related("detail").all()
        car_detail_form = CarDetailForm(request.POST, prefix='detail')
        car_main_form = CarMainForm(request.POST, prefix='main')
        if car_detail_form.is_valid() and car_main_form.is_valid():
            marka = car_main_form.cleaned_data['marka']
            if marka:
                cars = cars.filter(main__marka=marka)

            model = car_main_form.cleaned_data['model']
            if model:
                cars = cars.filter(main__model=model)

            #detail
            color = car_detail_form.cleaned_data['color']
            if color:
                cars = cars.filter(detail__color=color)

            seats = car_detail_form.cleaned_data['seats']
            if seats:
                cars = cars.filter(detail__seats=seats)

            fuel = car_detail_form.cleaned_data['fuel']
            if fuel:
                cars = cars.filter(detail__fuel=fuel)


            power_min = car_detail_form.cleaned_data['power_min']
            power_max = car_detail_form.cleaned_data['power_max']
            if power_min:
                cars = cars.filter(detail__power__gte=power_min)
            if power_max:
                cars = cars.filter(detail__power__lte=power_max)

            price_min = car_detail_form.cleaned_data['price_min']
            price_max = car_detail_form.cleaned_data['price_max']
            if price_min:
                cars = cars.filter(detail__price__gte=price_min)
            if price_max:
                cars = cars.filter(detail__price__lte=price_max)


            production_date_start = car_detail_form.cleaned_data['production_date_start']
            production_date_end = car_detail_form.cleaned_data['production_date_end']
            if production_date_start:
                cars = cars.filter(detail__production_date__gte=production_date_start)
            if production_date_end:
                cars = cars.filter(detail__production_date__lte=production_date_end)

        context['cars'] = cars
        print(cars)
        context["car_detail_form"] = car_detail_form
        context["car_main_form"] = car_main_form
        return render(request, template, context)

def car_view(request, pk):
    template="car_detail.html"
    context={}
    if request.method == "GET":
        car = Car.objects.get(id=pk)
        context['car'] = car
        return render(request, template, context)


class AllCarsListView(ListView):
    model = Car
    template_name = "all_cars_list.html"
    def get_query_set(self,*args,**kwargs):
        car_list = Booking.objects.all()
        return car_list


class BookingListView(ListView):
    model = Booking
    template_name = "booking_list.html"
    def get_query_set(self,*args,**kwargs):
        booking_list = Booking.objects.filter(user=self.requet.user)
        return booking_list

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'car_booking.html'

    def form_valid(self, form):
        data = form.cleaned_data
        car_list = Car.objects.select_related("main").select_related("detail").all()
        for car in car_list:
            if check_availability(car, data['check_in'],data['check_out']):

                booking = Booking.objects.create(
                    user = self.request.user,
                    car = car,
                    check_in = data['check_in'],

                    check_out = data['check_out'],
                )
                booking.save()
                return HttpResponse(booking)
            else:
                return HttpResponse('This car is already booked.')

@login_required
def add_comment_to_car(request, pk):
    car = get_object_or_404(Car,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('cars:detail',pk=car.pk)
    else:
        form = CommentForm()
    return render(request,'cars/comment_form.html',{'form':form})
