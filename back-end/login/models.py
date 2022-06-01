from django.db import models

class Role(models.Model):
    description = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    users_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'role'


class Users(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    student_number = models.CharField(unique=True, max_length=45)
    nickname = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    major = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'