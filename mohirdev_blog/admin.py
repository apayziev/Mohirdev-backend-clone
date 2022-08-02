from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from mohirdev_blog.models import Post, PostAuthor, PostCategory, PostComment
# Register your models here.
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'author', 'category', 'created_at', 'updated_at']
    list_filter = ['author', 'category']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

@admin.register(PostAuthor)
class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "avatar"]
    search_fields = ["first_name", "last_name"]
    list_per_page = 10


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "post_count"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "post", "content", "created_at"]
    list_filter = ["user", "post"]
    search_fields = ["user__username", "post__title"]
    list_per_page = 10