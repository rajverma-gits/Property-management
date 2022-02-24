from django.contrib import admin
# Register your models here.
from Home.models import Agent,Owner,Registration,Property,Property_2,Customer,Appointment,Appointment_2,Bill
admin.site.site_header="My Website | Property Management"

class CustomerAdmin(admin.ModelAdmin):
    list_display=["id","name","email","contact","address","registration"]
    search_feilds=["name","email","contact","registration"]
    list_filter=["name","email","contact","registration"]

class OwnerAdmin(admin.ModelAdmin):
    list_display=["id","name","email","contact","username","password"]
    search_feilds=["name","email","contact","username","password"]
    list_filter=["name","email","contact","username"]

class Property_2Admin(admin.ModelAdmin):
    list_display=["id","property","agent"]
    search_feilds=["property","agent"]
    list_filter=["property","agent"]

class PropertyAdmin(admin.ModelAdmin):
    list_display=["id","name","desc","property_type","status","location","Owner"]
    search_feilds=["name","property_type","status","location","Owner"]
    # list_filter=["name","property_type","status","location","Owner"]
    list_filter=["Owner"]

class AgentAdmin(admin.ModelAdmin):
    list_display=["id","name","email","contact"]
    search_feilds=["name","email","contact"]
    list_filter=["email","contact"]

class AppointmentAdmin(admin.ModelAdmin):
    list_display=["id","date","customer","desc","status","owner"]
    search_feilds=["date","customer","status","owner"]
    list_filter=["date","customer","desc","status","owner"]

class Appointment_2Admin(admin.ModelAdmin):
    list_display=["id","owner","agent"]
    search_feilds=["owner","agent"]
    list_filter=["owner","agent"]

class RegistrationAdmin(admin.ModelAdmin):
    list_display=["id","date","desc"]
    search_feilds=["date"]
    list_filter=["date"]

class BillAdmin(admin.ModelAdmin):
    list_display=["id","customer","property","owner","amount","date"]
    list_filter=["date"]


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Property_2,Property_2Admin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Appointment,AppointmentAdmin)
admin.site.register(Appointment_2,Appointment_2Admin)
admin.site.register(Bill,BillAdmin)