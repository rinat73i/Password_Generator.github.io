from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(requests):
    
    return render(requests, 'generator/home.html') 

def password(requests):    
    
    thepassword = ''  
    length = int(requests.GET.get("length"))
    
    chars = list(string.ascii_lowercase)    
    
    if 'uppercase' in requests.GET:
        chars.extend(list(string.ascii_uppercase))
    
    if 'digits' in requests.GET:
        chars.extend(list('0123456789'))
        
    if 'symbols' in requests.GET:
        chars.extend(list('!@#$%^&*'))
        
        
    for _ in range(length):
        thepassword += random.choice(chars)
    

    return render(requests, 'generator/password.html', {'password':thepassword})

def info(requests):
    return render(requests, 'generator/info.html') 
