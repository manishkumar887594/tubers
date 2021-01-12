from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):

    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices=(
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('panasonic','panasonic'),
        ('other','other'),
    )

    category_choices=(
        ('code','code'),
        ('review','review'),
        ('gaming','gaming'),
        ('comedy','comedy'),
        ('vlogs','vlogs'),
    )


    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%y/%m/')
    video_url=models.CharField(max_length=255)
    descrription=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    height=models.IntegerField()
    crew=models.CharField(choices=crew_choices,max_length=255)
    camera_type=models.CharField(choices=camera_choices,max_length=255)
    subs_count=models.CharField(max_length=255)
    category=models.CharField(choices=category_choices,max_length=255)
    is_featured=models.BooleanField(default=False)
    create_date=models.DateTimeField(default=datetime.now,blank=True)