from rest_framework import generics
from ..models import Teacher, Object
from .serializers import TeacherSerializers, ObjectSerializers

class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class TeacherDetail(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class ObjectList(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializers

class ObjectDetail(generics.RetrieveAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializers

class TeacherSearch(generics.ListAPIView):
    serializer_class = TeacherSerializers

    def get_queryset(self):
        name_tea = self.request.GET.get('name_tea')
        address = self.request.GET.get('address')

        teachers = Teacher.objects.all()
        if name_tea:
            teachers = teachers.filter(name_tea=name_tea)
        if address:
            teachers = teachers.filter(addres=address)
        return teachers

class TeacherUpdate(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

class TeacherDelete(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

