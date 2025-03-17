from django.db import models
from django.contrib.auth.models import User
from author.models import Authors

class Profile(models.Model):
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, default=100)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    author = models.ForeignKey(Authors, on_delete=models.PROTECT, null=True, related_name="books")

    def __str__(self):
        return self.name+" "+str(self.price)

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ['-published']
        default_related_name = "books"


class History(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name="history")
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()

    class Meta:
        unique_together = ("profile", "book", "date_start", "date_end")
        # indexes = ("date_start", "date_end")