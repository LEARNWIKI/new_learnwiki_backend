from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators


# Create your models here.
class Node(models.Model):
    x = models.IntegerField(verbose_name="X координата", default=0, blank=True)
    y = models.IntegerField(verbose_name="Y координата", default=0, blank=True)
    type_node = models.CharField(verbose_name="Тип", max_length=255)
    label = models.CharField(verbose_name="Текст", max_length=255)

    def __str__(self) -> str:
        return f'Нода: {self.label}, {self.x}, {self.y} '

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"


class Link(models.Model):
    from_links = models.ForeignKey(Node, verbose_name="From",
                                   related_name="from_links", on_delete=models.CASCADE)
    to = models.ForeignKey(Node, verbose_name="To",
                           related_name="tolinks", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"
