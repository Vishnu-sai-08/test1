from django.shortcuts import render,redirect
from app1.models import register

def ev1(request):
    return render(request,"eve1.html")

def log(request):
    return render(request,"login.html")

def reg(request):
    return render(request,"register.html")

def mia(request):
    return render(request,"main.html")

def cont(request):
    return render(request,"contact.html")

def abo(request):
    return render(request,"about.html")

def use(request):
    return render(request,"user.html")

def adm(request):
    return render(request,"admin.html")

def modi(request):
    operation=request.GET['operation']
    Username = request.GET['Username']
    Email = request.GET['Email']
    password = request.GET['assword']
    Phone = request.GET['Phone']
    desig = request.GET['Desig']
    r=register.objects.get(Email=Email)
    if operation == 'update':
        r.Username=Username
        r.Email=Email 
        r.password=password
        r.Phone=Phone
        r.desig=desig  
        r.save()
    else:
        register.delete(r)     
    print(operation)
    users = register.objects.all()
    return render(request,"views.html",{"users":users})


def vus(request):
    users = register.objects.all()
    return render(request,"views.html",{"users":users})

def doreg(request):
    print("calindee...")
    Username = request.GET['username']
    Email  = request.GET['email']
    Password = request.GET['password']
    Phone = request.GET['phone']
    r = register()
    r.Username=Username
    r.Email=Email
    r.password=Password
    r.Phone=Phone
    r.save()
    return render(request,"login.html",{"msg":"success"})

def logincheck(request):
    email1=request.GET['email']
    password1=request.GET['password']
    r=None
    try:   
     r=register.objects.get(Email=email1,password=password1)
    except Exception as ex:
        return render(request,"login.html",{"msg":"Invalid Email/Password"})
    if(r!=None):
        if(r.desig == 'user'):
            return redirect("/userhome")
        if(r.desig == 'admin'):
            return redirect("/adminhome")
        else:
            return render(request,"login.html", {'msg': "Invalid designation"})
    return render(request,"success.html")

