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


class DataSerializers(serializers.Serializer):
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    attrs = serializers.JSONField(required=False)
    type = serializers.CharField(required=False)
    val_1 = serializers.IntegerField()
    val_2 = serializers.IntegerField()

    @staticmethod
    def validate_type(type):
        if not type in ["dict", "list", "tuple"]:
            raise serializers.ValidationError(f"{type} is not allowed")
        return type
