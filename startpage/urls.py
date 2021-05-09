
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('submitt_form',views.submitt_form, name='submitt_form'),
    #path('main',views.main),
    path('login_submit',views.login_submitt),
    path('logout',views.logout),
    path('contact',views.contact),
    path('sellerreg',views.sellerreg),
    path('rentVehichle',views.rentVehichle),
    
    path('products',views.product),
    path('contact_form',views.contact_form),
    path('addmeet',views.addmeet),
    path('process',views.process),
    path('gallery',views.gallery)
]
