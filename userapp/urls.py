from django.urls import path
from userapp import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('adminindex',views.adminindex,name="adminindex"),
    path('adminside',views.adminside,name="adminside"),
    path('indexdone',views.indexdone,name="indexdone"),
    path('admindone',views.admindone,name="admindone"),
    path('userdetail',views.userdetail,name="userdetail"),
    path('viewcategory',views.viewcategory,name="viewcategory"),
    path('viewcomp',views.viewcomp,name="viewcomp"),
    path('viewproduct',views.viewproduct,name="viewproduct"),
]
   