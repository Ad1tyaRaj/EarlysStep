from django.shortcuts import render
from .models import Suggested_Steps,Other_sec

# Create your views here.


def Home(request):
    data = Suggested_Steps.objects.all()
    card = Other_sec.objects.all()

    return render(request,'Home/index.html',{'Data':data,'cards':card})


