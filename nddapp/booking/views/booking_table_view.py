from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from ..models import Booking
from customer.models import Principal, Shipper
from ..forms import BookingFilterSortForm
# from django.shortcuts import render_to_response
from datetime import datetime, timedelta, date
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class BookingTableView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def get_table(request):
        template_name = 'booking/booking_table.html'

        tmr = datetime.now() + timedelta(days=1)
        today = datetime.now()

        if request.method == "GET":
            filter_by = request.GET.get("filter_by")
            date = request.GET.get("date")
            
            if date == None:
                date = ''

            if not date:
                bookings = Booking.objects.filter((Q(date__month=today.month) & Q(date__year=today.year)) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')
            else:
                if filter_by == "month":
                    month_year = datetime.strptime(date, '%Y-%m')
                    bookings = Booking.objects.filter((Q(date__month=month_year.month) & Q(date__year=month_year.year)) | ((Q(closing_date__lte=tmr) | Q(date__lte=today)) & (Q(return_tr='') & ~Q(cancel='1')))).order_by('date', 'work_id')
                else:
                    bookings = Booking.objects.filter(Q(date=date) | ((Q(closing_date__lte=tmr) | Q(date__lte=today)) & (Q(return_tr='') & ~Q(cancel='1')))).order_by('date', 'work_id')

        else:
            bookings = Booking.objects.filter((Q(date__month=today.month) & Q(date__year=today.year)) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')

        return render(request, template_name, {'bookings': bookings, 'filter_by': filter_by, 'date': date, 'today': today, 'tmr': tmr, 'nbar': 'booking-table'})


    @login_required(login_url=reverse_lazy('login'))
    def update_data(request):
        if request.method == 'POST':
            pk = request.POST['pk']
            vessel = request.POST['vessel']
            port = request.POST['port']
            
            address = request.POST['address'+pk]
            if address == 'other':
                address_other = request.POST['address_other']

            cancel = request.POST['cancel']

            filter_by = request.POST['filter_by']
            date_filter = request.POST['date_filter']

            booking = Booking.objects.get(pk=pk)
            booking.vessel = vessel
            booking.port = port
            booking.address = address
            if address == 'other':
                booking.address_other = address_other
            booking.cancel = cancel
            booking.save()

            messages.success(request, "Updated Booking.")
            return redirect(reverse('booking-table') + '?filter_by=' + filter_by + '&date=' + date_filter)
        else:
            return redirect('booking-table')
