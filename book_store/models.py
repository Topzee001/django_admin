from django.db import models
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your models here.


# advanced model relationships
# practice exercises
# 1. using ForeignKey
class Department(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Employee(models.Model):
    name= models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
   
    def __str__(self):
        return self.name
# 2. using OneToOneField
class Product(models.Model):
    name= models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_publish_product", "can publish product")
        ]

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product = models.OneToOneField(Product, on_delete= models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
         # Truncate description to 30 characters for readability
        short_description = self.description[:30] + '...' if len(self.description) > 30 else self.description
        return f"{self.product.name} - ₦{self.price}"

# 3. using ManyToManyField

class Student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    student = models.ManyToManyField(Student, related_name='courses')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# 4.  Handling Related Object Deletion

# class Company(models.Model):
#     name = models.CharField(max_length=100)

# class Department(models.Model):
#     company = models.ForeignKey(
#         Company,
#         on_delete=models.SET_NULL,  # You can also try PROTECT, SET_DEFAULT, etc.
#         null=True,
#         blank=True
#     )
#     name = models.CharField(max_length=100)
# 5. Query Optimization using select_related and prefetch_related, meant to be in the views model and not hereee
#  selected_related: Use for ForeignKey and OneToOneField
# without selected, 1 query for employees, N queries for departments
# employees = Employee.objects.all()

# # Optimized, with eselected: 1 query total
# employees = Employee.objects.select_related('department')

# for emp in employees:
#     print(emp.name, emp.department.name)

# # prefetch_related: Use for ManyToManyField and reverse ForeignKeys
# # without prefetch: 1 query for courses, N query for students
# courses = Course.objects.all()

# # Optimized: 2 queries total
# courses = Course.objects.prefetch_related('student')

# for course in courses:
#     for student in course.student.all():
#         print(course.title, student.name)



# Basic models for a book store application existing code in the db
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title


# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=500)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

