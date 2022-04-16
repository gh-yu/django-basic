from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register), # register/라는 url과 views.py의 함수를 연결해준다 (fcuser/register/)
    path('login/', views.login), # login/ url 들어오면 views의 login함수 호출
    path('logout/', views.logout),
]
