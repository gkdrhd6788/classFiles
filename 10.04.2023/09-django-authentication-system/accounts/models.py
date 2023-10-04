from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass  # pass로 두고 필요한 순간에 필드를 수정(장고와의 약속)

