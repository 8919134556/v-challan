from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from paytum import Checksum
from policeapp.models import V_Fines
MERCHANT_KEY = '**************************'
from adminapp.models import *
from .models import*

def user_home(request):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    
    return render(request, './user/user-home.html', {'view': data1, 'view1': data})



def view_challan(request, num):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    data2 = V_Fines.objects.filter(vechile_number=num)
    data3 = Payments.objects.filter(vechile_number=num)
    return render (request, './user/view-challan.html', {'view': data1, 'view1': data2, 'view2' : data3})

def payments(request, id):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    data2 = V_Fines.objects.get(id = id)
    request.session["p_id"] = id
    print(request.session["p_id"])
    param_dict={}
    if request.method == "POST":
        fname = request.POST['fname']
        v_name = request.POST['v-name']
        casuse = request.POST['casuse']
        amount = request.POST['amount']
        v_color = request.POST['v_color']
        v_num = request.POST['v_num']
        chars =  'abcdefghijklmnopqrstuvwxyz0123456789'
        order_id = get_random_string(8, chars)
        data = Payments.objects.create(user_name=fname, vechile_make=v_name, causes=casuse, 
        amount=amount, vechile_color=v_color, vechile_number=v_num, order_id=order_id)
        
        print("1")
        param_dict={
        'MID': '*****************',
        'ORDER_ID': str(order_id),
        'TXN_AMOUNT': str(amount),
        'CUST_ID': str(v_num),
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'WEBSTAGING',
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:5555/userapp/paymentrequest',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return  render(request, './user/paytm.html', {'param_dict': param_dict})
    return render(request, './user/payments.html',{'view' : data2, 'view1': data1})



@csrf_exempt
def paymentrequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            print( response_dict.values())
            order_id = response_dict['ORDERID']
            status = "Success"
            tex_id = response_dict['TXNID']
            payment_mode = response_dict['PAYMENTMODE']
            bank_tex_id = response_dict['BANKTXNID']
            bank_name = response_dict['BANKNAME']
            
            data = get_object_or_404(Payments, order_id = order_id)
            data.order_id = order_id
            data.status = status
            data.tex_id = tex_id
            data.payment_mode = payment_mode
            data.bank_tex_id = bank_tex_id
            data.bank_name = bank_name
            data.save(update_fields =['order_id', 'tex_id', 'status', 'payment_mode', 'bank_tex_id', 'bank_name'])
            messages.success(request, "Transction Successfuly Complite")
            return redirect("user_home")
            
        else:
            messages.error(request, "Transction Failure")
            return redirect("user_home") 
            
    return {'response': response_dict}


def u_complient(request, id):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    data2 = V_Fines.objects.get(id = id)
    context = {
    'view':data1,
    'view2' : data2
        }
    if request.method == "POST":
        name = request.POST['name']
        v_num = request.POST['v-num']
        causes = request.POST['causes']
        amount = request.POST['amount']
        u_complient = request.POST['complient']
        chars =  '0123456789'
        tic_id = get_random_string(10, chars)
        complient = Complient.objects.create(tic_id=tic_id, user_name=name, vechile_num=v_num, causes=causes, 
        amount=amount, complient=u_complient, user_email=request.session["email"])
        complient.save()
        email = EmailMessage('Subject',f'Hello {name},\nWe Take Your Complient\nHere Your Details:\nTicket Id : {tic_id}\n Your Complient : {u_complient}\n With Two or Three days we will solve you Problem', to=[ request.session["email"]])
        email.send()
        return redirect("compliant")
    return render(request, './user/user-complient.html', context=context)






def challa_list(request):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    data2 = Fines.objects.all()
    return render (request, './user/challan-list.html', {'view': data1, 'view1':data2})

def compliant(request):
    data = Vechile_Register.objects.filter(user_email=request.session["email"])
    data1 = data[0]
    data2 = Complient.objects.filter(user_email=request.session["email"])
    return render (request, './user/compliant.html', {'view': data1, 'view1':data2})

def u_logout(request):
    # del request.session["email"]
    return redirect('home')



