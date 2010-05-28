=================
django-smart-slug
=================

slug fields for the lazy

Examples
--------

There are exhausting examples in the tests, but here's the quick rundown::

    from django.db import models
    from smart_slug.fields import SmartSlugField

    class Simple(models.Model):
        slug = SmartSlugField(max_length=5, underscores=False)

    class Complex(models.Model):
        title = models.CharField(max_length=100)
        slug = SmartSlugField(
            source_field='title',
            date_field='pub_date',
            split_on_words=True,
            max_length=10)
        pub_date = models.DateTimeField(auto_now=True)

    >>> s1 = Simple.objects.create(slug='simple')
    >>> s1.slug
    simpl

    >>> s2 = Simple.objects.create(slug='simple')
    >>> s2.slug
    sim-1

    >>> s3 = Simple.objects.create(slug='simple')
    >>> s3.slug
    sim-2

    >>> c1 = Complex.objects.create(title='complex example')
    >>> c1.slug
    complex

    >>> c2 = Complex.objects.create(title='complex example')
    >>> c2.slug
    complex_
