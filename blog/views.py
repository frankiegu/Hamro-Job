from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.


def blog(request):
    context = {
        'blog': Blog.objects.all()[:3],
    }
    return render(request, 'blog.html', context)


def blog_details(request, id):
    blog = {
        'single_blog': Blog.objects.get(id=id),
    }
    return render(request, 'blog_details.html', blog)

# Create your views here.
