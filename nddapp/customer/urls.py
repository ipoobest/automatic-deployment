from django.urls import path
from django.conf.urls import url
from .views.customer_table_view import CustomerTableView
from .views.customer_add_view import CustomerAddView
from .views.customer_edit_view import CustomerEditView
from .views.customer_delete_view import CustomerDeleteView


urlpatterns = [
    url(r'^$', CustomerTableView.get_customer_table, name='customer-list'),
    url(r'^(?P<pk>\d+)/detail/$', CustomerTableView.customer_detail, name='customer-detail'),

    url(r'^add-customer/$', CustomerAddView.add_customer, name='customer-add-new'),
    url(r'^add-shipper/$', CustomerAddView.add_shipper, name='shipper-add-new'),

    url(r'^edit-customer/$', CustomerEditView.edit_customer, name='customer-edit'),
    url(r'^edit-shipper/$', CustomerEditView.edit_shipper, name='shipper-edit'),

    url(r'^delete-customer/$', CustomerDeleteView.delete_customer, name='customer-delete'),
    url(r'^delete-shipper/$', CustomerDeleteView.delete_shipper, name='shipper-delete'),
]


