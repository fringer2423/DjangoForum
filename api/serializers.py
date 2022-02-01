from rest_framework import serializers
from api.models import Checkbox


class CheckboxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkbox
        fields = '__all__'
