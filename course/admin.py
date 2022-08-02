from django.contrib import admin
from course.models import Course, CourseAuthor, Category

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'author', 'category', 'level', 'status']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(CourseAuthor)
class CourseAuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

@admin.register(Category)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}