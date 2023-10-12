from django.urls import path
from . import views
app_name = 'libraries'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:book_num>/',views.detail,name='detail'),
    path('<int:book_num>/review_create/',views.review_create,name='review_create'),
    path('<int:book_num>/comments/<int:review_num>/delete',views.review_delete,name='review_delete'),
]
