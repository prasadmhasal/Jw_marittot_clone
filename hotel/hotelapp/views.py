from django.shortcuts import render , HttpResponseRedirect , HttpResponse
from .models import *
from .forms import ProductForm 
from django.contrib.auth import authenticate ,login 
from django.contrib import messages
from django.contrib.auth.models import User
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def Home(request):
    return render(request,'user/index.html')

def Userhome(request):
    slider = RoomProduct.objects.all().order_by('-id')[:3] 
    offer = RoomOffer.objects.all().order_by('-id')[:3] 
    return render(request,'user/userhome.html',{'slider':slider,'offer':offer})


def Index(request):
    fm = ProductForm()
    if request.method =='POST':
        fm=ProductForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            fm=ProductForm()
    return render(request,'admin/index1.html',{'fm':fm})


def Productlist(request):
    data = Product.objects.all()
    print(data)
    return render(request,'admin/productlist.html',{'data':data})

def RoomAdd(request):
    if request.method == 'POST':
        rname = request.POST.get('rname')
        capacity = request.POST.get('capacity')
        desc=request.POST.get('desc')
        views = request.POST.get('views')
        caption = request.POST.get('caption')
        price = request.POST.get('price')
        beds_bedding=request.POST.get('bedbedding')
        food_beverages = request.POST.get('foodbeverage')
        entertainment =request.POST.get('entertainment')
        bath_bathroom_features=request.POST.get('bathbathroom')
        kitchen_features=request.POST.get('kitchen')
        room_features=request.POST.get('roomfeature')
        accessible_features = request.POST.get('accessible')
        furniture_furnishings = request.POST.get('furniture')
        internet_phones =request.POST.get('internate')
        hospitality_services=request.POST.get('hospitality')
        image = request.FILES.get('image')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        print(rname,capacity,desc,views,price, caption)
        RoomProduct.objects.create(room=rname,capacity=capacity,desc=desc,view=views,caption=caption,price=price,image=image,img1=img1,img2=img2,img3=img3,beds_bedding=beds_bedding,food_beverages=food_beverages,entertainment=entertainment, bath_bathroom_features= bath_bathroom_features,kitchen_features=kitchen_features,room_features=room_features,accessible_features=accessible_features, furniture_furnishings= furniture_furnishings, internet_phones= internet_phones, hospitality_services= hospitality_services)
        messages.success(request,"Data Add successfully")
        return HttpResponseRedirect('/roomadd/')
    return render(request,'admin/roomadd.html')

def Roomlist(request):
        roomlist = RoomProduct.objects.all()
        print(roomlist)
        return render(request,'admin/roomlist.html',{'roomlist':roomlist})

def Roomupdate(request, id):
    if request.method == 'POST':
        rup = RoomProduct.objects.get(pk=id)
        rup.room = request.POST.get('rname')
        rup.capacity = request.POST.get('capacity')
        rup.caption = request.POST.get('caption')
        rup.description = request.POST.get('desc')  
        rup.views = request.POST.get('views')
        rup.price = request.POST.get('price')
        if 'image' in request.FILES:
            rup.image = request.FILES['image']
        if 'img1' in request.FILES:
            rup.img1 = request.FILES['img1']
        if 'img2' in request.FILES:
            rup.img2 = request.FILES['img2']
        if 'img3' in request.FILES:
            rup.img3 = request.FILES['img3']
            
        rup.save()
        messages.success(request, "Data Update successful..")
        return HttpResponseRedirect('/roomlist/')
    else:
        rup = RoomProduct.objects.get(pk=id)
        return render(request, 'admin/actionsforms/roomupdate.html',{'rp':rup})

def Roomdelete(request,id):
    if request.method == "POST":
        rde = RoomProduct.objects.get(pk=id)
        rde.delete()
        messages.success(request, "Data Delete successful.")
        return HttpResponseRedirect('/roomlist/')
    else:
        return HttpResponse("Invalid method. Use POST.")


def Roomdetails(request,id):
    detail = RoomProduct.objects.filter(pk=id)
    print(detail)
    return render(request,'user/roomdetails.html',{'detail':detail})

    


