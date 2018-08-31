from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import AgentTransport
from ..forms import AgentTransportFilterSortForm
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class AgentTransportTableView(TemplateView):

    @login_required(login_url=reverse_lazy('login'))
    def get_table(request):
        template_name = 'agent_transport/agent_transport_table.html'

        today = datetime.now()

        if request.method == "GET":
            filter_by = request.GET.get("filter_by")
            date = request.GET.get("date")

            if date == None:
                date = ''

            if not date:
                agent_transports = AgentTransport.objects.filter((Q(date__month=today.month) & Q(date__year=today.year)) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')
            else:
                if filter_by == "month":
                    month_year = datetime.strptime(date, '%Y-%m')
                    agent_transports = AgentTransport.objects.filter((Q(date__month=month_year.month) & Q(date__year=month_year.year)) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')
                else:
                    agent_transports = AgentTransport.objects.filter(Q(date=date) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')
        else:
            agent_transports = AgentTransport.objects.filter((Q(date__month=today.month) & Q(date__year=today.year)) | (Q(return_tr='') & ~Q(cancel='1'))).order_by('date', 'work_id')

        return render(request, template_name, {'agent_transports': agent_transports, 'filter_by': filter_by, 'date': date, 'today': today, 'nbar': 'agent-transport-table'})
    

    @login_required(login_url=reverse_lazy('login'))
    def update_data(request):
        if request.method == 'POST':
            pk = request.POST['pk']
            address = request.POST['address'+pk]
            if address == 'other':
                address_other = request.POST['address_other']

            cancel = request.POST['cancel']

            filter_by = request.POST['filter_by']
            date_filter = request.POST['date_filter']

            agent_transport = AgentTransport.objects.get(pk=pk)
            agent_transport.address = address
            if address == 'other':
                agent_transport.address_other = address_other
            agent_transport.cancel = cancel
            agent_transport.save()

            messages.success(request, "Updated Agent Transport.")
            return redirect(reverse('agent-transport-table') + '?filter_by=' + filter_by + '&date=' + date_filter)
        else:
            return redirect('agent-transport-table')
