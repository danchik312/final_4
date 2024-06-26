from django.urls import path
from . import views

urlpatterns = [
    path('', views.SportListView.as_view(), name="sport_app"),
    path("all_products/", views.all_products, name="all_products"),
    path("Sport_list/", views.SportProductView.as_view(), name="Sport_list"),
    path(
        "Sport_list/<int:id>/",
        views.SportDetailView.as_view(),
        name="SportDetailView",
    ),
    path("youth/", views.sport_tags_view, name="youth"),
    path('pensioner/', views.pensioner_tags_view, name="pensioner"),
]
