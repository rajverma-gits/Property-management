from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django import forms
from Home.models import Customer,Property,Appointment,Bill,Appointment_2,Property_2

class CustomerForms(forms.ModelForm):
    
    class Meta:
        model=Customer
        exclude='registration',
        fields='__all__'

class PropertyForms(forms.ModelForm):
    
    class Meta:
        model=Property
        fields='__all__'

class AppointmentForms(forms.ModelForm):
    
    class Meta:
        model=Appointment
        # exclude='status',
        fields='__all__'

class CreateAppointmentForms(forms.ModelForm):
    
    class Meta:
        model=Appointment
        fields='__all__'

class Appointment2Forms(forms.ModelForm):
    
    class Meta:
        model=Appointment_2
        fields='__all__'

class Property2Forms(forms.ModelForm):
    
    class Meta:
        model=Property_2
        fields='__all__'

class BillForms(forms.ModelForm):
    
    class Meta:
        model=Bill
        exclude='date',
        fields='__all__'