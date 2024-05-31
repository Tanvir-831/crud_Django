from django.shortcuts import redirect,render
from .models import Member
def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})


def add(request):
    return render(request,'add.html')


def addrec(request):
    x=request.POST['first']
    y=request.POST['first']
    z=request.POST['first']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect("/")