from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.paginator import Paginator

from .forms import *

# Create your views here.

def home(request):
    messages.success(request, 'ยินดีต้อนรับ')
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