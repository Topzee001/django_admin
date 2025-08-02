from django.contrib import admin
from .models import Book, Product, Department, Employee, Course, ProductDetail, Student, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date',)
    search_fields = ('title', 'author',)
    list_filter= ('published_date',)
    ordering = ('-published_date',)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # fields to display the admin list view
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_superuser')

    # fields to search by
    search_fields = ('email',)

    # How records are ordered
    ordering = ('email',)

    # fieldsets for editing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {'fields': ('date_of_birth', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('importamt dates', {'fields': ('last_login',)}),
    )

    # Fieldsets for adding new users
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'full_name', 'date_of_birth', 'profile_picture', 'password1', 'password2', 'is_staff', 'is_superuser'),
    }),
)


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(ProductDetail)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(CustomUser, CustomUserAdmin)
