from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('profile',views.profile,name="profile"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name="search"),
    path('signUp',views.userSignUp,name="signUp"),
    path('login',views.userLogin,name="login"),
    path('logout',views.userLogout,name="logout"),
    path('writeblog',views.writeBlog,name="writeblog"),
    path('myposts',views.myposts,name="myposts"),
    path('myposts/<int:sno>/delete',views.deletepost,name="deletepost"),
    path('myposts/<int:sno>/update',views.updatepost,name="updatepost"),
    
]