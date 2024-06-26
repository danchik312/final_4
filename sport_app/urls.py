from django.urls import path
from . import views

urlpatterns = [
    path('sport_app/', views.SportListView.as_view()),
]
