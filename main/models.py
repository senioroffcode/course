from django.db import models
from  django.contrib.auth.models import AbstractUser

class Direction(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    payment = models.DecimalField(decimal_places=2, max_digits=25)

    def __str__(self):
        return self.name

class User(AbstractUser):
    status = models.IntegerField(choices=(
        (1, 'mentor'),
        (2, 'reception'),
        (3, 'accountant'),
        (4, 'director'),
    ), null=True, blank=True)
    phone = models.CharField(max_length=555, null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    status = models.IntegerField(choices=(
        (1, 'active'),
        (2, 'in_group'),
        (3, 'leave'),
        (4, 'graduated'),
        (5, 'passive'),
    ), default=1)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    extra_phone = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(max_length=255)
    debt = models.DecimalField(decimal_places=2, max_digits=25)


class Group(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    created_at = models.CharField(max_length=255)


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    money = models.DecimalField(decimal_places=2, max_digits=25)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


