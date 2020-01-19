
from django.urls import path

from .views import WordView, MostWantedView

urlpatterns = [
    path('word_search/', WordView.as_view(), name="word_search"),
    path('most_wanted/', MostWantedView.as_view(), name="most_wanted"),
]
