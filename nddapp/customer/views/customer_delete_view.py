from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Principal, Shipper

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CustomerDeleteView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def delete_customer(request):
        if request.method == 'POST':
            customer_pk = request.POST['customer_pk']

            customer = Principal.objects.get(pk=customer_pk)
            customer.delete()
            
        return redirect('customer-list')


    @login_required(login_url=reverse_lazy('login'))
    def delete_shipper(request):
        if request.method == 'POST':
            customer_pk = request.POST['customer_pk']
            shipper_pk = request.POST['shipper_pk']
            
            shipper = Shipper.objects.get(pk=shipper_pk)
            shipper.delete()
            
            return redirect('customer-detail', pk=customer_pk)
        else:
            return redirect('customer-list')

