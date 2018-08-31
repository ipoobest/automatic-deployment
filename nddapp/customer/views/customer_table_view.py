from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Principal, Shipper

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CustomerTableView(TemplateView):

    global template_name
    template_name = 'customer/customer_table.html'

    @login_required(login_url=reverse_lazy('login'))
    def get_customer_table(request):
        principals = Principal.objects.all()
        return render(request, template_name, {'principals': principals, 'nbar': 'customer'})


    @login_required(login_url=reverse_lazy('login'))
    def customer_detail(request, pk):
        principals = Principal.objects.all()

        customer = Principal.objects.get(pk=pk)
        shippers = Shipper.objects.filter(principal=pk).order_by('name')

        return render(request, template_name, {'principals': principals, 'customer': customer, 'shippers': shippers, 'nbar': 'customer'})

