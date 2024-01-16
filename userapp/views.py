from django.shortcuts import render
from mainapp.models import *

# Create your views here.
def home(request):
    category= Category.objects.all()
    
    products=Product.objects.all()[:4]
    context={"products":products,"category":category}

    return render(request,'home.html',context)
def adminindex(request):

    return render(request,'adminindex.html')
def adminside(request):

    return render(request,'adminside.html')
def indexdone(request):

    return render(request,'indexdone.html')
def admindone(request):

    return render(request,'admindone.html')
def userdetail(request):
    userdetail=Register.objects.all()
    context={"userdetail":userdetail}
    
    return render(request,'user.html',context)
def viewcategory(request):
    viewcategory=Category.objects.all()
    context={"viewcategory":viewcategory}

    return render(request,'viewcategory.html',context)
def viewcomp(request):
    viewcomp=Comment.objects.all()
    context={"viewcomp":viewcomp}
    
    return render(request,'viewcomp.html',context)

def viewproduct(request):
    viewpro=Product.objects.all()
    context={"viewpro":viewpro}

    return render(request,'viewproduct.html',context)
