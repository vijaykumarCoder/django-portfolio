
from django.core import paginator
from .filter import PostFilter
from django.conf.urls import url
from .forms import ImageForm, PostForm
from .models import Image, Post
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
    posts = Post.objects.all()
    posts = Post.objects.order_by("-id")[:2]
    context = { 'posts': posts}
    return render(request,"base/index.html",context)
def posts(request):
   # posts = Post.objects.all()
    posts = Post.objects.order_by("-id")[:2]
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = { 'posts': posts, "myFilter": myFilter}
    return render(request,"base/posts.html",context)

def post(request):
    return render(request,"base/post.html")

def profile(request):
    return render(request,"base/profile.html")

def uploadImage(request):
    form = ImageForm()
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance

            context = {'form': form, "img_obj": img_obj}
            return render(request, "base/uploadImage.html",context)
    
    context = {'form': form}
    return render(request, "base/uploadImage.html",context)

@login_required(login_url="home")
def postForm(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect("posts")

    context  =  { "form": form}
    return render(request, "base/post_form.html",context)

def updatePost(request,pk):
    postData = Post.objects.get(id=pk)
    form = PostForm(instance=postData)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=postData)
        if form.is_valid():
            form.save()
        return redirect("posts")
    
    context = { "form": form}

    return render(request, "base/post_form.html",context)

def deletePost(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    context ={}
    return render(request, "base/delete.html",context)



#paginators here
def pagePage(request):
    objects = []
    for i in range(55):
        objects.append(i)
    
    p = Paginator(objects, 10)
    page_num = request.GET.get('page',1)
    try: 
        objects = p.page(page_num)
    except EmptyPage:
        objects = p.page(1)
    context = {"objects":objects}
    return render(request, 'base/pagintor.html', context)

