from .models import *

#this is used to get the average rating for a given movie (checking that it has reviews)
def calculateRating(id):
    if Review.objects.all().exists():
        all_reviews = Review.objects.all()
        if all_reviews.filter(movie__id=id).exists():
            reviews = Review.objects.filter(movie__id=id)
            average_score = 0.0
            for review in reviews:
                average_score += review.rating
            average_score = (average_score)/(reviews.count())
            return average_score
    else:
        return "N/A"