import json
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, JsonResponse

from django.contrib import messages

# หน้า
from django.core.paginator import Paginator

# django auth
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# custom decorators
from .decorators import *

# ส่งemail
from project_crud import settings
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
#สร้างtokens
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# dajngoเวอชั่นเก่าใช้force_textแต่เวอชั่น4ขึ้นใช้force_strแทน
from django.utils.encoding import force_bytes, force_str 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import generate_token

# encode/decode
import base64

# forms & models
from .forms import *
from .models import *

# Create your views here.


def home(request):

    # messages.success(request, 'ยินดีต้อนรับ')

    return render(request, 'app_general/home.html')

def listitem(request):
    # dummyarray = []
    # ranglist = range(100)

    # for i in ranglist:
    #     dummyarray.append(i)

    # p = Paginator(ProductModel.objects.all(), 8)
    # p = Paginator(dummyarray, 8)

    p = Paginator(TaskModel.objects.all(), 8)
    page = request.GET.get('page')
    pitems = p.get_page(page)
    nums = 'a' * pitems.paginator.num_pages

    context = {
        # 'dummyarray':dummyarray,
        'pitems':pitems,
        'nums':nums,
    }
    return render(request, 'app_general/listitem.html', context)

@allowed_users(allowed_roles=['customer_crud'])
@login_required(login_url='signin')
def taskcreate(request):
    # if request.method == 'POST':
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
        # print(request.POST['taskname'])
        
    # form = UserForm()
    # context = {'form':form}
    return render(request, 'app_general/taskcreate.html')

@allowed_users(allowed_roles=['customer_crud'])
@login_required(login_url='signin')
def videoitem(request):
    return render(request, 'app_general/videoitem.html')

@unauthenticated_user
def signup(request):

    if request.method == 'POST':
        signupname = request.POST['signupname']
        signuppass = request.POST['signuppass']
        signupemail = request.POST['signupemail']

        if User.objects.filter(username=signupname):
            messages.error(request, 'ชื่อผู้ใช้นี้ถูกใช้แล้ว')
            return redirect('signup')

        # ต้องใช้ create_user ถึงจะบันทึกลงdatabaseได้ถูกต้อง
        # myuser = User.objects.create_user(username=input_username, email=input_email, password=input_password)
        # myuser.first_name = input_first_name
        # myuser.last_name = input_last_name

        # myuser.is_active = False

        # create user
        try:
            myuser = User.objects.create_user(username=signupname, password=signuppass, email=signupemail)
            myuser.is_active = True

            myuser.save()

            # add user group
            group = Group.objects.get(name='customer_crud')
            myuser.groups.add(group)

            messages.success(request, 'สร้างบัญชีสำเร็จ')
            # return redirect('home')

            # ส่งอีเมล
            # gmailที่ใช้ ต้องเปิด2faของมันเอง แล้วไปที่apppasswordเอาpasswordที่generateมาใส่

            current_site = get_current_site(request)
            email_subject = 'ยินดีต้อนรับสู่"CRUD"'
            
            message_greeting = render_to_string('app_general/email/email_greeting.html', {
                'name':myuser.username,
            })

            email = EmailMessage(
                email_subject,
                message_greeting,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()

            messages.success(request, 'โปรดตรวจสอบอีเมลของท่าน')

        except:
            messages.error(request, 'ผิดพลาด')

    return render(request, 'app_general/signup.html')

@unauthenticated_user
def signin(request):

    if request.method == 'POST':
        try:
            signinname = request.POST['signinname']
            signinpass = request.POST['signinpass']

            signinuser = authenticate(username=signinname, password=signinpass)

            if signinuser is not None:
                login(request, signinuser)
                messages.success(request, 'ลงชื่อเข้าใช้สำเร็จ')
                return redirect('home')

            else:
                messages.error(request, 'ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง!')
                return redirect('signin')
        except:
            pass

    return render(request, 'app_general/signin.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, 'คุณได้ลงชื่อออกแล้ว')
    return redirect('home')
