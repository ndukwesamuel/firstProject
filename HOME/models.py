from django.db import models


# Create your models here.
from django.urls import reverse





class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return f'{self.author} ==> {self.title} '

    def get_absolute_url(self):
        return reverse("Detail", kwargs={"pk": self.pk})
    
    



    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

