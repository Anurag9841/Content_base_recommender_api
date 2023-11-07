from rest_framework import serializers
from .models import tag

class tagSerializers(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'
