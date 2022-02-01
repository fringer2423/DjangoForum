from rest_framework import serializers
from api.models import Checkbox
from django.contrib.auth.models import User


class CheckboxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
