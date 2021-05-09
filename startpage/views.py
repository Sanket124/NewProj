
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Contact,RentVehichle,Muser
from django.contrib.sessions.models import Session  
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
 
# Create your views here.
def sellerreg(request):
     if request.session.has_key('is_logged'):
        return render(request, 'sellerregis2.html')
     else:
         return redirect('/login')

        

     
    

def index(request):
    return render(request, 'main.html')

def main(request):
    data=RentVehichle.objects.all().order_by()[::-1] 
    if request.session.has_key('is_logged'):
        return render(request, 'mainpage.html',{"messages": data})
    return redirect('/login')
    #return render(request, 'mainpage.html')
   
def register(request):
    return render(request, 'register2.html')
    
    
def login(request):
    
    return render(request, 'login.html')
 
def submitt_form(request):
     #print('Hello lund') 
     if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        u_email=request.POST['email']
        passw=request.POST['password']
        conf_pass=request.POST['confpassword']
        if passw==conf_pass:

            if User.objects.filter(username=uname).exists():
                messages.info(request,'User Taken')
                return redirect('/')

            elif User.objects.filter(email=u_email).exists():
                messages.info(request,'E-mail Taken')
                return redirect('/')


            else:
                user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=u_email,password=passw)
                muser = Muser(muser=user)
                user.save()
                muser.save()
                #sendmail
                #email = EmailMessage(
                #'Welcome '+uname+' to our platform',
                #'Welcome to Findmyride the only platform where you can book a self-driven vehichle to explore any city or outstation',
                # 'sanketpandey619@gmail.com',
                #[u_email],
                
                #)
                #email.send(fail_silently=False)
                #endmail
                return redirect('/process')
                
            
        else:
            print('user not saved')
            return redirect('/register')

            
            
     else:
        return render(request,'index.html')

def login_submitt(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['pass']
        #email=request.POST['email']
        user=auth.authenticate(username=uname,password=passw)
        
        try:
            muser = Muser.objects.get(muser=user)
        except Exception as e:
            return redirect('/register')
        if user is not None:
            request.session['is_logged']=True
            if muser.status == 1:
                auth.login(request,user)
                return redirect('/sadmin')
            else:
                auth.login(request, user)
                print(request, user)
                return redirect('/products')

            
        else:
            messages.error(request,'invalid user')
            return redirect('/')

    else:
        return render(request,'main.html')
    
def logout(request): 
    del request.session['is_logged']
    auth.logout(request)
    return redirect('/')

def contact_form(request):
    
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    subject=request.POST['subject']
    messagee=request.POST['message']
    #login_user=User.objects.get(username=request.user.username)
    new_contact=Contact(firstname=fname,lastname=lname,email=email,subject=subject,message=messagee)
    new_contact.save()
    return redirect('/contact')
    
    
        
    

def rentVehichle(request):
    if request.method=='POST':
        ownname=request.POST['fullname'] 
        dname=request.POST['deptname']              
        address=request.POST['address']
        wano=request.POST['cno'] 
        std_img=request.FILES['myfile']
         
        #fs = FileSystemStorage()
        #filename = fs.save(vehichle_regis.name, vehichle_regis) 

        login_user=User.objects.get(username=request.user.username)
        new_rent=RentVehichle(username=login_user,fullname=ownname,dept_name=dname,
        address=address,whatsapp_no=wano,shop_photo=std_img )
        new_rent.save()
        
    #return render(request,'mainpage.html')     
    return redirect('/main')    
    #return render(request,'sellerregis.html')         
    
def addmeet(request):
    return render(request,"addmeet.html")

def product(request):
    return render(request,"products.html")

def process(request):
    return render(request,"process.html")

def gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,"contact.html")

     

    
     
    

     
