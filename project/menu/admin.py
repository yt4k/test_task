from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    list_editable = ('order',)
    fields = ('title', 'url', 'parent', 'menu_name', 'order')