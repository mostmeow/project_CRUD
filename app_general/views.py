from django.shortcuts import render

from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'app_general/home.html')

def listitem(request):
    dummyarray = []
    ranglist = range(100)

    for i in ranglist:
        dummyarray.append("a")

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