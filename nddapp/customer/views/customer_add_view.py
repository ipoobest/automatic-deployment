from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Principal, Shipper

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CustomerAddView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def add_customer(request):
        if request.method == 'POST':
            customer_name = request.POST['customer_add']
            work_type = request.POST['work_type_add']

            data = {
                'name': customer_name,
                'work_type': work_type
            }

            customer = Principal(**data)
            customer.save()
            
            return redirect('customer-detail', pk=customer.pk)
        else:
            return redirect('customer-list')


    @login_required(login_url=reverse_lazy('login'))
    def add_shipper(request):
        if request.method == 'POST':
            customer_pk = request.POST['customer_pk']
            shipper = request.POST['shipper_add']
            address = request.POST['address_add']

            data = {
                'principal': Principal.objects.get(pk=customer_pk),
                'name': shipper,
                'address': address
            }

            shipper = Shipper(**data)
            shipper.save()
            
            return redirect('customer-detail', pk=customer_pk)
        else:
            return redirect('customer-list')

