from django.urls import path
from .views import CheckQuizResponse

# api url to check user submission answer
urlpatterns = [
    path('check_answer/', CheckQuizResponse.as_view({'post': 'create'}), name='check_answer'),
]
