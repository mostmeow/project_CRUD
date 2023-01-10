import json
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, JsonResponse

from django.contrib import messages

# หน้า
from django.core.paginator import Paginator

# django auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import *

# Create your views here.




def home(request):

    # messages.success(request, 'ยินดีต้อนรับ')

    return render(request, 'app_general/home.html')

def listitem(request):
    dummyarray = []
    ranglist = range(100)

    for i in ranglist:
        dummyarray.append(i)

    # p = Paginator(ProductModel.objects.all(), 8)
    p = Paginator(dummyarray, 8)
    page = request.GET.get('page')
    pitems = p.get_page(page)
    nums = 'a' * pitems.paginator.num_pages

    context = {
        # 'dummyarray':dummyarray,
        'pitems':pitems,
        'nums':nums,
    }
    return render(request, 'app_general/listitem.html', context)

def userform(request):
    if request.method == 'POST':
        # --DJANGOFORM
        # form = UserForm(request.POST)

        # if form.is_valid():
        #     data = form.cleaned_data
        # else:
        #     messages.error(request, 'โปรดกรอกข้อมูลให้ถูกต้อง')
        #     return redirect('userform')

        # input_name = data['name']
        # print(input_name)

        # --JAVAFORM
        print(request.POST['myname'])
        messages.success(request, 'ขอบคุณที่ลงชื่อเข้าใช้')
        return redirect('home')
        
    # form = UserForm()
    # context = {'form':form}
    return render(request, 'app_general/userform.html')

def videoitem(request):
    messages.error(request, 'หวงห้าม')
    return render(request, 'app_general/videoitem.html')

def signup(request):

    if request.method == 'POST':
        signupname = request.POST['signupname']
        signuppass = request.POST['signuppass']

        if User.objects.filter(username=signupname):
            messages.error(request, 'ชื่อผู้ใช้นี้ถูกใช้แล้ว')
            return redirect('signup')

        # ต้องใช้ create_user ถึงจะบันทึกลงdatabaseได้ถูกต้อง
        # myuser = User.objects.create_user(username=input_username, email=input_email, password=input_password)
        # myuser.first_name = input_first_name
        # myuser.last_name = input_last_name

        # myuser.is_active = False

        myuser = User.objects.create_user(username=signupname, password=signuppass)
        myuser.is_active = True

        myuser.save()
        messages.success(request, 'สร้างบัญชีสำเร็จ')
        return redirect('home')

    return render(request, 'app_general/signup.html')

def signin(request):

    if request.method == 'POST':
        signinname = request.POST['signinname']
        signinpass = request.POST['signinpass']

        signinuser = authenticate(username=signinname, password=signinpass)

        if signinuser is not None:
            login(request, signinuser)
            messages.success(request, 'ลงชื่อเข้าใช้สำเร็จ')
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.error(request, 'ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง!')
            return HttpResponseRedirect(reverse('signin'))

    return render(request, 'app_general/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'คุณได้ลงชื่อออกแล้ว')
    return HttpResponseRedirect(reverse('home'))
