from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from ..models import Booking
from customer.models import Principal, Shipper
from ..forms import BookingAddForm
# from django.shortcuts import render_to_response
from datetime import datetime
from django.db.models import Max
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class BookingAddView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def add_booking(request):
        add_booking = BookingAddView()
        template_name = 'booking/booking_add.html'
        context = {}
        context['form'] = BookingAddForm()
        context['principals'] = Principal.objects.all().order_by('name')
        context['nbar'] = 'booking-table'
        if request.method == 'POST':
            context = add_booking.create_context(request.POST)
            
        return render(request, template_name, context)

    def create_context(self, req):
        context = {}
        # context['form'] = BookingAddForm()
        context['principals'] = Principal.objects.all().order_by('name')
        if 'principal' in req:
            # print(request.POST)
            context['principal'] = req.get('principal')
            if context['principal']:
                context['shippers'] = Shipper.objects.filter(principal=context['principal']).order_by('name')
            else:
                context['shippers'] = []

            req._mutable = True
            context['size'] = req.getlist('size')
            context['quantity'] = req.getlist('quantity')
            context['date'] = req.getlist('date')
            context['zip'] = zip(context['size'], context['quantity'], context['date'])

            req.update({'size':'', 'quantity':'', 'date':''})
            context['form'] = BookingAddForm(req)
        return context

    @login_required(login_url=reverse_lazy('login'))
    def save_booking(request):
        add_booking = BookingAddView()
        if request.method == 'POST':
            form = BookingAddForm(request.POST)
            if form.is_valid():
                # print(request.POST)
                principal = request.POST['principal']
                shipper = request.POST['shipper']
                agent = request.POST['agent']
                booking_no = request.POST['booking_no']
                booking_color = request.POST['booking_color']
                size = request.POST.getlist('size')
                quantity = request.POST.getlist('quantity')
                date = request.POST.getlist('date')
                pickup_from = request.POST['pickup_from']
                factory = request.POST['factory']
                return_to = request.POST['return_to']
                vessel = request.POST['vessel']
                port = request.POST['port']
                closing_date = request.POST['closing_date']
                closing_time = request.POST['closing_time']
                ref = request.POST['ref']
                remark = request.POST['remark']
                address = request.POST['address']

                cut = request.POST['cut']

                if not closing_date:
                    closing_date = None
                if address == 'other':
                    address_other = request.POST['address_other']

                container = zip(size, quantity, date)
                for s, q, d in container:
                    add_booking.work_id_after_add(d, shipper, int(q))
                    
                    if cut == '1':
                        return_date = request.POST['return_date']
                    else:
                        return_date = d

                    for i in range(int(q)):
                        work_id, work_number = add_booking.run_work_id(d, shipper)
                        data = {
                            'principal': Principal.objects.get(pk=principal),
                            'shipper': Shipper.objects.get(pk=shipper),
                            'agent': agent,
                            'booking_no': booking_no,
                            'booking_color': booking_color,
                            'size': s,
                            'date': d,
                            'pickup_from': pickup_from,
                            'factory': factory,
                            'return_to': return_to,
                            'vessel': vessel,
                            'port': port,
                            'closing_date': closing_date,
                            'closing_time': closing_time,
                            'ref': ref,
                            'remark': remark,
                            'work_id': work_id,
                            'work_number': work_number,
                            'pickup_date': d,
                            'factory_date': d,
                            'return_date': return_date,
                            'address': address
                        }
                        if address == 'other':
                            data['address_other'] = address_other

                        booking = Booking(**data)
                        booking.save()
                 
                messages.success(request, "Added Booking.")
                return redirect('booking-table')
            messages.error(request, "Form not validate.")
        return redirect('booking-add')


    def run_work_id(self, date, shipper):
        work = Booking.objects.filter(date=date).aggregate(Max('work_number'))
        if work['work_number__max'] == None:
            work_number = 0
        else:
            work_shipper = Booking.objects.filter(date=date, shipper=shipper).aggregate(Max('work_number'))
            if work_shipper['work_number__max'] == None:
                work_number = work['work_number__max'] + 1
            else:
                work_number = work_shipper['work_number__max'] + 1

        work = str("{:03d}".format(work_number))
        d = datetime.strptime(date, "%Y-%m-%d")
        work_id = d.strftime('%d')+d.strftime('%m')+d.strftime('%y')+work
        return work_id, work_number


    def work_id_after_add(self, date, shipper, quantity):
        max_work = Booking.objects.filter(date=date, shipper=shipper).aggregate(Max('work_number'))
        if max_work['work_number__max']:
            work_gt = Booking.objects.filter(date=date, work_number__gt=max_work['work_number__max'])
            for work in work_gt:               
                new_work_number = work.work_number + quantity
                work_str = str("{:03d}".format(new_work_number))
                d = datetime.strptime(date, "%Y-%m-%d")
                work_id = d.strftime('%d')+d.strftime('%m')+d.strftime('%y')+work_str

                booking = Booking.objects.get(pk=work.pk)
                booking.work_id = work_id
                booking.work_number = new_work_number
                booking.save()
        return None

            

