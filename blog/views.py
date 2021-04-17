from django.shortcuts import render,HttpResponse
from blog import models

# Create your views here.
def blogHome(request):
    allPosts = models.Post.objects.all()
    context = {'posts':allPosts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = models.Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogPost.html',context)



