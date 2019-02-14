from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.CharField(max_length=8, primary_key=True, verbose_name='用户id')
    user_name = models.CharField(max_length=11, verbose_name='登录名')
    password = models.CharField(max_length=128, verbose_name='密码')
    slat = models.CharField(max_length=20, verbose_name='盐')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.user_name



