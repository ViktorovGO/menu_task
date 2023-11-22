from django.contrib import admin

from .models import MenuItem, Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'level', 'menu_name')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)
    # prepopulated_fields = {'url':('title',)} 
    ordering = ('menu_name',)
    exclude = ('level', 'url',)

admin.site.register(MenuItem, MenuAdmin)
admin.site.register(Menu)
