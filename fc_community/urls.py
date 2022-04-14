"""fc_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), # admin은 기본적으로 들어가 있음, admin/ 하위에 있는 것, 즉 admin/이 붙는 url은 admin.site.urls와 연결
    path('fcuser/', include('fcuser.urls')) # 프로젝트 urls.py에 fcuser 관련 url 매핑 -> fcuser/ 하위 url은 fcuser 앱(폴더)의 urls.py를 참고한다
]
