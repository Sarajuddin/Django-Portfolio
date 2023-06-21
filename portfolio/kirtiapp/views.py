from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from kirtiapp.models import Connection, viewed
from django.conf import settings
from django.core.mail import send_mail
import socket
from datetime import datetime

# Create your views here.
def index(request):
    def device_type():
        if request.user_agent.is_mobile:
            return 'Mobile'
        if request.user_agent.is_tablet:
            return 'Tablet'
            # request.user_agent.is_touch_capable
        if request.user_agent.is_pc:
            return 'PC/Laptop'
        if request.user_agent.is_bot:
            return 'Bot'
    
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    browser = request.user_agent.browser.family
    os = request.user_agent.os.family + " " + request.user_agent.os.version_string
    description = device_type()
    time = datetime.now().ctime()

    if request.method=='POST':
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message').capitalize()
        
        if len(phone) != 10:
            messages.info(request, "Phone number should be 10 Character long.")
            return redirect('/#contact')
        if phone.startswith('6') or phone.startswith('7') or phone.startswith('8') or phone.startswith('9'):
            pass
        else:
            messages.info(request, "Phone number should start with (6,7,8,9)")
            return redirect('/#contact')
        
        member = Connection(name=name, email=email, phone=phone, message=message, hostname=host_name, ip=host_ip, browser=browser, os=os, description=description, time=time)
        member.save()

        subject = f'{name} wants to connect with you through your Portfolio'
        message = f'Name : {name}\nEmail : {email}\nPhone : {phone}\n\n {message}\n\nWe have get some credential information of the user. Please look at them - \n\n Device Name : {host_name}\nIP Address : {host_ip}\nBrowser : {browser}\nOperation System : {os}\nDevice Type : {description}\nTime : {time}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['saraju.work@gmail.com', 'kirtirajput63969@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
        # print('Mail is Sent.')

        messages.success(request, "Message is Sent")
        return redirect('/#contact')
    
    subject = f'Someone viewed your Portfolio'
    message = f'We have detected that someone viewed your portfolio. Some information of the user are given below - \n\nDevice Name : {host_name}\nIP Address : {host_ip}\nBrowser : {browser}\nOperation System : {os}\nDevice Type : {description}\nTime : {time}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saraju.work@gmail.com', 'kirtirajput63969@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    # print('Mail is sent......')
    
    member = viewed(hostname=host_name, ip=host_ip, browser=browser, os=os, description=description, time=time)
    member.save()
    
    return render(request, 'index.html')