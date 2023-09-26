# articles/urls.py
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # 게시글 전체 조회 /articles/
    path('', views.index,name='index'),
    # 게시글 상세 조회 /articles/i/
    path('<int:article_pk>/', views.detail, name='detail'),
    # # 게시글 작성 폼 요청
    # path('new/', views.new, name='new'),
    # 게시글 생성 요청
    path('create/', views.create, name='create'),
]
