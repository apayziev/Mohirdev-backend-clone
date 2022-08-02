from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from helpers.models import BaseModel
from common.models import User

# Create your models here.
COURSE_LEVEL = (
    ("beginner", "Beginner"),
    ("intermediate", "Intermediate"),
    ("advanced", "Advanced"),
    ("expert", "Expert"),
    ("all levels", "All Levels"),
)


COURSE_STATUS = (
    ("bepul", "Bepul"),
    ("pullik", "Pullik"),
)


class CourseAuthor(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    avatar = models.ImageField(upload_to="course/author/avatar", blank=True, null=True)
    background = models.ImageField(
        upload_to="course/author/background", blank=True, null=True
    )

    # social account links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Course Author"
        verbose_name_plural = "Course Authors"


class Category(BaseModel):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    image = models.ImageField(upload_to="category_images", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    what_to_learn = models.TextField(
        blank=True, null=True, verbose_name="What to learn?"
    )
    requirements = models.TextField(blank=True, null=True, verbose_name="Requirements")

    image = models.ImageField(
        upload_to="course_images", null=True, blank=True, verbose_name="Course Image"
    )

    level = models.CharField(
        max_length=255, choices=COURSE_LEVEL, verbose_name="Course Level"
    )
    price = models.IntegerField(default=0)

    status = models.CharField(max_length=255, choices=COURSE_STATUS,
                default="bepul", verbose_name="Course Status")
    author = models.ForeignKey(
        CourseAuthor, on_delete=models.CASCADE, related_name="courses"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="courses"
    )

    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class CourseSection(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    order_number = models.IntegerField(default=0)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course Section"
        verbose_name_plural = "Course Sections"


class CourseLesson(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    section = models.ForeignKey(
        CourseSection, on_delete=models.CASCADE, related_name="lessons"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course Lesson"
        verbose_name_plural = "Course Lessons"


class CourseReview(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = "Course Review"
        verbose_name_plural = "Course Reviews"


# class CourseEnrollment(BaseModel):
#     course = models.ForeignKey(
#         Course, on_delete=models.CASCADE, related_name="enrollments"
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")

#     def __str__(self):
#         return f"{self.user} - {self.course}"

#     class Meta:
#         verbose_name = "Course Enrollment"
#         verbose_name_plural = "Course Enrollments"


# class CourseProgress(BaseModel):
#     pass
