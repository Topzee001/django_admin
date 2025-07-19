from django.contrib import admin
from .models import Book, Product, Department, Employee, Course, ProductDetail, Student

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter= ('published_date',)
    ordering = ('-published_date',)
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(ProductDetail)
admin.site.register(Student)
admin.site.register(Course)
