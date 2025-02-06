from django.db import models
from django.contrib.auth.models import User


class Authors(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, null=True, blank=True)
    birthdate = models.DateTimeField()
    deathdate = models.DateTimeField(null=True, blank=True)

    bio = models.TextField(null=True, blank=True, verbose_name="Биография")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = "Автор"

    @property
    def fio(self):
        return self.name+" "+self.patronymic+" "+self.surname


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    price = models.FloatField(null=True, blank=True, default=100)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    author = models.ForeignKey(Authors, on_delete=models.PROTECT, null=True, to_field="")

    def __str__(self):
        return self.name+" "+str(self.price)

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ['-published']
        default_related_name = "books"


class History(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()

    class Meta:
        unique_together = ("profile", "book", "date_start", "date_end")
        # indexes = ("date_start", "date_end")