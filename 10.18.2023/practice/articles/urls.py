from django.urls import path
from . import views

urlpatterns = [
    # 게시글 전체 조회 및 게시글 생성
    path('articles/',views.article_list_or_create),
    # 게시글 상세 조회, 삭제, 수정
    path('articles/<int:article_pk>/',views.article_detail_or_delete_or_update),

]