from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from blog import models
from django.contrib.auth import login, logout, authenticate
import pyrebase

# Create your views here.

# def get_user_name(self):
#     if self.first_name or self.last_name:
#         return self.first_name + " " + self.last_name
#     return self.username


config={
    "apiKey": "AIzaSyBfb25bhuyHKBF9BXnUklfH_HPyDLAEA5w",
    "authDomain": "firstdjangowebsite.firebaseapp.com",
    "projectId": "firstdjangowebsite",
    "storageBucket": "firstdjangowebsite.appspot.com",
    "messagingSenderId": "125474027497",
    "appId": "1:125474027497:web:e05c0de075a8ba7762bd78",
    "measurementId": "G-9Y38TW55PT",
    "databaseURL":"https://firstdjangowebsite-default-rtdb.firebaseio.com/"
}

firebase=pyrebase.initialize_app(config)
storage = firebase.storage()


def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<5:
            messages.warning(request,'Enter valid data.')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully.')    
    return render(request,'home/contact.html')

def search(request):
    query = request.GET['search']
    if len(query) > 50:
        posts = []
    else:
        postsTitle= models.Post.objects.filter(title__icontains=query)
        postContent = models.Post.objects.filter(content__icontains=query)
        posts = postsTitle.union(postContent)  
    if posts.count() == 0:
        messages.warning(request,"Please refine your query")
    context = {'posts':posts,
               'query':query}
    return render(request,'home/search.html', context)


def userSignUp(request):
    if request.method=='POST':
       username = request.POST.get('username')
       fname = request.POST.get('fname')
       lname = request.POST.get('lname')
       email = request.POST.get('email')
       password = request.POST.get('password')
       cpassword = request.POST.get('cpassword')
       if password != cpassword:
           messages.success(request,'Password and Confirm Password must be same.')
           return redirect('home')
       if User.objects.filter(email=email).first() is not None:
           messages.success(request,'This email has already taken please try another one.')
           return redirect('home')
       try:
           myuser = User.objects.create_user(username,email,password)
           myuser.first_name = fname
           myuser.last_name = lname
           myuser.save()
           messages.success(request,"Account has been created successfully.")
           return redirect('home')
       except Exception as e:
           messages.success(request,'This username has already taken please try another one.',e)
           return redirect('home')
    else:
        return HttpResponse('Not Found')
       
       
       
def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Successfully login")
            return redirect(home)
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('home')
    return HttpResponse('Not Found')
        
def userLogout(request):
    logout(request)
    messages.success(request,"Successfully logout")
    return redirect('home')
    
    
def writeBlog(request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user.get_full_name()
        username=request.user.get_username()
        slug  = request.POST.get('title').replace(" ","-")
        display_image = request.POST.get('display_image')
        post = models.Post(title=title,content=content,author=author,slug=slug,display_image=display_image,username=username)
        post.save()
        messages.success(request,'Thank you for writing blog,Your blog has been published successfully.')
    return render(request,'home/writeBlog.html')


def myposts(request):
    posts = models.Post.objects.filter(username=request.user.get_username())
    context = {'posts':posts}
    return render(request,'home/myposts.html',context)


def deletepost(request,sno):
    post = models.Post.objects.filter(sno=sno)
    print(sno)
    post.delete()
    
    messages.success(request,"Your post has been deleted.")
    return redirect('myposts')
    
def updatepost(request,sno):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        slug  = request.POST.get('title').replace(" ","-")
        display_image = request.POST.get('display_image')
        models.Post.objects.filter(sno=sno).update(title=title,content=content,slug=slug,display_image=display_image)
        messages.success(request,"Your blog has been updated..")
        return redirect('myposts')
    else:
        post = models.Post.objects.filter(sno=sno).first()
        context = {'post':post}
        return render(request,'home/updateblog.html',context)
   
def profile(request):
    return render(request,"home/profile.html")     
    