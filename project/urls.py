"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # api 통신 시 편리함을 위해 시작점을 api로 통일
    # 상세 url은 각 앱에서 다룸
    path('api/', include('accounts.urls')),
    path('api/', include('mypage.urls')),
    path('api/', include('album.urls')),
    path('api/', include('snap.urls')),
    path('api/', include('stretching.urls')),
    path('api/', include('tracking.urls')),
]
