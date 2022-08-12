from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing,name='landing'),    
    path('index',views.index,name='index'),    
    path('student', views.student, name='student'),    
    path('createstudent', views.createstudent, name='createstudent'),    
    path('<int:pk>/viewstudent/<str:sk>', views.vstudent, name='vstudent'),
    path('year/branch/<int:pk>/viewstudent/<str:sk>', views.vstudent, name='vstudent'),         
    path('yourprofile/year/branch/<int:pk>/viewstudent/<str:sk>', views.vstudent, name='vstudent'),           
    path('year/branch/<int:pk>/viewstudent/creatememory/<str:sk>', views.creatememory, name='creatememory'),
    path('yourprofile/year/branch/<int:pk>/viewstudent/creatememory/<str:sk>', views.creatememory, name='creatememory'),
    path('<int:pk>/viewstudent/creatememory/<str:sk>', views.creatememory, name='creatememory'),
    path('register', views.register,name='register'),
    path('login', views.loginuser,name='login'),
    path('logout', views.logoutuser,name='logout'),   
    path('yourprofile/<str:pk>', views.yourprofile,name='yourprofile'),
    path('yourprofile/edit_detail/edituserdetail/<str:pk>', views.edituserdetail,name='edituserdetail'),
    path('year/branch/<int:sk>/viewstudent/edit_detail/edituserdetail/<str:pk>', views.edituserdetail_admin,name='edituserdetail'),
    path('yourprofile/edit_detail/<str:pk>', views.edit_detail,name='edit_detail'),
    path('year/branch/<int:sk>/viewstudent/edit_detail/<str:pk>', views.edit_detail_admin,name='edit_detail'),
    path('year/<int:pk>', views.year, name='year'),    
    path('year/branch/<int:pk>/<str:sk>', views.branch, name='branch'),    
    path('year/branch/<int:pk>/viewstudent/createcomment/<str:sk>', views.createcomment, name='createcomment'),    
    path('<int:pk>/viewstudent/createcomment/<str:sk>', views.createcomment, name='createcomment'),    
    path('year/branch/<int:pk>/viewstudent/approve/<str:sk>/<int:mk>', views.approve, name='approve'),    
    path('yourprofile/year/branch/<int:pk>/viewstudent/approve/<str:sk>/<int:mk>', views.approve, name='approve'),
    path('year/branch/<int:pk>/viewstudent/decline/<str:sk>/<int:mk>', views.decline, name='decline'),  
    path('yourprofile/year/branch/<int:pk>/viewstudent/decline/<str:sk>/<int:mk>', views.decline, name='decline'), 
    path('year/branch/<int:pk>/viewstudent/deletemem/<str:sk>/<int:mk>', views.deletemem, name='deletemem'), 
    path('yourprofile/year/branch/<int:pk>/viewstudent/deletemem/<str:sk>/<int:mk>', views.deletemem, name='deletemem'), 
    path('<int:pk>/viewstudent/approve/<str:sk>/<int:mk>', views.approve, name='approve'),    
    path('<int:pk>/viewstudent/decline/<str:sk>/<int:mk>', views.decline, name='decline'),  
    path('<int:pk>/viewstudent/deletemem/<str:sk>/<int:mk>', views.deletemem, name='deletemem'),
    path('error', views.error, name='error'),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('token', views.token, name='token'),    
    path('createyear', views.createyear, name='createyear'),
    path('createbranch', views.createbranch, name='createbranch'),
]   