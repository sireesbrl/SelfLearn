from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/<str:username>/", views.profile_view, name="profile"),
    path("courses/", views.courses, name="courses"),
    path("search/", views.search_courses, name="search"),
    path("enroll/<str:course>/", views.enroll, name="enroll"),
    path("resume/", include("courses.urls")),
    path("unenroll/<str:course>/", views.unenroll, name="unenroll"),
]