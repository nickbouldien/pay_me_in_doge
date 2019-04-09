from django.urls import path
from .views import (
    SiteCreateView,
    SiteDeleteView,
    SiteDetailView,
    SiteListView,
    SiteUpdateView,
    UserSiteListView,
)
from . import views

urlpatterns = [
    path("", SiteListView.as_view(), name="board-home"),
    path("about/", views.about, name="board-about"),
    path("resources/", views.resources, name="board-resources"),
    path("site/<uuid:pk>/", SiteDetailView.as_view(), name="site-detail"),
    path("site/<uuid:pk>/delete/", SiteDeleteView.as_view(), name="site-delete"),
    path("site/<uuid:pk>/update/", SiteUpdateView.as_view(), name="site-update"),
    path("site/new/", SiteCreateView.as_view(), name="site-create"),
    path("user/<str:username>/", UserSiteListView.as_view(), name="user-sites"),
]
