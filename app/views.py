from django.shortcuts import render

# create your views here.

def conditions(request):
    d={'a':122,'b':200}
    return render(request,'conditions.html',context=d)


def data_render(request):
    d={'a':1899,'b':2,'hobbies':['dancing','singing','painting','talking']}
    return render(request,'data_render.html',context=d)