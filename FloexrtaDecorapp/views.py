import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from pip._vendor.requests.auth import HTTPBasicAuth
import requests

from FloexrtaDecor.credentials import MpesaAccessToken, LipanaMpesaPpassword
from FloexrtaDecorapp.models import Bookings, User, ImageModel
from FloexrtaDecorapp.forms import BookingsForm, ImageUploadForm



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    images = ImageModel.objects.all()  
    return render(request, 'portfolio.html', {'images': images})
    
from django.shortcuts import render, redirect
from .models import contactinfo

def contact(request):
    if request.method == 'POST':
        contactsinformation = contactinfo(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        contactsinformation.save()
        return render(request, 'contact.html', {'success': 'Information sent successfully!'})
    else:
        return render(request, 'contact.html')

def bookings(request):
    if request.method == 'POST':
        mybookings = Bookings(
            name=request.POST['name'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            design_type=request.POST['design_type'],
            budget=request.POST['budget'],
            color_preference=request.POST['color_preference'],
            furniture_needs=request.POST['furniture_needs'],
            flooring_preference=request.POST['flooring_preference'],
            timeline=request.POST['timeline'],
            comments=request.POST['comments']
        )
        mybookings.save()
        return redirect('/payment')
    else:
        return render(request, 'bookings.html')

def display(request):
    allbookings = Bookings.objects.all()
    return render(request, 'display.html', {'bookings': allbookings})

def delete(request, id):
    book = Bookings.objects.get(id=id)
    book.delete()
    return redirect('/display')

def edit(request, id):
    editbookings = Bookings.objects.get(id=id)
    return render(request, 'edit.html', {'bookings': editbookings})

def update(request, id):
    updatebookings = Bookings.objects.get(id=id)
    form = BookingsForm(request.POST, instance=updatebookings)
    if form.is_valid():
        form.save()
        return redirect('/display')
    else:
        return render(request, 'edit.html')

def login(request):
    if request.method == 'POST':
        if User.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']

        ).exists():
            return redirect('/bookings')
        else:
            return render(request,'login.html',{'error_message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        members = User(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/portfolio')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def payment(request):
    return render(request, 'payment.html')

#payment
def token(request):
    consumer_key = 'VkyyTEYlBWSeufSNFWTaJ0GG4vjL7dmGcWZvbkMTd8lKGzWM'
    consumer_secret = 'snriAMaG3x5OAOwQ4B3SalX4v1RtX8oskwIf4BD6VwEGhTzooYVwXLSUGGfGLGuj'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {  
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "FLOEXTRADECOR",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=payload, headers=headers)
        return HttpResponse("Complete the transaction")
