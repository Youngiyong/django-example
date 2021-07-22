from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, help_text="이름")
    password = models.CharField(max_length=128, help_text="패스워드")
    email = models.CharField(max_length=45, help_text="이메일")
    phone = models.CharField(max_length=20, help_text="전화번호")
    is_active = models.SmallIntegerField(help_text="활동 상태")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, help_text="생성일")
    updated_at = models.DateTimeField(blank=True, null=True, help_text="변경일")
    deleted_at = models.DateTimeField(blank=True, null=True, help_text="삭제일")

    class Meta:
        db_table = 'members'
#
class Boards(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, help_text="제목")
    content = models.CharField(max_length=1000, help_text="본문내용")
    users = models.ForeignKey('Users',on_delete=models.DO_NOTHING, null=True, help_text="유저 아이디")

    class Meta:
        db_table = 'boards'

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, help_text="제목")
    content = models.CharField(max_length=1000, help_text="본문내용")
    users = models.ForeignKey('Users', on_delete=models.DO_NOTHING, null=True, help_text="유저 아이디")
    boards = models.ForeignKey('Boards', on_delete=models.DO_NOTHING, null=True, help_text="보드 아이디")

    class Meta:
        db_table = 'comments'