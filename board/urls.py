from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:pk>/', views.board_detail), # int형 값을 pk라는 변수명으로 받음 -> 이 변수는 view에서 사용
    path('list/', views.board_list),
    path('write/', views.board_write),
]
