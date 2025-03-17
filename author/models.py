from django.db import models

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