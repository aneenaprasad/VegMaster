from django.urls import path
from mainapp import views

urlpatterns = [
    path('',views.register,name="register"),
    path('login',views.login,name="login"),
    path('index',views.index,name="index"),
    path('registration_form',views.registration_form,name="registration_form"),
    path('addcat',views.addcat,name="addcat"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('blogsingle',views.blogsingle,name="blogsingle"),
    path('contact',views.contact,name="contact"),
    # path('addblog',views.addblog,name="addblog"),
    path('viewblog',views.viewblog,name="viewblog"),
    path('cart',views.cart,name="cart"),
    path('wishlist/<int:id>',views.wishlist,name="wishlist"),
    path('checkout',views.checkout,name="checkout"),
    path('viewcat',views.viewcat,name="viewcat"),
    path('singleproduct/<int:id>',views.singleproduct,name="singleproduct"),
    path('wishdone',views.wishdone,name="wishdone"),
    path('addcart/<int:id>',views.addcart,name="addcart"),
    path('viewcart/',views.viewcart,name="viewcart"),
    path('displaycart/<int:id>',views.displaycart,name="displaycart"),
    path('addcomp',views.addcomp,name="addcomp"),
    path('allproduct',views.allproduct,name="allproduct"),
    path('logout',views.logout,name="logout"),

    
]
