from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.models import BaseModel
from common.models import User


# Create your models here.
class PostCategory(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"


class PostAuthor(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to="blog/author/avatar", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Post(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    content = RichTextUploadingField()
    author = models.ForeignKey(PostAuthor, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PostComment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    

    def __str__(self):
        return f"{self.user} - {self.post}"

    class Meta:
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"


