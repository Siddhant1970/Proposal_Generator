from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.auth.models import User, auth
from startpage.models import Muser, Proposals

# Create your views here.
def checkAdmin(id):
    user = User.objects.get(id = id)
    muser = Muser.objects.get(muser = user)
    if muser.status == 2 :
        return False
    else:
        return True

def adminpage(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if checkAdmin(request.user.id):
            return redirect('/login')
        m = Proposals.objects.all().order_by()[::-1] 
        context = {'med':m}
        return render(request,'home2.html',context)

def proposalDetails(request, proposal_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    else:
        if checkAdmin(request.user.id):
            return redirect('/login')

        rent = Proposals.objects.get(id=proposal_id)
        m=User.objects.get(username=rent.username)
        return render(request, 'proposalDetails2.html',{'proposal':rent,'user':m})

def final(request):
    if request.method == 'POST':
        aid = request.POST.get('aid')
        approve = request.POST.get('approve')
        reject = request.POST.get('reject')
        oname = Proposals.objects.get(id=aid)
        if approve==None:
            print(reject)
            oname.status2 = -1

            oname.save()


        elif reject==None:
            print(approve)
            oname.status2 = 1
            oname.save()

    return redirect('adminhome')
