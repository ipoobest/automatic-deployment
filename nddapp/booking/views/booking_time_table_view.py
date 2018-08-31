# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# from django.utils import timezone
from ..models import Booking
# from customer.models import Principal, Shipper
# from ..forms import BookingFilterSortForm
# from django.shortcuts import render_to_response
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class BookingTimeTableView(TemplateView):
    
    @login_required(login_url=reverse_lazy('login'))
    def get_time_table(request):
        template_name = 'booking/booking_time_table.html'

        tmr = datetime.now() + timedelta(days=1)
        today = datetime.now()

        if request.method == "POST":
            
            pk_list = request.POST.getlist("check")
            date = request.POST['date']
            filter_by = request.POST['filter_by']

            bookings = Booking.objects.filter(pk__in=pk_list).order_by('date', 'work_id')

            request.session['pk_list'] = pk_list
            request.session['date'] = date
            request.session['filter_by'] = filter_by

            return render(request, template_name, {'bookings': bookings, 'filter_by': filter_by, 'date':date, 'today': today, 'tmr': tmr, 'nbar': 'booking-table'})
        else:
            if request.session['pk_list']:
                pk_list = request.session['pk_list']
                date = request.session['date']
                filter_by = request.session['filter_by']
                bookings = Booking.objects.filter(pk__in=pk_list).order_by('date', 'work_id')

                request.session['pk_list'] = pk_list
                request.session['date'] = date
                request.session['filter_by'] = filter_by

                return render(request, template_name, {'bookings': bookings, 'filter_by': filter_by, 'date':date, 'today': today, 'tmr': tmr, 'nbar': 'booking-table'})
            else:
                date = request.GET.get("date")
                if not date:
                    return redirect('booking-table')
                else:
                    return redirect('booking-table' + '?filter_by=' + filter_by + '&date=' + date)



    @login_required(login_url=reverse_lazy('login'))
    def save_time_table(request):
        if request.method == 'POST':
            pk = request.POST.getlist('pk')
            pickup_in_time_1 = request.POST.getlist('pickup_in_time_1')
            pickup_in_time_2 = request.POST.getlist('pickup_in_time_2')

            pickup_out_time_1 = request.POST.getlist('pickup_out_time_1')
            pickup_out_time_2 = request.POST.getlist('pickup_out_time_2')

            factory_in_time_1 = request.POST.getlist('factory_in_time_1')
            factory_in_time_2 = request.POST.getlist('factory_in_time_2')

            factory_load_start_time_1 = request.POST.getlist('factory_load_start_time_1')
            factory_load_start_time_2 = request.POST.getlist('factory_load_start_time_2')

            factory_load_finish_time_1 = request.POST.getlist('factory_load_finish_time_1')
            factory_load_finish_time_2 = request.POST.getlist('factory_load_finish_time_2')

            factory_out_finish_1 = request.POST.getlist('factory_out_finish_1')
            factory_out_finish_2 = request.POST.getlist('factory_out_finish_2')

            return_in_time_1 = request.POST.getlist('return_in_time_1')
            return_in_time_2 = request.POST.getlist('return_in_time_2')

            return_out_time_1 = request.POST.getlist('return_out_time_1')
            return_out_time_2 = request.POST.getlist('return_out_time_2')

            # pk = request.POST['pk']
            # pickup_in_time = request.POST['pickup_in_time']
            # pickup_out_time = request.POST['pickup_out_time']
            # factory_in_time = request.POST['factory_in_time']
            # factory_load_start_time = request.POST['factory_load_start_time']
            # factory_load_finish_time = request.POST['factory_load_finish_time']
            # factory_out_finish = request.POST['factory_out_finish']
            # return_in_time = request.POST['return_in_time']
            # return_out_time = request.POST['return_out_time']
            
            filter_by = request.POST['filter_by']
            date_filter = request.POST['date_filter']


            for i in range(0,len(pk)):
                booking = Booking.objects.get(pk=pk[i])
                booking.pickup_in_time = pickup_in_time_1[i] + '//' + pickup_in_time_2[i]
                booking.pickup_out_time = pickup_out_time_1[i] + '//' + pickup_out_time_2[i]
                booking.factory_in_time = factory_in_time_1[i] + '//' + factory_in_time_2[i]
                booking.factory_load_start_time = factory_load_start_time_1[i] + '//' + factory_load_start_time_2[i]
                booking.factory_load_finish_time = factory_load_finish_time_1[i] + '//' + factory_load_finish_time_2[i]
                booking.factory_out_finish = factory_out_finish_1[i] + '//' + factory_out_finish_2[i]
                booking.return_in_time = return_in_time_1[i] + '//' + return_in_time_2[i]
                booking.return_out_time = return_out_time_1[i] + '//' + return_out_time_2[i]
                
                booking.save()

            messages.success(request, "Saving Booking.")
            return redirect('booking-time')
        else:
            return redirect('booking-table')