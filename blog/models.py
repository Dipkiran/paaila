from django.conf import settings
from django.urls import reverse
from django.db import models




class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE,)
    title = models.CharField(max_length=120)
    image = models.FileField(null=True,blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_Date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"id":self.id})

    def get_url(self):
        return reverse("blog:update", kwargs={"id":self.id})

    def get_delete_url(self):
        return reverse("blog:delete", kwargs={"id":self.id})

    class Meta:
        ordering = ["-id", "-published_Date", "-updated"]
