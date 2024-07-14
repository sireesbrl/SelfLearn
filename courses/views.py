from django.shortcuts import render
from courses.models import Chapters
from loginsystem.models import Course
from . import util
from markdown2 import Markdown
from django.shortcuts import redirect

def get_course(request, course):
    """
    Retrieves the course and its associated chapters from the database based on the given course name.

    Parameters:
        request (HttpRequest): The HTTP request object.
        course (str): The name of the course.

    Returns:
        HttpResponse: The rendered HTML template with the course and chapters.
    """

    course = Course.objects.get(name=course)
    chapters = Chapters.objects.filter(course=course)
    total_chapters_completed = 0
    is_completed = []

    for chapter in chapters:
        if request.user in chapter.completed_by.all():
            total_chapters_completed += 1
            is_completed.append(chapter.name)


    return render(request, "courses/course.html" , {
        "course": course,
        "chapters": chapters,
        "total_chapters_completed": total_chapters_completed,
        "is_completed": is_completed,
        })

def get_chapter(request, course, chapter):
    """
    A function to retrieve a specific chapter's content for a given course and render it to the user.
    
    Parameters:
    - request: the HTTP request object
    - course: the name of the course
    - chapter: the name of the chapter
    
    Returns:
    - Rendered HTML page with chapter content, course information, and completion status
    """

    course = Course.objects.get(name=course)
    chapters = Chapters.objects.filter(course=course)
    chapter = Chapters.objects.get(name=chapter, course=course)
    path = chapter.path
    content = convert_to_html(path)
            
    completed_by = []
    if request.user in chapter.completed_by.all():
        completed_by.append(request.user)


    return render(request, "courses/chapter.html" , {
        "chapter": chapter,
        "chapters": chapters,
        "course": course,
        "content": content,
        "completed_by": completed_by,
        })

def mark_as_completed(request, course, chapter):
    """
    A function to mark a chapter as completed by a user.
    
    Parameters:
    - request: the HTTP request object
    - course: the name of the course
    - chapter: the name of the chapter
    
    Returns:
    - Redirect to the chapter page
    """

    course = Course.objects.get(name=course)
    chapter = Chapters.objects.get(name=chapter, course=course)
    chapter.completed_by.add(request.user)
    return redirect("chapter", course=course, chapter=chapter.name)

def mark_as_not_completed(request, course, chapter):
    """
    A function to mark a chapter as not completed by a user.
    
    Parameters:
    - request: the HTTP request object
    - course: the name of the course
    - chapter: the name of the chapter
    
    Returns:
    - Redirect to the chapter page
    """

    course = Course.objects.get(name=course)
    chapter = Chapters.objects.get(name=chapter, course=course)
    chapter.completed_by.remove(request.user)
    return redirect("chapter", course=course, chapter=chapter.name)
    
def convert_to_html(path):
    """
    A function that converts the contents of a file at the specified path to HTML format using Markdown.
    
    Parameters:
        path (str): The path of the file to convert.
    
    Returns:
        str: The HTML formatted content of the file if conversion is successful, otherwise "Content not available".
    """

    contents = util.get_chapter(path)
    markdowner = Markdown()
    if contents is not None:
        return markdowner.convert(contents)
    else:
        return "Content not available"