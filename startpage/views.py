
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Contact, Muser, Proposals


# Create your views here.
def generate_prop(request):
     if request.session.has_key('is_logged'):
        # context = {'med':m}
        return render(request, 'generate_prop.html')
     else:
         return redirect('/login')

def index(request):
    return render(request, 'index.html')

def main(request):
    # data=Shops.objects.all().order_by()
    if request.session.has_key('is_logged'):
        login_user=User.objects.get(username=request.user.username)
        m = Proposals.objects.filter(username=login_user)
        context = {'med':m}
        return render(request, 'mainpage.html',context)
    return redirect('/login')
    #return render(request, 'mainpage.html')
   
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
 
def submitt_form(request): 
     if request.method=='POST':
        uname=request.POST['name']
        u_email=request.POST['email']
        passw=request.POST['password']
        conf_pass=request.POST['re_password']
        if passw==conf_pass:

            if User.objects.filter(username=uname).exists():
                messages.info(request,'User Taken')
                return redirect('/')

            elif User.objects.filter(email=u_email).exists():
                messages.info(request,'E-mail Taken')
                return redirect('/')


            else:
                user = User.objects.create_user(username=uname,email=u_email,password=passw)
                muser = Muser(muser=user)
                user.save()
                muser.save()
                #sendmail
                # send_mail(
                # 'Welcome '+uname+' to our platform',
                # 'Welcome to Findmyride the only platform where you can book a self-driven vehichle to explore any city or outstation',
                #  'siddhantpandey118@gmail.com',
                # [u_email],
                # fail_silently=False
                # )
                # email.send(fail_silently=False)
                #endmail
                return redirect('/login')
        else:
            print('user not saved')
            return redirect('/register')

            
            
     else:
        return render(request,'index.html')

def login_submitt(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['pass']
        user=auth.authenticate(username=uname,password=passw)

        if user is not None:
            muser = Muser.objects.get(muser=user)
            request.session['is_logged']=True
            if muser.status == 1:
                auth.login(request,user)
                return redirect('/sadmin')
            elif muser.status == 2:
                auth.login(request,user)
                return redirect('/pip')
            else:
                auth.login(request, user)
                # print(request, user)
                return redirect('/main')

        else:
            messages.error(request,'invalid user')
            return redirect('/register')

    else:
        return render(request,'/register.html')
    
def logout(request): 
    auth.logout(request)
    return redirect('/')

def contact_form(request):
    fname=request.POST['firstname']
    lname=request.POST['lastname']
    email=request.POST['email']
    subject=request.POST['subject']
    messagee=request.POST['message']
    login_user=User.objects.get(username=request.user.username)
    if request.session.has_key('is_logged'):
        new_contact=Contact(username=login_user,firstname=fname,lastname=lname,email=email,subject=subject,message=messagee)
        new_contact.save()
        return redirect('/main')

    else:
         return redirect('/login')

def proposals(request):
    if request.method=='POST':
        # ownname=request.POST['oname'] 
        sname=request.POST['sname']              
        address=request.POST['saddress']
        wano=request.POST['wano'] 
        # hdstatus=request.POST['hdstatus'] 
        # date=request.POST[]
        vehichle_regis=request.FILES['vregis'] 
        # vehichle_img=request.FILES['myfile']

        #fs = FileSystemStorage()
        #filename = fs.save(vehichle_regis.name, vehichle_regis) 

        login_user=User.objects.get(username=request.user.username)
        new_rent=Proposals(username=login_user,ownername=request.user.username,shop_name=sname,
        address=address,Date=wano,shop_registration=vehichle_regis)
        new_rent.save()

    #return render(request,'mainpage.html')     
    return redirect('/main')    
    #return render(request,'sellerregis.html')        
    
def prac(request):
    return render(request,"prac.html")

def proposalDetails3(request, proposal_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        rent = Proposals.objects.get(id=proposal_id)
        return render(request, 'proposalDetails3.html',{'proposal':rent})

def final3(request):
    # if request.method == 'POST':
    

    return redirect('/main')



