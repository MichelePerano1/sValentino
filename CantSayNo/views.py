from django.shortcuts import render
from random import randint


# Create your views here.

def sanVal_view(request):
    row=6
    col=12
    if request.method=='POST':
        row=randint(2,17)
        col=randint(2,17)
        while (row==6 and col==6):
            row=randint(2,17)
            col=randint(2,17)
    return render(request,'MyVal.html',{'row':row , 'col':col})

def yes_view(request):
    return render(request, "yes_page.html")