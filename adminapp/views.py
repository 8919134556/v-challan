from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import *
from userapp.models import *
from policeapp.models import *
from mainapp.models import *
from django.db.models import Sum

def admin_home(request):
    v_regi = Vechile_Register.objects.all().count()
    fines = Fines.objects.all().count()
    money = Payments.objects.filter(status ="Success").aggregate(price_sum=Sum('amount'))
    v_fines = V_Fines.objects.all().count()
    context = {
        'data1' : v_regi,
        'data2' : fines,
        'data3' : money['price_sum'],
        'data4' : v_fines
    }
    return render (request, './admin/dashboard.html', context = context)

def upload_vechile(request):
    if request.method == "POST" and request.FILES["user-image"] and request.FILES["myFile"] :
        gender = request.POST['gender']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        v_type = request.POST['v-type']
        v_year = request.POST['v-year']
        v_make = request.POST['v-make']
        v_model = request.POST['v-model']
        v_color = request.POST['v-color']
        v_mileage = request.POST['v-mileage']
        v_number = request.POST['v-number']
        country = request.POST['country']
        state = request.POST['state'] 
        city = request.POST['city']
        s_name = request.POST['s-name']
        h_number = request.POST['h-number']
        u_image = request.FILES['user-image']
        v_image = request.FILES['myFile']
        reg_details = Vechile_Register.objects.create(gender=gender,user_name=fname,user_lastname=lname,
        user_phone=phone,country=country,state=state,city=city,vechile_year=v_year,vechile_make=v_make,
        vechile_model=v_model,vechile_color=v_color,vechile_mileage=v_mileage,vechile_number=v_number,
        vechile_type=v_type,street_name=s_name,house_number=h_number,vechile_image=v_image,
        user_email=email,user_image = u_image)
        reg_details.save()

    return render (request, './admin/upload-vechile.html')

def v_deatils(request):
    data = Vechile_Register.objects.all()
    return render (request, './admin/view-details.html', {'view' : data})

def popup(request, id):
    data = Vechile_Register.objects.get(id=id)
    return render (request, './admin/popup-form.html', {'view': data})

def fine(request):
    data = Fines.objects.all()
    return render (request, './admin/fine.html', {'view' : data})

def fine_details(request):
    if request.method == "POST" and request.FILES["image"]:
        title = request.POST['title']
        prison = request.POST['prison']
        amount = request.POST['amount']
        subject = request.POST['subject']
        image = request.FILES['image']
        data = Fines.objects.create(title=title, prison=prison, amount=amount,descrption=subject, image=image)
        data.save()
    return render (request, './admin/upload-fine-details.html')

def fine_edit(request, id):
    data = Fines.objects.get(id=id)
    if request.method == "POST" and request.FILES["image"] :
        title = request.POST['title']
        prison = request.POST['prison']
        amount = request.POST['amount']
        subject = request.POST['subject']
        image = request.FILES['image']
        data1 = get_object_or_404(Fines, id=id)
        data1.title = title
        data1.prison = prison
        data1.amount = amount
        data1.descrption = subject
        data1.image = image
        data1.save(update_fields=["title","prison","amount","descrption", "image"])
        data1.save()
        return redirect("fine")

    return render (request, './admin/fine-edit.html', {'view': data})



def logout(request):
    return redirect("home")