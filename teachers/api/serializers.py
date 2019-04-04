from rest_framework import serializers
from ..models import Teacher, Object


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name_tea', 'address']


class ObjectSerializers(serializers.ModelSerializer):
    teach = serializers.SerializerMethodField()

    class Meta:
        model = Object
        fields = ['id', 'teach', 'name_obj', 'credit',]

    def get_teach(self, obj):
        return obj.teach.name_tea