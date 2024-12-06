
from django.contrib import admin
from django.urls import path

from FloexrtaDecorapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('bookings/', views.bookings, name='bookings'),
    path('display/', views.display, name='display'),
    path('delete/<int:id>', views.delete ),
    path('edit/<int:id>', views.edit, name='edit' ),
    path('update/<int:id>', views.update, name='update' ),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('payment/', views.payment, name='payment'),
    
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
