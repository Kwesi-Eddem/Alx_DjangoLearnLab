# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm demonstrates how to build a form
    from the Book model with validation.
    """
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
