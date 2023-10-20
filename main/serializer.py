from rest_framework import serializers
from .models import *

class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',  'first_name', 'last_name', 'direction', 'phone', 'status']

class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"

class StudentSerializers(serializers.ModelSerializer):
    direction = DirectionSerializer(read_only=True)
    region = RegionSerializers(read_only=True)
    class Meta:
        model = Student
        fields = "__all__"

class GroupSerializers(serializers.ModelSerializer):
    students = StudentSerializers(read_only=True, many=True)
    mentor = UserSerializers(read_only=True)
    direction = DirectionSerializer(read_only=True)
    class Meta:
        model = Group
        fields = "__all__"

class PaymentSerializers(serializers.ModelSerializer):
    students = StudentSerializers(read_only=True)
    group = GroupSerializers(read_only=True)
    class Meta:
        model = Payment
        fields = "__all__"
