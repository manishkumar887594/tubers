from django.contrib import admin
from .models import Slider,Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="50" />'.format(object.photo.url))

    list_display=('id','myphoto','first_name','Role','created_date')
    list_display_links=('first_name','id')
    search_fields=('first_name','Role')
    list_filter=('Role',)


admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)
