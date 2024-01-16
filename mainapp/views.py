from django.shortcuts import render,redirect
from mainapp.models import *

def register(request):
    if request.method =="POST":
        a=request.POST['name']
        b=request.POST['age']
        c=request.POST['contactno']
        d=request.POST['email']
        e=request.POST['password']
        print(a)

        data = Register(
            user_name=a,
            user_age=b,
            user_contactno=c,
            user_email=d,
            user_password=e,    
        )
        data.save()
        

    return render(request,'register.html')

def login(request):
    if request.method =="POST":
        a=request.POST['email']
        b=request.POST['password']

        if Register.objects.filter(user_email=a,user_password=b).exists():
            data = Register.objects.filter(user_email=a,user_password=b,).values('user_name', 'user_age', 'user_contactno','id').first()
            request.session['u_name'] = data['user_name']
            request.session['u_age'] = data['user_age']
            request.session['u_contactno'] = data['user_contactno']
            request.session['u_email'] = a
            request.session['u_id'] = data['id']
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    del request.session['u_name']
    del request.session['u_age']
    del request.session['u_contactno']
    del request.session['u_email']
    del request.session['u_id']
    return redirect('login') 

def index(request):
    
    return render(request,'index.html')
def about(request):
    
    return render(request,'about.html')
def registration_form(request):
    
    return render(request,'registrationform.html')
def addcat(request):
    if request.method =="POST":
        a=request.POST['addcategory']
        b=request.FILES['catimage']
        print(a)
        data = Category(
            category=a,
            category_img=b,         
        )
        data.save()
    return render(request,'addcategory.html')
def viewcat(request):
    vc=Category.objects.all()
    context={"vc":vc}
    print(vc)

    return render(request,'home.html',context)

def addproduct(request):
    category= Category.objects.all()
    context={"category":category}
    if request.method=='POST':
        category=request.POST['addcategory']
        # c_id=Category.objects.get(Category=category)
        proimage=request.FILES['productimage']
        proname=request.POST['productname']
        proprice=request.POST['productprice']
        print(proprice)
        data = Product(
            Category=Category.objects.get(id=category),
            product_image=proimage,
            product_name=proname,
            product_price=proprice,         
        )
        data.save()
    return render(request,'addproduct.html',context)
        
def blog(request):
    
    return render(request,'blog.html')
        
def blogsingle(request):
    
    return render(request,'blog-single.html')
def contact(request):
    
    return render(request,'contact.html')
# def addblog(request):
#     if request.method=="POST":
#         e=request.FILES['pimage']
#         f=request.POST['pname']
#         g=request.POST['date']
#         h=request.POST['enterblog']


#         data=Blog(
#             b_image=e,
#             b_name=f,
#             b_date=g,
#             b_enterblog=h,
#         )
#         data.save()
#     return render(request,'addblog.html')

def viewblog(request):
    if request.method=="POST":
        e=request.FILES['pimage']
        f=request.POST['pname']
        g=request.POST['date']
        h=request.POST['enterblog']


        data=Blog(
            b_image=e,
            b_name=f,
            b_date=g,
            b_enterblog=h,
        )
        data.save()
    

    vb=Blog.objects.all()
    print(vb)
    context={"vb":vb}
    return render(request,'blog.html',context)
def cart(request):
    # ct=Products.objects.get(id=id)
    # cid=request.session.get('u_id')

    
    return render(request,'cart.html')
def wishlist(request,id):
    wl=Product.objects.get(id=id)
    uid=request.session.get('u_id')
    Wishlist.objects.create(wishuser=Register.objects.get(id=uid),wishproduct=wl)

def wishdone(request):
    wid=request.session.get('u_id')
    wr=Wishlist.objects.filter(wishuser=wid)
    context={'wr':wr}
    return render(request,'wishlist.html',context)
def checkout(request):
    return render(request,'checkout.html')
def singleproduct(request,id):
    pid=request.session.get('u_id')
    sp=Product.objects.filter(id=id)
    context={"sp":sp}
    return render(request,'product-single.html',context)
def addcart(request,id):
    uid=request.session.get('u_id') 
    if request.method=='POST':
        size=request.POST['size']
        quantity=request.POST['quantity']
        totall=request.POST['total']
        
    
        print(size)
        data = Cart(
            cartproduct=Product.objects.get(id=id),
            cartuser=Register.objects.get(id=uid),
            product_size=size,
            product_quantity=quantity,
            totalsize=totall,
            
        )
        data.save()
        return redirect(f'/singleproduct/{id}')
        
    
    return render(request,'cart.html')
    # return redirect('product-single')
def displaycart (request,id):
    dc=Product.objects.get(id=id)
    did=request.session.get('u_id')
    Cart.objects.create(cartuser=Register.objects.get(id=uid),cartproduct=dc)

def viewcart(request):
    # vid=request.session.get('u_id')
    # vc=Product.objects.filter(id=id)
    # cc=Cart.objects.filter(id=id)
    # context={"vc":vc,"cc":cc}
    # return render(request,'cart.html',context)
    vid=request.session.get('u_id')
    vc=Cart.objects.filter(cartuser=vid)
    context={'vc':vc}
    return render(request,'cart.html',context)
def addcomp(request):
    if request.method=="POST":
        e=request.POST['datee']
        f=request.POST['entercomp']

        data=Comment(
            datee=e,
            addcomplain=f,
          
        )
        data.save()
    return render(request,'comment.html')
def allproduct(request):
    products=Product.objects.all()

    context={"products":products}

    return render(request,'allproduct.html',context)









