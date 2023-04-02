from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    title = models.CharField(max_length=128, unique=True, verbose_name='Пункт меню')
    slug = models.SlugField(max_length=128, unique=True, verbose_name='Slug', primary_key=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родитель')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title









