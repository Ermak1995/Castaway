from django.contrib import admin
from .models import Episodes, Tags

# admin.site.register(Episodes)
admin.site.register(Tags)

@admin.register(Episodes)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}  # автоматическое создание slugа
