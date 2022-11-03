from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
#hello

def function(request):
    if request.method == 'POST':
        name = request.POST.get("n")
        address = request.POST.get("add")
        empID = request.POST.get("Eid")
        a = Sai(name=name,address=address,empID=empID)
        a.save()
        print(name,address,empID)
    else:
        return render(request,"task.html",context={})
    return HttpResponse("printed on Console, please Check!!")










# Create your views here.

# def func(request):
#     if request.method=='POST':
#         name=request.POST.get("nm")
#         address=request.POST.get("add")
#         city=request.POST.get("city")
#         pincode=request.POST.get("pin")
#         print(name,address)
#     return HttpResponse("Printed on Console!! Please check")
#     #return render(request,"page1.html",context={})
#     # return redirect("page2")



# def func2(request):
#     # a=Kiran()
#     # b=Kiran.objects.get(empID=12335)
#     # c=Kiran.objects.filter(empID=12335)
#     # print(b)
#     # print(b.name)
#     #d=Kiran.objects.all()
#     #print(d)
    
#     #return render(request,"page1.html",context={"name":"SAikiran"})
#     return render(request,"page1.html",context={})

# def func3(request):
#     if request.method=='POST':
#         name=request.POST.get("n")
#         address=request.POST.get("add")
#         Eid=request.POST.get("Eid")
#         print(name,address,Eid)
#     return HttpResponse("Printed on Console!! Please check")


# def func4(request):
#     return render(request,"task.html",context={})




# def func5(request):
#     x=Sai()
#     y=Sai.name(input())
#     z=Sai.address(input())
#     z1=Sai.empID(int(input()))
#     y.save()
#     z.save()
#     z1.save()
#     return HttpResponse("Done")
