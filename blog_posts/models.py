from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import redirect
from django.db import models


class BlogPost(models.Model):
  title       = models.CharField(max_length=300)
  slug        = models.SlugField('id_url', unique=True)
  upload_date = models.DateTimeField(default=datetime.now)
  description = models.CharField(max_length=500)
  article     = RichTextUploadingField()
  image       = models.ImageField(upload_to='photos/blog_post/%Y/%m/%d/')
  image_alt   = models.CharField(max_length=300)


  def get_absolute_url(self):
    return redirect('/post/%s' % self.slug)
