from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import AgentTransport
from ..forms import AgentTransportFilterSortForm
from datetime import datetime, timedelta
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

class AgentTransportEditTableView(TemplateView):
    
    @login_required(login_url=reverse_lazy('login'))
    def get_edit_table(request):
        template_name = 'agent_transport/agent_transport_edit_table.html'

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
    def save_edit_table(request):
        if request.method == 'POST':
            pk = request.POST['pk']
            date = request.POST['date']
            pickup_tr = request.POST['pickup_tr']
            pickup_from = request.POST['pickup_from']
            return_tr = request.POST['return_tr']
            return_to = request.POST['return_to']
            container_1 = request.POST['container_1']
            container_2 = request.POST['container_2']
            ref = request.POST['ref']
            remark = request.POST['remark']
            pickup_date = request.POST['pickup_date']
            return_date = request.POST['return_date']

            filter_by = request.POST['filter_by']
            date_filter = request.POST['date_filter']

            if not date:
                date = None
            if not pickup_date:
                pickup_date = None
            if not return_date:
                return_date = None

            agent_transport = AgentTransport.objects.get(pk=pk)
            agent_transport.date = date
            agent_transport.pickup_tr = pickup_tr
            agent_transport.pickup_from = pickup_from
            agent_transport.return_tr = return_tr
            agent_transport.return_to = return_to
            agent_transport.container_1 = container_1
            agent_transport.container_2 = container_2
            agent_transport.ref = ref
            agent_transport.remark = remark
            agent_transport.pickup_date = pickup_date
            agent_transport.return_date = return_date
            agent_transport.save()

            messages.success(request, "Saving Agent Transport.")
            return redirect(reverse('agent-transport-edit') + '?filter_by=' + filter_by + '&date=' + date_filter)
        else:
            return redirect('agent-transport-edit')
