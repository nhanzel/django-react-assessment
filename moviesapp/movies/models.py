# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)

    RATED_VALUES = (
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
        ("Not Rated", "Not Rated (NR)")
    )
    rated = models.CharField(max_length=64, choices=RATED_VALUES)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    average_rating = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.id})

class Review(models.Model):
    reviewer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL)

    RATING_VALUES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
    )

    rating = models.PositiveIntegerField(null=True, choices=RATING_VALUES)
    review = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.reviewer.username + ": " + self.movie.title