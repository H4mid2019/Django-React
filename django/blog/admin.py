from django.contrib import admin
from .models import Post, Writer

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'brief', 'tags')
    ordering = ('title',)
    search_fields = ('title', 'brief', 'tags')
    fieldsets = (
      ('Standard info', {'fields': ('title', 'brief')}),
      ('Second Part', {'fields': ('subtitle', 'slug','article','ff')}),
      ('Address info', {'fields': ('imag', ('tags'))}),
   )


admin.site.register(Post, PostAdmin)


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
