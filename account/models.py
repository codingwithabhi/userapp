from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", blank=True)
    degree = models.CharField(max_length=30, blank=True)
    year_of_passing = models.CharField(max_length=30,blank=True)
    certificate = models.ImageField(upload_to="certificate", blank=True)
    short_desc = models.TextField(max_length=500, blank=True)
    long_desc = RichTextUploadingField(blank=True,null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()