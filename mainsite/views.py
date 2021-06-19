from django.shortcuts import render
from django.http import HttpResponse
from mainsite.models import Post

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())
