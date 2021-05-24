from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('flavors', views.flavors, name='flavors'),
    path('dessert', views.dessert, name='dessert'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
]
