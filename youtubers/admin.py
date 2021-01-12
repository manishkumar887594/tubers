from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.
class ytubeAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="50" />'.format(object.photo.url))

    list_display=('id','name','myphoto','subs_count','is_featured')
    searcfield=('name','camera_type')
    list_filter=('city','camera_type')
    list_display_links=('id','name')
    list_editable=('is_featured',)

admin.site.register(Youtuber,ytubeAdmin)
