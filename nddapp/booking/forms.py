from django import forms
from datetime import datetime
from customer.models import Principal, Shipper
from .models import Booking


class BookingFilterSortForm(forms.Form):
	date = forms.DateField(
		widget=forms.DateInput(
			attrs={
				'type': 'date',
				'class': 'form-control',
				# 'onchange': 'this.form.submit();'
			}
		),
		required=False
	)

	month = forms.DateField(
		widget=forms.DateInput(
			attrs={
				'type': 'month',
				'class': 'form-control',
				# 'onchange': 'this.form.submit();'
			}
		),
		required=False
	)

class BookingAddForm(forms.Form):

	time = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	agent = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	booking_no = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'autocomplete': 'off',
			}
		),
		required=False
	)

	booking_color = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'color',
				'class': 'form-control',
			}
		),
		required=False
	)

	pickup_from = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)
	
	return_to = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	return_date = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'date',
				'class': 'form-control',
			}
		),
		required=False,
		disabled=True,
	)

	vessel = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	port = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	closing_date = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'date',
				'class': 'form-control',
			}
		),
		required=False
	)

	closing_time = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'type': 'time',
				'class': 'form-control',
			}
		),
		required=False
	)

	ref = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	remark = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	factory = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	ADDRESS_CHOICES = (
		('shipper', 'Shipper'),
		('other', 'Other'),
		('none', 'None'),
	)
	address = forms.ChoiceField(
		choices=ADDRESS_CHOICES,
		initial="shipper",
		widget=forms.RadioSelect(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)

	address_other = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'class': 'form-control',
			}
		),
		required=False
	)