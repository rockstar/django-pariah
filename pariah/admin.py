from django.contrib import admin

from pariah import models


class ComicPostAdmin(admin.ModelAdmin):
    '''Admin for `pariah.models.ComicPost`'''
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'published'
    fields = ('title', 'image', 'published')
    list_display = ('title', 'published')
    search_fields = ('title',)

admin.site.register(models.ComicPost, ComicPostAdmin)
