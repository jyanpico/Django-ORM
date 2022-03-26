from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.view_panels, name="panels"),
    path('', views.panel_details, name="details"),
    path("details/<panel_id>/", views.panel_details, name="details"),
]
