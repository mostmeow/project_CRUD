from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.paginator import Paginator

from .forms import *

# Create your views here.

def home(request):
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
        form = UserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
        else:
            messages.error(request, 'โปรดกรอกข้อมูลให้ถูกต้อง')
            return redirect('userform')

        input_name = data['name']
        print(input_name)

    form = UserForm()
    context = {'form':form}
    return render(request, 'app_general/userform.html', context)

def videoitem(request):
    return render(request, 'app_general/videoitem.html')