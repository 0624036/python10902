from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

from mainsite.models import Post, Visitor_202105, Visitor_202104, Visitor_202103, Visitor_202102, Visitor_202101

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())

def logout(request):
    auth.logout(request)
    return redirect("/")

def show202105(request):
    try:
        visitor_data = Visitor_202105.objects.all()
        title_date = "2021年05月份" 
    except:
        return redirect('/')
    return render(request, "202105.html", locals())

def show202104(request):
    try:
        visitor_data = Visitor_202104.objects.all()
        title_date = "2021年04月份" 
    except:
        return redirect('/')
    return render(request, "202104.html", locals())

def show202103(request):
    try:
        visitor_data = Visitor_202103.objects.all()
        title_date = "2021年03月份" 
    except:
        return redirect('/')
    return render(request, "202103.html", locals())

def show202102(request):
    try:
        visitor_data = Visitor_202102.objects.all()
        title_date = "2021年02月份" 
    except:
        return redirect('/')
    return render(request, "202102.html", locals())

def show202101(request):
    try:
        visitor_data = Visitor_202101.objects.all()
        title_date = "2021年01月份" 
    except:
        return redirect('/')
    return render(request, "202101.html", locals())

def show202105draw(request):
    try:
        visitor_data = Visitor_202105.objects.all()
        title_date = "2021年05月份" 
    except:
        return redirect('/')
    return render(request, "202105draw.html", locals())

def show202104draw(request):
    try:
        visitor_data = Visitor_202104.objects.all()
        title_date = "2021年04月份" 
    except:
        return redirect('/')
    return render(request, "202104draw.html", locals())

def show202103draw(request):
    try:
        visitor_data = Visitor_202103.objects.all()
        title_date = "2021年03月份" 
    except:
        return redirect('/')
    return render(request, "202103draw.html", locals())

def show202102draw(request):
    try:
        visitor_data = Visitor_202102.objects.all()
        title_date = "2021年02月份" 
    except:
        return redirect('/')
    return render(request, "202102draw.html", locals())

def show202101draw(request):
    try:
        visitor_data = Visitor_202101.objects.all()
        title_date = "2021年01月份" 
    except:
        return redirect('/')
    return render(request, "202101draw.html", locals())
"""
def show(request, id):
    try:
        switch={
        202101: case1,
        202102: case2,
        202103: case3,
        202104: case4,
        202105: case5
        }
        switch[id]()
    except:
        return redirect('/')
    return render(request, "show.html", locals())
"""
"""
def rank(request):
    cities = City.objects.all()
    return render(request, "rank.html", locals())
"""
"""
def case1():
    visitor_data = Visitor_202101.objects.all()
    title_date = "2021年01月份" 
    pass
def case2():
    visitor_data = Visitor_202102.objects.all()
    title_date = "2021年02月份" 
    pass
def case3():
    visitor_data = Visitor_202103.objects.all()
    title_date = "2021年03月份" 
    pass
def case4():
    visitor_data = Visitor_202104.objects.all()
    title_date = "2021年04月份" 
    pass
def case5():
    visitor_data = Visitor_202105.objects.all()
    title_date = "2021年05月份" 
    pass
"""

