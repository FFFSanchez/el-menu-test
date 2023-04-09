from django.contrib import admin
from menu.models import MenuCategories


class MenuCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'explicit_url')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'

    class Meta:
        order_by = 'explicit_url'


admin.site.register(MenuCategories, MenuCategoriesAdmin)
