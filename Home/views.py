from django.shortcuts import render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from .models import Doctor,Chemist,LabChemist
from .forms import DoctorCreate,ChemistCreate,LabChemistCreate
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.views.decorators.cache import never_cache


# Create your views here.
@never_cache
def home(request):
    cache.clear()
    #request.session['uname'] = 'null'
    if request.session.get('uname'):
        return HttpResponseRedirect('/welcome/')
    else:
        return render(request,"Home/home.html")


def home1(request):
    if request.session.get('uname'):
        print('i get session')
        try:
            print('session delete')
            for key in list(request.session.keys()):
                print(key)
                del request.session[key]
        except KeyError:
            pass
    else:
        pass 
    return HttpResponseRedirect('/')

@never_cache
def Welcome(request):
    cache.clear()
    if request.session.get('uname'):
        return render(request,'Welcome/Doctor/dashboard.html',{'uname':request.session['uname']})
        #return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        #return render(request,'Welcome/Doctor/dashboard.html',{'uname':request.session['uname']})


def user(request):
    if request.session.get('uname'):
        return render(request,'Welcome/Doctor/user.html',{'uname':request.session['uname']})
        #return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        #return render(request,'Welcome/Doctor/user.html',{'uname':request.session['uname']})


def patient(request):
    if request.session.get('uname'):
        return render(request,'Welcome/Doctor/patient.html',{'uname':request.session['uname']})
        #return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        #return render(request,'Welcome/Doctor/patient.html',{'uname':request.session['uname']})


def table(request):
    if request.session.get('uname'):
        return render(request,'Welcome/Doctor/table.html',{'uname':request.session['uname']})
        #return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        #return render(request,'Welcome/Doctor/table.html',{'uname':request.session['uname']})


def history(request):
    if request.session.get('uname'):
        return render(request,'Welcome/Doctor/history1.html',{'uname':request.session['uname']})
        #return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        #return render(request,'Welcome/Doctor/history1.html',{'uname':request.session['uname']})


def RegDoct(request):
    dr_info = DoctorCreate()
    if request.method == 'POST':
        if Doctor.objects.filter(drEmail = request.POST.get('drEmail')) and Chemist.objects.filter(cEmail = request.POST.get('drEmail')) and LabChemist.objects.filter(lEmail = request.POST.get('drEmail')):
            return HttpResponse('Already Exist !!')
        else:
            dr_info = DoctorCreate(request.POST,request.FILES)
            if dr_info.is_valid():
                dr_info.save()
                print('good')
                request.session['uname'] = request.POST.get('drEmail')
                return HttpResponse('1')
            else:
                print('something wrong')
                return HttpResponse('You can not register !!!')
    else:
        return HttpResponse('You can not register !!!')


def RegChem(request):
    chem_info = ChemistCreate()
    if request.method == 'POST':
        if Doctor.objects.filter(drEmail = request.POST.get('cEmail')) and Chemist.objects.filter(cEmail = request.POST.get('cEmail')) and LabChemist.objects.filter(lEmail = request.POST.get('cEmail')):
            return HttpResponse('Already Exist !!')
        else:
            chem_info = ChemistCreate(request.POST,request.FILES)
            if chem_info.is_valid():
                chem_info.save()
                print('good')
                request.session['uname'] = request.POST.get('cEmail')
                return HttpResponse('1')
            else:
                print('something wrong')
                return HttpResponse('You can not register1 !!!')
    else:
        return HttpResponse('You can not register !!!')


def RegLabChemist(request):
    lab_info = LabChemistCreate()
    if request.method == 'POST':
        if Doctor.objects.filter(drEmail = request.POST.get('lEmail')) and Chemist.objects.filter(cEmail = request.POST.get('lEmail')) and LabChemist.objects.filter(lEmail = request.POST.get('lEmail')):
            return HttpResponse('Already Exist !!')
        else:
            lab_info = LabChemistCreate(request.POST,request.FILES)
            if lab_info.is_valid():
                lab_info.save()
                print('good')
                request.session['uname'] = request.POST.get('lEmail')
                return HttpResponse('1')
            else:
                print('something wrong')
                return HttpResponse('You can not register1 !!!')
    else:
        return HttpResponse('You can not register !!!')

def LogDoct(request):
    if request.method == 'POST':
        if Doctor.objects.filter(drEmail = request.POST.get('drEmail_log')) and Doctor.objects.filter(drPassword = request.POST.get('drPassWord_log')):
            dremail = request.POST.get('drEmail_log')
            request.session['uname'] = dremail
            return HttpResponse('1')
        else:
            return HttpResponse('Please Check Your Credential or Register !!!')
    else:
        return HttpResponse('You can not Login !!!')

def LogChem(request):
    if request.method == 'POST':
        if Chemist.objects.filter(cEmail = request.POST.get('cEmail')) and Chemist.objects.filter(cPassword = request.POST.get('cPassword')):
            lemail = request.POST.get('lEmail')
            request.session['uname'] = lemail
            print(request.session['uname'])
            return HttpResponse('1')
        else:
            return HttpResponse('Please Check Your Credential or Register !!!')
    else:
        return HttpResponse('You can not Login !!!')

def LogLabChemist(request):
    if request.method == 'POST':
        if LabChemist.objects.filter(lEmail = request.POST.get('lEmail')) and LabChemist.objects.filter(lPassword = request.POST.get('lPassword')):
            lemail = request.POST.get('lEmail')
            request.session['uname'] = lemail
            print(request.session['uname'])
            return HttpResponse('1')
        else:
            return HttpResponse('Please Check Your Credential or Register !!!')
    else:
        return HttpResponse('You can not Login !!!')








