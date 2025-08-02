from django.contrib import messages
from django.http import HttpResponse
# imports for function-based view
from django.shortcuts import redirect, render
from .models import Book, Student
# import for class-based view
from django.views.generic import TemplateView, DetailView, UpdateView
from django.urls import reverse_lazy
# passing view to template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect


def intro(request):
    return HttpResponse("welcome to my book store.")

# Create your views here.
# function-based view
def index(request):
    books = Book.objects.all()

    context = {'book_list': books} #create a context dic with book list

    return render(request, 'books/book_list.html', context)

# class-based view

class HelloView(TemplateView):
     """A class-based view rendering a template named 'hello.html'."""
     template_name = 'hello.html'

class BookDetailView(DetailView):
     """A class-based view for displaying details of a specific book."""
     model = Book
     template_name = 'book/book_detail.html'

     def get_context_data(self, **kwargs):
          """Injects additional context data specific to the book."""
          context = super().get_context_data(**kwargs)
          book = self.get_object()
          context['average_rating'] = book.get_average_rating()
          return context

class BookUpdateView(UpdateView):
       """A class-based view for updating details of a specific book."""
       model = Book
       fields = ['title', 'author', 'description'] # Specify fields to be editable
       template_name = 'book/book_update_form.html'
       success_url = reverse_lazy('book_list') # URL to redirect after successful update

       def form_valid(self, form):
             """Executes custom logic after form validation."""
             response = super().form_valid(form) # Call default form validation
    # Perform additional actions after successful update (e.g., send notifications)
             return response
    
# practice exercise for views and url
# Create a function-based view that displays a simple message

def task(request):
     return HttpResponse("this is just what's needed from the task")

# Implement a class-based view that renders a template
class greeting(TemplateView):
    #  ensure to provide proper template directory location
     template_name = 'book/greeting.html'

# template task 
def home(request):
    context = {
        'name': 'Temitope',
        'items': ['Django', 'Python', 'Flutter']
    }
    return render(request, 'home.html', context)

@login_required
def profile_view(request):
    #  this view can only be accessed by authenticated users
    return render(request, 'accounts/profile.html')


# class ProfileView(LoginRequiredMixin, TemplateView):
#  # A protected view that displays the user's profile page, class based, fxn based above
#     template_name = 'accounts/profile.html'


# signup view
# authentication class
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name= 'registration/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully! You can now log in.")
        return super().form_valid(form)

#  user registration

def register(request):
     if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login') # redirect after successful registration
     else:
          form = CustomUserCreationForm()
     return render(request, 'registration/register.html', {'form': form})

# User = get_user_model()
# user = User.objects.get(email='tope@gmail.com')  # Change to target user
# permission = Permission.objects.get(codename='can_approve_book')
# user.user_permissions.add(permission)
@permission_required('book_store.can_approve_student', raise_exception=True)
def approve_student_view(request, student_id):
    # student = get_object_or_404(Student, id=student_id)
    # student.is_approved = True
    # student.save()
    # return redirect('student_list')  # or any page you want
    return render(request, 'approve_student.html', {'student_id': student_id})

