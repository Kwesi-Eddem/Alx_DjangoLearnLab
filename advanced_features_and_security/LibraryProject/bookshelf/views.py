from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to list all books with permission check
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})