from django.db import models
from accounts.models import CustomUser
from publications.choices import POSITION

# Create your models here.

class Bio(models.Model):
    bio = models.TextField(blank=True, null=True)
    career = models.TextField()
    name = models.CharField(max_length=255)
    
    position = models.IntegerField(choices=POSITION, default=1, null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    email_list = models.TextField()
    # image = models.ImageField(upload_to='bio_images/', null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING, related_name='bio', null=True, blank=True)

    def __str__(self):
        return self.name
