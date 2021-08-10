from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')    

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')    

def blog_details(request):
    return render(request,'blog-details.html')

def blog_standard(request):
    return render(request,'blog-standard.html')

def gallery(request):
    return render(request,'gallery.html')     

def index_2(request):
        return render(request,'index-2.html')

def manu(request):
    return render(request,'manu.html')    

def restaurant_details(request):
    return render(request,'restaurant-details.html')

def restaurant(request):
    return render(request,'restaurant.html')

def team(request):
    return render(request,'team.html')
