# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics


from .models import Movie, Review
from .helpers import calculateRating
from .filters import MovieFilter
from .serializers import MovieSerializer

"""Movies views."""

class MovieListView(generics.ListCreateAPIView):
    """Show all movies."""
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class MovieDetailView(LoginRequiredMixin, DetailView):
    """Show the requested movie."""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    
class MovieCreateView(LoginRequiredMixin, CreateView):
    """Create a new movie."""

    model = Movie
    template_name = '../templates/movies/movie_form.html'

    fields = ['title', 'year', 'rated', 'released_on', 'genre', 'director', 'plot']

    def get_context_data(self, **kwargs):   
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['success'] = True
        return context

    def form_valid(self, form):
        messages.success(self.request, "The movie has been successfully created!")
        response = super().form_valid(form)
        print("THIS IS HAPPENING")
        print("THE RESPONSE CODE IS SET")
        return response
    
    def form_invalid(self, form):
        messages.info(self.request, "The creation has failed")
        return super().form_valid(form)

    def get_success_url(self):
        print("HOPEFULLY THIS HAPPENS")
        return '/movies/' + str(self.object.id) + '/'


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    """Update the requested movie."""

    model = Movie
    template_name = '../templates/movies/movie_form.html'

    fields = ['title', 'year', 'rated', 'released_on', 'genre', 'director', 'plot']

    def get_success_url(self):
        return '/movies/' + str(self.object.id) + '/'

    def form_valid(self, form):
        messages.success(self.request, "The movie has been successfully updated!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(request, "The update has failed.")
    

class MovieDeleteView(LoginRequiredMixin, DeleteView):
    """Delete the requested movie."""

    model = Movie
    template_name = '../templates/movies/movie_confirm_delete.html'

    success_url = '/movies'

    def form_valid(self, form):
        messages.success(self.request, "The movie has been successfully deleted!")
        return super().form_valid(form)

class MovieReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = '../templates/movies/movie_reviews.html'

    fields = ['movie', 'rating', 'review']

    def get_context_data(self, *args, **kwargs):
        context = super(MovieReviewView, self).get_context_data(*args, **kwargs)
        context["reviewer"] = User

        return context

    def get_success_url(self):
        return '/movies/' + str(self.object.movie.id) + '/'
