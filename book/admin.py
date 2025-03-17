from django.contrib import admin
from book.models import Book
from author.models import Authors

# Register your models here.
admin.site.register(Book)
admin.site.register(Authors)