def Dashbord(request):
    return render(request,'admin/dashbord.html')


def Signin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        print(uname,email,pass1)
        User.objects.create_user(uname,email,pass1)
        messages.success(request,"Sign in successfully competed")
        return HttpResponseRedirect('/userlogin/')
    else:
        return render(request,'user/signin.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get ('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/userhome/')
    return render(request,'user/login.html')


def roomproduct(request):
    return render(request,'admin/roomproduct.html')

def Roomoffer(request):
    if request.method == 'POST':
        room = request.POST.get('rname')
        capacity = request.POST.get('capacity')
        desc = request.POST.get('desc')
        caption = request.POST.get('caption')
        price =request.POST.get('price')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        include = request.POST.get('include')
        needknow = request.POST.get('needknow')
        image = request.FILES.get('image')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        print(room,capacity,desc,capacity,startdate,enddate)
        RoomOffer.objects.create(room=room,capacity=capacity,caption=caption,desc=desc,startdate=startdate,enddate=enddate,price=price,image=image,img1=img1,img2=img2,img3=img3,include=include,needknow=needknow)
        messages.success(request,"Data enter successfull..") 
        return HttpResponseRedirect('/roomoffer/')
    else:
        return render(request,'admin/roomoffer.html')

def Diningadd(request):
    if request.method == 'POST':
        dining = request.POST.get('dtitle')
        dtype = request.POST.get('dtype')
        descripation = request.POST.get('desc')
        dtime = request.POST.get('dtime')
        ntime=request.POST.get('ntime')
        day = request.POST.get('day')
        number = request.POST.get('number')
        dresscode=request.POST.get('dresscode')
        prebooking=request.POST.get('prebooking')
        image = request.FILES.get('image')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        print(dining,dtype,descripation,dtime,ntime)
        Product.objects.create(dining=dining,dtype=dtype,descripation=descripation,dtime=dtime,ntime=ntime,number=number,dresscode=dresscode,image=image,img1=img1,img2=img2,img3=img3,day=day,prebooking=prebooking)
        messages.success(request,"Data enter successfull..") 
        return HttpResponseRedirect('/diningadd/')  
    else:
       return render(request,'admin/diningadd.html')

def Diningupdate(request,id):
    if request.method == 'POST':
        up=Product.objects.get(pk=id)
        up.dining = request.POST.get('dtitle')
        up.dtype = request.POST.get('dtype')
        up.descripation = request.POST.get('desc')
        up.dtime = request.POST.get('dtime')
        up.ntime=request.POST.get('ntime')
        up.day = request.POST.get('day')
        up.number = request.POST.get('number')
        up.dresscode=request.POST.get('dresscode')
        up.prebooking=request.POST.get('prebooking')
        if 'image' in request.FILES:
            up.image = request.FILES['image']
        if 'img1' in request.FILES:
            up.img1 = request.FILES['img1']
        if 'img2' in request.FILES:
            up.img2 = request.FILES['img2']
        if 'img3' in request.FILES:
            up.img3 = request.FILES['img3']
        up.save()
        messages.success(request,"Data Update successfull..") 
        return HttpResponseRedirect('/productlist/')
    else:
        up=Product.objects.get(pk=id)
        return render(request,'admin/actionsforms/diningupdate.html',{'up':up})
    
def Diningdelete(request, id):
    if request.method == 'POST':
        # try:
        de = Product.objects.get(pk=id)
        de.delete()
        messages.success(request, "Data Delete successful.")
        return HttpResponseRedirect('/productlist/')
    else:
        return HttpResponse("Invalid method. Use POST.")
      
def Offerlist(request):
    offer=RoomOffer.objects.all()
    print(offer)
    return render(request,'admin/offerlist.html',{'off':offer})

def Offerupdate(request,id):
    if request.method == 'POST':
        offerup = RoomOffer.objects.get(pk=id)
        offerup.room=request.POST.get('rname')
        offerup.capacity=request.POST.get('capacity')
        offerup.desc=request.POST.get('decs')
        offerup.startdate=request.POST.get('startdate')
        offerup.enddate=request.POST.get('enddate')
        offerup.price=request.POST.get('price')
        if 'image' in request.FILES:
            offerup.image = request.FILES['image']
        if 'img1' in request.FILES:
            offerup.img1 = request.FILES['img1']
        if 'img2' in request.FILES:
            offerup.img2 = request.FILES['img2']
        if 'img3' in request.FILES:
            offerup.img3 = request.FILES['img3']
        offerup.save()
        messages.success(request,"Data enter successfull..") 
        return HttpResponseRedirect('/offerlist/')
    else:
        offerup=RoomOffer.objects.get(pk=id)
        return render(request,'admin/actionsforms/offerupdate.html',{'offerup':offerup})

def Offerdelete(request,id ):
    if request.method == "POST":
        offerde=RoomOffer.objects.get(pk=id)
        offerde.delete()
        messages.success(request,"data sucessfully deleted")
        return HttpResponseRedirect('/offerlist/')
    else:
        return HttpResponse(request,'admin/offerlist')     

def Offercard(request):
    card = RoomOffer.objects.all().order_by('-id')[:8]
    return render(request,'user/offercard.html',{'card':card})

def Offerdetails(request,id):
    offerdetail = RoomOffer.objects.filter(pk=id)
    alloffer = RoomOffer.objects.all().order_by('-id')[:8]
    return render(request,'user/offerdetails.html',{'offerdetail':offerdetail,'alloffer':alloffer})

def Gallery(request):
    return render(request,'user/gallery.html')

def Acommodation(request):
    data = RoomProduct.objects.all().order_by('-id')[:8]
    return render(request,'user/acommodations.html',{'data':data})

def Dining(request):
    dining = Product.objects.all()
    return render(request,'user/dining.html' ,{'dining':dining})

def DiningBook(request,id):
    book = Product.objects.filter(pk=id)
    cid = id
    if request.method == "POST":
        restaurant= request.POST.get('restaurant')
        time=request.POST.get('booking_time')
        adult=request.POST.get('adult')
        date=request.POST.get('date')
        children=request.POST.get('children')
        prebooking=request.POST.get('prebooking')
        title=request.POST.get('title')
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        cnumber=request.POST.get('cnumber')
        number=request.POST.get('number')
        email=request.POST.get('email')
        note=request.POST.get('message')
        print(restaurant,time,adult,date,children,prebooking,title,first_name,last_name,cnumber,number,email,note)
        DiningBooking.objects.create(product_id=id,restaurant=restaurant,time=time,adult=adult,date=date,children=children,prebooking=prebooking,title=title,first_name=first_name,last_name=last_name,cnumber=cnumber,number=number,email=email,note=note)
        messages.success(request,"Data enter successfull..") 
        return HttpResponseRedirect(f'/diningconfirm/{cid}')
    
    return render(request,'user/diningbooking.html',{'book':book,'cid':cid})

def Roombooking(request):
    return render(request,'user/roombooking.html')


@csrf_exempt
def Diningconfirm(request,id):
    confirm= DiningBooking.objects.filter(product_id=id)
    print(confirm)
    client = razorpay.Client(auth=("rzp_test_VPel75yVZnzpbD", "SYoHmR95xmbUb7BNW1SSLzBc"))
    product_amt= Product.objects.filter(id=id).values_list('prebooking',flat=True)
    print(product_amt)
    print(product_amt[0])
    amount = product_amt[0]
    data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    context = {}
    context['amt']= amount*100
    context['confirm']=confirm
    print(confirm)
    context['pid'] = id
    return render(request,'user/diningconfirm.html',context)

def DiningPayment(request,id):
    client = razorpay.Client(auth=("rzp_test_VPel75yVZnzpbD", "SYoHmR95xmbUb7BNW1SSLzBc"))
    product_amt= Product.objects.filter(id=id).values_list('prebooking',flat=True)
    print(product_amt[0])
    amount = product_amt[0]
    data = {"amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    context = {}
    context['amt']= amount*100

    context['pid'] = id
    
    return render(request,'user/pay.html',context)