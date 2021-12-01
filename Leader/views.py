from pyexpat.errors import messages

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime


# Create your views here.

from Leader.forms import  Register, Userregister
from Leader.models import emailus, dailywork,profile,suser
import easygui

def admin(request):
    return render(request,'index.html')

def register(request):
    form = Register(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            
        return redirect(admin)
    return render(request,"register.html",{"form":form})


def login(request):
    msg = ""
    
   
    
    if request.method=='POST':
        aa = request.POST.get('empid')
        bb = request.POST.get('cpsw')
        context = {
            "empid":aa
        }
        
        # print(bb)
        try:

            value = profile.objects.get(empid=aa,cpsw=bb)

            if value is not None:

                return render(request,"worklog.html",context)






        # except
        #     print('ghh')
        #     msg = "Somthing went wrong"
        except Exception as e:
            print (e)
    return render(request,"Login.html",{'msg':msg})




def work(request):
    if request.method=="POST":
        user=request.POST.get('code')
        currentdate=request.POST.get('currentdate')
        hour1 = request.POST.get('hour1','')
        hour2 = request.POST.get('hour2','')
        hour3 = request.POST.get('hour3','')
        hour4 = request.POST.get('hour4','')
        hour5 = request.POST.get('hour5','')
        hour6 = request.POST.get('hour6','')
        hour7 = request.POST.get('hour7','')
        hour8 = request.POST.get('hour8','')
        r1 = request.POST.get('r1','')
        r2 = request.POST.get('r2','')
        r3 = request.POST.get('r3','')
        r4 = request.POST.get('r4','')
        r5 = request.POST.get('r5','')
        r6 = request.POST.get('r6','')
        r7 = request.POST.get('r7','')
        r8 = request.POST.get('r8','')
        task = dailywork( user=user,currentdate=currentdate,hour1=hour1, hour2=hour2, hour3=hour3, hour4=hour4, hour5=hour5,
                         hour6=hour6, hour7=hour7, hour8=hour8, r1=r1, r2=r2,r3=r3,r4=r4,r5=r5,r6=r6,r7=r7,r8=r8)
        task.save()



    return render(request,"login.html")


def landing(request):
    return render(request,'home.html')

def contact(request):
    if request.method=='POST':
        callus=emailus(contactname=request.POST['contactname'],
                      email=request.POST['email'],
                      message=request.POST['message']
                      )
        callus.save()
        subject='SAFE AND STRONG'
        message='THANKS FOR YOUR OPINION'
        email_from=settings.EMAIL_HOST_USER
        recepient=request.POST.get('contactmail')
        print("check:",recepient)
        send_mail(subject, message, email_from, [recepient], fail_silently = False)
        return redirect(contact)
    return render(request,'contact.html')


    

# admin---------------

def superregister(request):
    form = Userregister(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect(admin)
    return render(request,"adminregister.html",{"form":form})

def superlogin(request):
    msg =""
    if request.method=='POST':
        cc = request.POST.get('username')
        dd = request.POST.get('password')
        print(dd)
        try:

            value = suser.objects.get(username=cc,password=dd)

            if value is not None:

                return redirect(admin)

        except Exception as e:
            print (e)
    return render(request,"admlog.html")











def showresults(request):
    if request.method=="POST":
        fd=request.POST.get("fromdate")
        td=request.POST.get("todate")
        searchresult=dailywork.objects.raw('select empid,date from profile where join date between "'+fd+'"' and '"'+td+'"')
        return render(request,'index.html',{"data":searchresult})
    else:
        displaydata=dailywork.objects.all()
        return render(request,'index.html',{"data":displaydata})


def detail(request):
    a = dailywork.objects.all()
    return render(request, "view.html", {'data': a})



def single(request):
 if request.method=="POST":
    user=request.POST.get('empid')
    fromdate=request.POST.get('fromdate')
    todate=request.POST.get('todate')
    aa=profile.objects.filter(empid=user)
    bb=dailywork.objects.filter(currentdate__range=[fromdate,todate],user=user)
    #aa=profile.objects.all()
    #bb=dailywork.objects.all()
    return render (request,"filter.html",{"data":aa,"data1":bb})

