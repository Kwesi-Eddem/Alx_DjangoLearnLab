from django.shortcuts import render
from rest_framework import generics, permissions, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title','author', 'publication_year']

    search_fields = ['title', 'author__name']
    
    ordering_fields = ['title','publication_year']
    ordering = ['title']

    def get_queryset(self):
        author_id = self.request.query_params.get('author')
        if author_id:
            return Book.objects.filter(author_id=author_id)
        return Book.objects.all()
    

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get('id') or self.request.query_params.get('id')
        return get_object_or_404(Book, pk=book_id)

class BookDeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        book_id = self.request.data.get('id') or self.request.query_params.get('id')
        return get_object_or_404(Book, pk=book_id)