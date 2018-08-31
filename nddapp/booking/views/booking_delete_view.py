from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Booking
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class BookingDeleteView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def delete_data(request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()

        if request.method == "GET":
            filter_by = request.GET.get("filter_by")
            date = request.GET.get("date")
            if not date:
                return redirect(reverse('booking-table'))
            else:
                return redirect(reverse('booking-table') + '?filter_by=' + filter_by + '&date=' + date)


    @login_required(login_url=reverse_lazy('login'))
    def delete_multiple(request):
        
        if request.method == "POST":
            pk_list = request.POST.getlist('check')
            filter_by = request.POST['filter_by']
            date = request.POST['date']

            for pk in pk_list:
                booking = Booking.objects.get(pk=pk)
                booking.delete()

            if not date:
                return redirect(reverse('booking-table'))
            else:
                return redirect(reverse('booking-table') + '?filter_by=' + filter_by + '&date=' + date)