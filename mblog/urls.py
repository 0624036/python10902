"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainsite.views import index, show202105, show202104, show202103, show202102, show202101, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('202105/', show202105),
    path('202104/', show202104),
    path('202103/', show202103),
    path('202102/', show202102),
    path('202101/', show202101),
    path('logout/', logout),
    path('', index),
]
