from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class TimeStampMixin(models.Model):
    """Реализация атрибутов времени создания и обновления записи"""

    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        abstract = True


class Ingredient(TimeStampMixin):
    """Ингредиенты для рецепта"""

    name = models.CharField("Название", max_length=40, null=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "bookCook"
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Recipe(TimeStampMixin):
    """ Рецепт """
    name = models.CharField('Назвение', max_length=40, null=False)
    text = models.TextField('Описание', null=False)
    cooking_time = models.IntegerField('Время приготовления', null=False)
    type_of_kitchen = models.CharField("Тип кухни", max_length=40, null=False)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "bookCook"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"