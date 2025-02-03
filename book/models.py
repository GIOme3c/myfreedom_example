from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name+" "+str(self.price)

    class Meta:
        verbose_name_plural = "Книги"
        verbose_name = "Книга"
        ordering = ['-published']
