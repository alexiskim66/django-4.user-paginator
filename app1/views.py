from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogForm
from .models import Pictures ##

def home(request):
    blogs = Blog.objects.all()
    picture = Pictures.objects ##
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts, 'picture':picture})

# def thumbnail(request):
#     picture = Pictures.objects ##
#     return render(request, 'home.html', {'picture':picture})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

# def new(request):
#     form = BlogForm()
#     return render(request, 'new.html', {'form':form})

# def create(request):
#     form = BlogForm(request.POST, request.FILES)
#     if form.is_valid():
#         new_blog = form.save(commit=False)
#         new_blog.date = timezone.now()
#         new_blog.save()
#         return redirect('detail', new_blog.id)
#     return redirect('home')

# def edit(request, id):
#     edit_blog = Blog.objects.get(id=id)
#     return render(request, 'edit.html', {'blog':edit_blog})

# def update(request, id):
#     update_blog = Blog.objects.get(id=id)
#     update_blog.subject = request.POST['subject']
#     update_blog.author = request.POST['author']
#     update_blog.content = request.POST['content']
#     update_blog.date = timezone.now()
#     update_blog.save()
#     return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')

def new(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.date = timezone.now()
            blog.save()
            return redirect('home')
    else:
        blog_form = BlogForm()
        return render(request, 'new.html', {'blog_form':blog_form})

def edit(request, id):
    blog = get_object_or_404(Blog, pk=id)
    if request.method == 'GET':
        blog_form = BlogForm(instance=blog)
        return render(request, 'edit.html', {'edit_blog':blog_form})
    else:
        blog_form = BlogForm(request.POST, request.FILES, instance=blog)
        if blog_form.is_valid():
            blog = blog_form.save(commit=False)
            blog.date = timezone.now()
            blog.save()
        return redirect('/app1/' + str(id))