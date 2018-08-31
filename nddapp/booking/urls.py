from django.urls import path
from django.conf.urls import url
from .views.booking_table_view import BookingTableView
from .views.booking_print_view import BookingPrintView
from .views.booking_add_view import BookingAddView
from .views.booking_edit_table_view import BookingEditTableView
from .views.booking_time_table_view import BookingTimeTableView
from .views.booking_delete_view import BookingDeleteView
# from .views.authentication_view import AuthenticationView


urlpatterns = [
    url(r'^$', BookingTableView.get_table, name='booking-table'),
    url(r'^print/(?P<pk>\d+)/(?P<template>\w+)/$', BookingPrintView.as_view(), name='booking-print'),

    url(r'^add/$', BookingAddView.add_booking, name='booking-add'),
    url(r'^save/$', BookingAddView.save_booking, name='booking-save'), 

    url(r'^delete/(?P<pk>\d+)/$', BookingDeleteView.delete_data, name='booking-delete'), #delete in table page
    url(r'^delete/$', BookingDeleteView.delete_multiple, name='booking-delete-multiple'),
    
    url(r'^update/$', BookingTableView.update_data, name='booking-update'), #update in table page

    url(r'^edit/$', BookingEditTableView.get_edit_table, name='booking-edit'),
    url(r'^edit/save/$', BookingEditTableView.save_edit_table, name='booking-edit-save'),

    url(r'^time/$', BookingTimeTableView.get_time_table, name='booking-time'),
    url(r'^time/save/$', BookingTimeTableView.save_time_table, name='booking-time-save'),

    url(r'^time/print/$', BookingPrintView.print_time, name='booking-print-time'),
]


