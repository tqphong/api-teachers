from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', TeacherList.as_view(), name='teacher-list'),
    path('<int:pk>', TeacherDetail.as_view(), name='teacher-detail'),
    path('update/<int:pk>/', TeacherUpdate.as_view(), name='teacher-update'),
    path('delete/<int:pk>/', TeacherDelete.as_view(), name='teacher-delete'),
    path('object/', ObjectList.as_view(), name='object-list'),
    path('object/<int:pk>', ObjectDetail.as_view(), name='object-detail'),
    url(r'search', TeacherSearch.as_view(), name='teacher-search')

]

urlpatterns = format_suffix_patterns(urlpatterns)