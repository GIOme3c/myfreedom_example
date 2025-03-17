from django.urls import path
from book.views import BooksView, book, CreateBookView, edit_book, BookDetailView

арр_name = "books"

urlpatterns = [
    path('', BooksView.as_view(), name="books"), # books/
    path('<int:book_id>/', book, name="book"), # books/
    path('create/', CreateBookView.as_view(), name="create-book"), # books/
    path('edit/<int:book_id>/', edit_book, name="edit-book"), # books/
    # path('books/<int:pk>/', get_book, name='get_book'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='get_book'),
]