from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="tester", password="password123")
        self.client = APIClient()

        # Create sample author and books
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

    # ---------- CRUD TESTS ----------

    def test_list_books(self):
        """Ensure /books/ returns all books with status 200."""
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_authentication(self):
        """Unauthenticated users cannot create books."""
        response = self.client.post("/books/create/", {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated users can create books."""
        self.client.login(username="tester", password="password123")
        response = self.client.post("/books/create/", {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        """Authenticated users can update books."""
        self.client.login(username="tester", password="password123")
        response = self.client.put("/books/update/", {
            "id": self.book1.id,
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete books."""
        self.client.login(username="tester", password="password123")
        response = self.client.delete("/books/delete/", {"id": self.book2.id})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- FILTERING / SEARCH / ORDERING ----------

    def test_filter_books_by_year(self):
        """Filter books by publication_year."""
        response = self.client.get("/books/?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        """Search books by title."""
        response = self.client.get("/books/?search=Animal")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_year_desc(self):
        """Order books by publication_year descending."""
        response = self.client.get("/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
