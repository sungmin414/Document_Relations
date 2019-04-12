from django.db import models


class User1Manager(models.Manager):
    def nomal_users(self):
        # super().get_queryset()
        # 상위 클래스에서 정의한 '기본적으로' 돌려줄 QuerySet
        return super().get_queryset().filter(is_admin=False)
        # return User1.objects.filter(is_admin=False)

    def admin_users(self):
        return super().get_queryset().filter(is_admin=True)


class User1(models.Model):
    name = models.CharField('이름', max_length=40)
    is_admin = models.BooleanField('관리자', default=False)

    # 이 클래스에 커스텀 매니저를 적용
    objects = User1Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Inheritance_Proxy_User1'

    def find_user(self, name):
        return User1.objects.filter(name__contains=name)


class NormalUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=False)


class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class NomalUser(User1):
    objects = NormalUserManager()

    class Meta:
        proxy = True


class Admin(User1):
    objects = AdminUserManager()

    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()