from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Principal, Shipper

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CustomerEditView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def edit_customer(request):
        if request.method == 'POST':
            pk = request.POST['pk']
            customer_name = request.POST['customer_edit']
            work_type = request.POST['work_type_edit']

            customer = Principal.objects.get(pk=pk)
            customer.name = customer_name
            customer.work_type = work_type
            customer.save()
            
            return redirect('customer-detail', pk=pk)
        else:
            return redirect('customer-list')


    @login_required(login_url=reverse_lazy('login'))
    def edit_shipper(request):
        if request.method == 'POST':
            customer_pk = request.POST['customer_pk']
            shipper_pk = request.POST['shipper_pk']
            shipper_name = request.POST['shipper_edit']
            address = request.POST['address_edit']

            shipper = Shipper.objects.get(pk=shipper_pk)
            shipper.name = shipper_name
            shipper.address = address
            shipper.save()
            
            return redirect('customer-detail', pk=customer_pk)
        else:
            return redirect('customer-list')

