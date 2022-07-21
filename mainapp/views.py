from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.template import loader
from django.shortcuts import render
from django.core.mail import EmailMessage
import tweepy 
import pandas as pd
from django.utils.crypto import get_random_string
from adminapp.models import *




def home(request): 
    data = Fines.objects.all()

    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAABs8egEAAAAAbqHsK%2BYcRtf3vwk%2BnDbz5Ne01rM%3DKEIbAWRYg3ZZzUftOMELv0WYtoclKJ2eWet491YZIAz6qYWhWP')
    query = 'HYDTP -is:retweet'
    tweets = client.search_recent_tweets(query=query,tweet_fields=['context_annotations', 'created_at'],user_fields=['profile_image_url'], expansions='author_id', max_results=10)
    # CONSUMER_KEY='AcBjLlGEZwYUyBjEexmIKZWq2'
    # CONSUMER_SECRET='7rfDE3Am3ESscQGdYVPJdtOWr9vjDI701tnFWptLEduVpnhuW8'
    # ACCESS_TOKEN='1544992890904281090-bkNhF2jcQDsj0kg2QMSRiMzx2CaONq'
    # ACCESS_TOKEN_SECRET='O5NjayvktlD4rOIZWA9IwegXKhnaHBEva3iWJ9b1dhfps'
    # auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    # cursor = tweepy.Cursor(api.search_tweets, q='HYDTP', tweet_mode="extended").items(10)
    # for i in cursor:
    #     print(i.full_text)
  
    context = {
        'tweet' : tweets,
        'view':data,
        
    }
    return render(request, './main/index.html', context=context)

def about(request):
    return render (request, './main/about.html')

def admin(request):
    if request.method == "POST":
        admin_email = request.POST.get('user')
        admin_pws = request.POST.get ('pws')
        if admin_email =='admin' and admin_pws =='admin':
            messages.success(request, "welcome")
            return redirect('admin_home')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('admin')
    return render(request, './main/admin.html')


def user(request):
    
    if request.method == "POST":
        phone = request.POST.get('user')    
        try:
            login = Vechile_Register.objects.filter(user_phone=phone)
            request.session["email"]= login[0].user_email
            print(request.session["email"])
            

            return redirect ("user_home")
        except:
            messages.error(request, "bad credential")
            return redirect("home")
    return render (request, './main/user.html')





def police(request):
    if request.method == "POST":
        email = request.POST.get('user')
        pws = request.POST.get ('pass')
        if email =='police' and pws =='police':
            request.session["police"]= email
            messages.success(request, "welcome")
            return redirect('police_home')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('police')
    return render (request, './main/police.html')

def contact(request):
    return render (request, './main/contact.html')

