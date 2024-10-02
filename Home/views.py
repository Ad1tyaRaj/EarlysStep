from django.shortcuts import render
from .models import Suggested_Steps,Other_sec,Remides

# Create your views here.


def Home(request):
    data = Remides.objects.all()
    card = Other_sec.objects.all()

    return render(request,'Home/index.html',{'Data':data,'cards':card})

# def Remides_tamp(request,id):
#     step_data = Remides.objects.get(id=1)
#     # for i in Remides.objects.all():
#     #     instanc = i.id
#     #     print(instanc)
#     if id == 6:
#         step_data = Remides.objects.get(id=6)
#     if id == 7 :
#         step_data = Remides.objects.get(id=7)
#     if id == 8 :
#         step_data = Remides.objects.get(id=8)
#
#     return render(request,'Remides_tamplate/remedy.html',{'Step_Data':step_data})


def Remides_tamp(request,id):
    for i in Remides.objects.all():
        instance = i.id
        if id == instance:
            step_data = Remides.objects.get(id=instance)

        # if id == instance :
        #     step_data = Remides.objects.get(id=instance)
        #
        # if id == instance :
        #     step_data = Remides.objects.get(id=instance)

    return render(request,'Remides_tamplate/remedy.html',{'Step_Data':step_data})