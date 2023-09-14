from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    title = models.CharField(max_length=10)  # model 모듈의 CharField클래스의 인스턴스(Article의 변수)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
