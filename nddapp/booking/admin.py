from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'principal', 'shipper', 'agent', 'size', 'booking_no', 'booking_color', 'pickup_tr', 'pickup_from', 'forward_tr', \
    'factory', 'backward_tr', 'return_tr', 'return_to', 'container_no','seal_no', \
    'vessel', 'port', 'closing_date', 'closing_time', 'ref', 'remark', 'work_id', 'work_number', 'pickup_date', 'factory_date', 'return_date', 'pickup_in_time', 'pickup_out_time', \
    'factory_in_time', 'factory_load_start_time', 'factory_load_finish_time', 'factory_out_finish', 'return_in_time', 'return_out_time', \
    'address', 'address_other', 'cancel')

    ordering = ('date', 'work_id')
 
admin.site.register(Booking, BookingAdmin)
