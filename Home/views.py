from django.shortcuts import render
from .models import Suggested_Steps

# Create your views here.


def Home(request):
    data = Suggested_Steps.objects.all()

    return render(request,'Home/index.html',{'Data':data})


