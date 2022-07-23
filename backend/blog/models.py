from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils.translation import gettext_lazy as _

# Create your models here.

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """
    Blog post model.

    Title, slug, content and author are required. All other fields are defaults.

    Title and slug are unique.
    """

    title = models.CharField(_("Title"), max_length=300, unique=True)
    slug = models.SlugField(_("Slug Field"), max_length=300, unique=True)
    content = QuillField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    status = models.IntegerField(_("Status"), choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return str(self.title)


class Profile(models.Model):
    """
    User profile for registered users of the blog site.

    User field is the only required field.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)
    github = models.CharField(max_length=300, blank=True, null=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class Comment(models.Model):
    """
    Blog comment model.

    User, content, and post are required. Other fields are optional.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user) + " Comment: " + str(self.content)
