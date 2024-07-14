from django.urls import path
from . import views

urlpatterns = [
    path("course/<str:course>/", views.get_course, name="resume"),
    path("course/<str:course>/<str:chapter>/", views.get_chapter, name="chapter"),
    path("course/<str:course>/<str:chapter>/mark_as_completed/", views.mark_as_completed, name="mark_as_completed"),
    path("course/<str:course>/<str:chapter>/mark_as_not_completed/", views.mark_as_not_completed, name="mark_as_not_completed"),
]
