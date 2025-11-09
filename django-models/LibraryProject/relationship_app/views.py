from django.shortcuts import render
from django.views.generic.detail import DetailView
# Create your views here.
from .models import *

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


