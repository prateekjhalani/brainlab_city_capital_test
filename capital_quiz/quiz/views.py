from django.shortcuts import render
import random
from .models import Country


def quiz(request):
    # Get a random country from the database
    random_country = random.choice(Country.objects.all())
    return render(request, 'quiz.html', {'country': random_country})
