from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User, Course, Profile
from django.urls import reverse
from courses.models import Chapters


def home(request):
    """
    Redirects the user to their profile page if they are logged in, otherwise redirects them to the login page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the user's profile page if they are logged in, otherwise a redirect response
        to the login page.
    """
    
    #check if user is logged in
    if request.user.is_authenticated:
        return redirect(reverse("profile", kwargs={'username': request.user.username}))
    else:
        return redirect("login")

def login_view(request):
    """
    A view function that handles user login.
    If the request method is POST, it attempts to sign the user in using the provided username and password.
    If the authentication is successful, it logs in the user and redirects to the user's profile page.
    If the authentication fails, it renders the login page. If the request method is not POST, it simply renders the login page.
    
    Parameters:
        request (HttpRequest): The HTTP request object containing user login information.

    Returns:
        HttpResponse: Redirects to the user's profile page if login is successful,
        otherwise renders the login page.
    """

    if request.method == "POST":
        
        #attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        #check if authentication successful
        if user is not None:
            login(request, user)
            return redirect(reverse("profile", kwargs={'username': username}))
        else:
            return render(request, "loginsystem/login.html")

    else:
        return render(request, "loginsystem/login.html")

def logout_view(request):
    """
    Logs out the user by invalidating their session and redirects them to the login page.

    Parameters:
        request (HttpRequest): The HTTP request object containing user session information.

    Returns:
        HttpResponseRedirect: A redirect response to the login page.
    """

    logout(request)
    return redirect(reverse("login"))

def register_view(request):
    """
    Registers a new user if the request method is POST, otherwise renders the registration form.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        If the request method is POST and the passwords do not match, renders the registration form with an error message.
        If the request method is POST and the username is already taken, renders the registration form with an error message.
        If the request method is POST and the registration is successful, logs in the user and redirects them to their profile page.
        If the request method is not POST, renders the registration form.
    """

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "loginsystem/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return redirect(reverse("profile", kwargs={'username': username}))

    else:
        return render(request, "loginsystem/register.html")

def profile_view(request, username):
    """
    Retrieves the profile of a user based on their username.

    Parameters:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the user.

    Returns:
        HttpResponse: The rendered profile page with the user's username and courses.
        HttpResponseRedirect: Redirects to the courses page if the user profile does not exist.

    Raises:
        Profile.DoesNotExist: If the user profile does not exist.
    """

    # get user profile
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        courses = profile.courses.all()
        
        return render(request, "loginsystem/profile.html", {
            "username": username,
            "courses": courses,
        })
    
    # redirect to courses to enroll if user profile doesn't exist
    except Profile.DoesNotExist:
        return redirect("courses")

def courses(request):
    """
    Retrieves all courses and checks if the current user is enrolled in any of them.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered courses page with all courses and the courses the user is enrolled in.
    """

    courses = Course.objects.all()

    # check if user is enrolled in any of the courses
    enrolled = []
    for course in courses:
        if course.students.filter(username=request.user.username).exists():
            enrolled.append(course)
    
    return render(request, "loginsystem/courses.html", {
        "courses": courses,
        "enrolled": enrolled,
    })

def search_courses(request):
    """
    Searches for courses based on a given search parameter.

    Args:
        request (HttpRequest): The HTTP request object containing the search parameter.

    Returns:
        HttpResponse: The rendered search.html template with the search parameter and the courses
        matching the search.
    """
    parameter = request.POST["search"]
    courses = Course.objects.filter(name__contains=parameter)
    return render(request, "loginsystem/search.html", {
        "parameter": parameter,
        "courses": courses,
    })

def enroll(request, course):
    """
    Enrolls a user in a given course and adds it to their profile. If the user's profile does not exist, it creates a new one.

    Parameters:
    - request (HttpRequest): The HTTP request object.
    - course (str): The name of the course to enroll the user in.

    Returns:
    - HttpResponseRedirect: A redirect to the user's profile page.
    """

    course = Course.objects.get(name=course)

    # enroll course in user profile, or create profile if it doesn't exist
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    # add course to user profile
    profile.courses.add(course)
    profile.save()

    # enroll user in course
    course.students.add(request.user)
    course.save()

    return redirect("resume", course=course.name)

def unenroll(request, course):
    """
    A function to unenroll a user from a course, update the user profile, and remove chapter completions.
    
    Parameters:
    - request: the request object containing user information
    - course: the name of the course to unenroll from
    
    Returns:
    - Redirects the user to their profile page after unenrollment
    """

    # remove course from user profile
    course = Course.objects.get(name=course)
    profile = Profile.objects.get(user=request.user)
    profile.courses.remove(course)
    profile.save()

    # if a profile has no courses, delete it
    if profile.courses.count() == 0:
        profile.delete()

    # unenroll user from course
    course.students.remove(request.user)
    course.save()
    
    # remove chapter completion of user
    chapters = Chapters.objects.filter(completed_by=request.user)
    for chapter in chapters:
        chapter.completed_by.remove(request.user)
        chapter.save()

    return redirect("profile", username=request.user.username)
