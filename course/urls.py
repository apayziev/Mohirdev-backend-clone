from django.urls import path
from course.views import CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="courses-list"),
]