from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from helpers.pagination import CustomPagination
from course.models import Course, CourseAuthor, Category
from course.serializers import CourseSerializer

# Create your views here.
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['title']
    filterset_fields = ['is_new']




    