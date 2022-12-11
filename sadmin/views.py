from django.shortcuts import render,redirect
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.contrib.auth.models import User, auth
from startpage.models import Muser, Proposals

# Create your views here.
def checkAdmin2(id):
    user = User.objects.get(id = id)
    muser = Muser.objects.get(muser = user)
    if muser.status == 1:
        return False
    else:
        return True

def adminpage2(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if checkAdmin2(request.user.id):
            return redirect('/login')
        m = Proposals.objects.all().order_by()[::-1] 
        context = {'med':m}
        return render(request,'home1.html',context)

def proposalDetails2(request, proposal_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if checkAdmin2(request.user.id):
            return redirect('/login')
        rent = Proposals.objects.get(id=proposal_id)
        m=User.objects.get(username=rent.username)
        return render(request, 'try.html',{'proposal':rent,'user':m})

def final(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        approve = request.POST.get('approve')
        reject = request.POST.get('reject')
        oname = Proposals.objects.get(id=aid)
        if approve==None:
            print(reject)
            oname.status = -1

            oname.save()


        elif reject==None:
            print(approve)
            oname.status = 1
            oname.save()
            # #sendmail
            # send_mail(
            #     'We are ,
            #      'siddhantpandey118@gmail.com',
            #     [oname],
            #     fail_silently=False
            # )
            # email.send(fail_silently=False)
            # endmail

    return redirect('adminhome2')
