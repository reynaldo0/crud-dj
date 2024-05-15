from django.shortcuts import redirect, render
from .models import Member

def index(req):
    mem=Member.objects.all()
    return render(req,'index.html',{'mem':mem})

def add(req):
    return render(req, 'add.html')

def addrec(req):
    x=req.POST['first']
    y=req.POST['last']
    z=req.POST['country']
    mem = Member(firstname = x, lastname = y, country = z)
    mem.save()
    return redirect("/")

def delete(req, id):
    mem = Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(req, id):
    mem = Member.objects.get(id=id)
    return render(req, 'update.html', {'mem':mem})

def uprec(req, id):
    x = req.POST['first']
    y = req.POST['last']
    z = req.POST['country']
    mem = Member.objects.get(id=id)
    mem.firstname = x
    mem.lastname = y
    mem.country = z
    mem.save()
    return redirect("/")