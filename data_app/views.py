from django.shortcuts import render

# Create your views here.
from . models import my_table

def Table_show(request):
    table=my_table.objects.all()

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        table1=my_table(name=name,email=email)
        table1.save()

    return render(request,'table.html',{'table':table})