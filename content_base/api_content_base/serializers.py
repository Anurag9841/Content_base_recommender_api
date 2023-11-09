from rest_framework import serializers
from .models import tag,preprocessedcourse

class tagSerializers(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'

class preprocessedcourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = preprocessedcourse
        fields = '__all__'



