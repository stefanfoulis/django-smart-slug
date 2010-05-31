from django.db import models

from smart_slug.fields import SmartSlugField

class Simple(models.Model):
    slug = SmartSlugField(max_length=5)

class Complex(models.Model):
    title = models.CharField(max_length=100)
    slug = SmartSlugField(
        source_field='title',
        date_field='pub_date',
        split_on_words=True,
        max_length=10)
    pub_date = models.DateTimeField()

class UnderscoresNumerals(models.Model):
    slug_underscores = SmartSlugField(max_length=10)
    slug_numerals = SmartSlugField(underscores=False, max_length=10)
