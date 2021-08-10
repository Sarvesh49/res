from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about',views.about,name='about'),

    path('faq',views.faq,name='faq'),
    path('contact',views.contact,name='contact'),
    
    path('blog_details',views.blog_details,name='blog_details'),
    path('blog_standard',views.blog_standard,name='blog_standard'),
    
    path('gallery',views.gallery,name='gallery'),
    path('index_2',views.index_2,name='index_2'),
    
    path('manu',views.manu,name='manu'),
    path('restaurant_details',views.restaurant_details,name='restaurant_details'),
    
    path('restaurant',views.restaurant,name='restaurant'),
    path('team',views.team,name='team')
]


