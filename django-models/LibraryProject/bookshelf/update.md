
---

### 📄 `update.md`
```markdown
# Update the title of the Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
