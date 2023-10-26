from django.shortcuts import redirect, render
from .models import inquiry
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
     if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        service=request.POST['service']
        address=request.POST['address']
        Inquiry=inquiry(name=name,email=email,phone=phone,message=message,service=service,address=address)
        Inquiry.save()
        return redirect('index')
     return render(request,"contact.html")
     
    
def services(request):
    return render(request,'class.html')


