from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import ListView
from django.views import View

from book.models import Book
from book.forms import BookForm
from django.views.decorators.cache import cache_page


class BooksView(ListView):
    model = Book


@cache_page(27*60)
def book(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, 'book/book.html', {"book": book})


class CreateBookView(View):
    def get(self, request):
        form = BookForm()

        return render(request, "book/create_book.html", {"form": form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("book", book_id=book.pk)


def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book", book_id=book.pk)
    else:
        form = BookForm(instance=book)

    return render(request, "book/edit_book.html", {"form": form, "book": book})


from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from book.serializers import BookSerializer
from rest_framework.views import APIView


# class BookDetailView(APIView):
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)

#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     def patch(self, request, pk):
        
#         book = Book.objects.get(pk=pk)

        # serializer = BookSerializer(book, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
