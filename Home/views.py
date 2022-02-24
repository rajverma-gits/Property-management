from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from Home.models import Agent,Registration,Owner,Property,Property_2,Customer,Appointment,Appointment_2,Bill
from Home.forms import CustomerForms,PropertyForms,AppointmentForms,BillForms,CreateAppointmentForms,Appointment2Forms,Property2Forms
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.views.generic import TemplateView
    
class PropertyChartView(TemplateView):
    template_name='bill/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Bill.objects.all()
        return context
    
class BillListView(ListView):
    model=Bill
    template_name='bill/bill_list.html'

def bill_render_pdf_view(request,*args,**kwargs):
    pk=kwargs.get('pk')
    bill=get_object_or_404(Bill,pk=pk)
    template_path = 'bill/pdf.html'
    context = {'bill': bill}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if Download
    # response['Content-Disposition'] = 'attachment; filename="bill.pdf"'
    # if Display
    response['Content-Disposition'] = 'filename="bill.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def index(request):
    recent=Property.objects.all().order_by("-id")[:5]
    props=Property.objects.all()
    return render(request,'index.html',{"messages":recent,"property":props})

def agent(request):
    data=Agent.objects.all().order_by("-id")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        agent=Agent(name=name,email=email,contact=contact)
        agent.save()
        messages.success(request,'Form has been submitted.')
        return render(request,'agent.html')
    
    return render(request,'agent.html',{"feedback":data})

def appointment(request):
    data=Appointment.objects.all().order_by("-id")
    form=AppointmentForms()
    if request.method =="POST":
        subject="Your Appointment"
        form=AppointmentForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/appointment')

    return render(request,'appointment.html',{'form':form,"feedback":data})

def appointment2(request):
    data=Appointment_2.objects.all().order_by("-id")
    form=Appointment2Forms()
    if request.method =="POST":
        subject="Your Appointment"
        form=Appointment2Forms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/appointment2')

    return render(request,'Ag-Appoin-Appoin2s.html',{'form':form,"feedback":data})

def property2(request):
    data=Property_2.objects.all().order_by("-id")
    form=Property2Forms()
    if request.method =="POST":
        form=Property2Forms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/property2')

    return render(request,'Property2s.html',{'form':form,"feedback":data})

def createAppointment(request):
    form=CreateAppointmentForms()
    if request.method=='POST':
        form=CreateAppointmentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/appointment')
    
    context={'form':form}
    return render(request,'bill/appointment_form.html',context)

def updateAppointment(request,pk):

    appointment=Appointment.objects.get(id=pk)
    form=CreateAppointmentForms(instance=appointment)

    if request.method=='POST':
        form=CreateAppointmentForms(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form}
    return render(request,'bill/appointment_form.html',context)

def deleteAppointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    context={}
    return render(request,'bill/delete.html',context)

def customer(request):
    data=Customer.objects.all().order_by("-id")
    form=CustomerForms()
    if request.method =="POST":
        form=CustomerForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/appointment')

    return render(request,'customer.html',{'form':form,"feedback":data})

def owner(request):
    data=Owner.objects.all().order_by("-id")
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        contact=request.POST.get('contact')
        password=request.POST.get('password')
        owner=Owner(name=name,email=email,username=username,contact=contact,password=password)
        owner.save()
        messages.success(request,'Form has been submitted.')
    return render(request,'owner.html',{"feedback":data})

def property(request):
    data=Property.objects.all().order_by("-id")
    form=PropertyForms()
    if request.method =="POST":
        form=PropertyForms(request.POST,request.FILES)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/property')

    return render(request,'property.html',{'form':form,"feedback":data})

def bill(request):
    form=BillForms()
    if request.method =="POST":
        form=BillForms(request.POST,request.FILES)
        # print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request,'Form has been submitted.')
            return redirect('/bill')

    return render(request,'bill.html',{'form':form})

def registration(request):
    data=Registration.objects.all().order_by("-id")
    if request.method =="POST":
        date=request.POST.get('date')
        desc=request.POST.get('desc')
        registration=Registration(date=date,desc=desc)
        registration.save()
        messages.success(request,'Form has been submitted.')
    return render(request,'registration.html',{"feedback":data})

def handleSignup(request):
    if request.method=='POST':
        # Get the post parameters
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # Check for errorneous inputs
        # Username should be under 10 characters
        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('/')
        # Username should be alphanumeric
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('/')
        # Passwords should match
        if pass1!=pass2:
            messages.error(request,"Password Do not match")
            return redirect('/')


        # Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been succesfully created")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials,Please Try again")
            return redirect('/')
    
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('/')