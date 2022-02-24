from django.contrib import admin
from django.urls import path
from Home import views
from django.conf import settings
from django.conf.urls.static import static

app_name='Home'

urlpatterns = [
    path("",views.index,name='home'),
    path('chart',views.PropertyChartView.as_view(),name='chart'),
    path("bills_list",views.BillListView.as_view(),name='bill-list-view'),
    path('pdf/<pk>/',views.bill_render_pdf_view,name='bill-pdf-view'),
    path("property",views.property,name='property'),
    path("customer",views.customer,name='customer'),
    path("agent",views.agent,name='agent'),
    path("appointment",views.appointment,name='appointment'),
    path("appointment2",views.appointment2,name='appointment2'),
    path("property2",views.property2,name='property2'),
    path('create_appointment/',views.createAppointment,name='create_appointment'),
    path('update_appointment/<str:pk>/',views.updateAppointment,name='update_appointment'),
    path('delete_appointment/<str:pk>/',views.deleteAppointment,name='delete_appointment'),
    path("registration",views.registration,name='registration'),
    path("owner",views.owner,name='owner'),
    path("bill",views.bill,name='bill'),
    path("signup",views.handleSignup,name='handleSignup'),
    path("login",views.handleLogin,name='handleLogin'),
    path("Logout",views.handleLogout,name='handleLogout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)