"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hotelapp import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('userhome/',views.Userhome,name='userhome'),
    path('index/',views.Index,name='index'),
    path('dashbord/',views.Dashbord,name='dashbord'),
    path('productlist/',views.Productlist,name='productlist'),
    path('roomlist/',views.Roomlist,name='roomlist'),
    path('roomadd/',views.RoomAdd,name='roomadd'),
    path('roomupdate/<int:id>',views.Roomupdate,name='roomupdate'),
    path('roomdelete/<int:id>',views.Roomdelete,name='roomdelete'),
    path('roomdetails/<int:id>',views.Roomdetails,name='roomdetails'),
    path('roomoffer/',views.Roomoffer,name='roomoffer'),
    path('offercard/',views.Offercard,name='offercard'),
    path('offerdetails/<int:id>',views.Offerdetails,name='offerdetails'),
    path('userlogin/',views.Login,name='userlogin'),
    path('usersignin/',views.Signin,name='usersignin'),
    path('roomproduct/', views.roomproduct,name='roomproduct'),
    path('diningadd/',views.Diningadd,name='diningadd'),
    path('diningupdate/<int:id>',views.Diningupdate,name='diningupdate'),
    path('diningdelete/<int:id>',views.Diningdelete,name='diningdelete'),
    path('offerlist/',views.Offerlist,name='offerlist'),
    path('offerupdate/<int:id>',views.Offerupdate,name='offerupdate'),
    path('offerdelete/<int:id>',views.Offerdelete,name='offerdelete'),
    path('gallery/',views.Gallery,name='gallery'),
    path('acommodations/',views.Acommodation,name='acommodation'),
    path('dining/',views.Dining,name='dining'),
    path('diningbooking/<int:id>',views.DiningBook,name='diningbooking'),
    path('diningconfirm/<int:id>',views.Diningconfirm,name='diningconfirm'),
    path('diningpay/<int:id>',views.DiningPayment,name='diningpayment'),
    path('roombooking/',views.Roombooking,name='roombooking'),
    path('roombookingpoup/<int:id>/', views.BookingPopUp,name='roombookingpoup'),
    path('roombookform/<int:id>/',views.Roombookform,name='roombookform'),
    path('bookingroom/<int:id>/',views.Bookingroom,name='bookingroom'),
    path('thankyou/',views.Thankyou,name='thankyou'),
    path('reset_password/', views.password_reset_request, name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset_password_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
   

]
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)