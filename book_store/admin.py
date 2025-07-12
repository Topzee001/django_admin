from django.contrib import admin
from .models import Book, Product

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter= ('published_date',)
    ordering = ('-published_date',)
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Product)
