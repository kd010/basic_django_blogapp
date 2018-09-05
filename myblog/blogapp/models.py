from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    created = models.DateTimeField()
    user = models.ForeignKey(User)
    title = models.TextField()
    b_text = models.TextField()
    like = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to = 'pictures/',null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField()
    blogid = models.ForeignKey(Blog)
    desc = models.TextField()
    like = models.IntegerField()
    

class Profile(models.Model):
    created = models.DateTimeField()
    user = models.ForeignKey(User)
    Add = models.TextField()
    Qual = models.TextField()
    mob = models.IntegerField()
    pro_image = models.ImageField(null=True)


