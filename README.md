# SelfLearn

**Video Demo**: [watch here](https://youtu.be/uAO_2DXPkco?si=RiV2agaqPhVquXB6)<br>

## Distinctiveness and Complexity

SelfLearn is a Django Web App revolutionizing online learning by curating a collection of open-source and free resources, enabling underprivileged individuals to access higher education across diverse fields. The platform's inception aimed to offer a centralized hub for top-notch open-source materials, fostering personal growth and knowledge expansion.
    
With a sleek and intuitive user interface, SelfLearn simplifies course enrollment and management. Each user has a dedicated profile showcasing all enrolled courses, allowing seamless course navigation. Users can easily resume or unenroll from courses directly within their profile. Course chapters are conveniently displayed in the left sidebar upon enrollment, facilitating structured learning. Progress tracking is enhanced through the ability to mark chapters as completed, ensuring a comprehensive overview of course advancement. Additionally, supplementary resources are provided for each chapter, enriching the learning experience.

## General File Contents
#### Settings
The project's settings are well-configured in the `settings.py` file, which serves as the central configuration hub for the Django project. It includes essential settings such as the project's base directory, secret key for security, debugging options, and allowed host configurations. These settings are crucial for the project's functionality, security, and deployment.

#### Models
The project follows the Model-View-Template (MVT) architectural pattern provided by Django. Models in the loginsystem and courses apps define the data structures used in the application, such as User, Course, Chapter, and Profile. Views in these apps handle user interactions and business logic, while templates render the HTML content displayed to users.

#### Urls
The `urls.py` file in the project defines the URL patterns that map to views, enabling proper navigation within the application. URLs like `/admin/`, `/courses/`, and `/course/<str:course>/` are defined to access different parts of the application easily.

#### Authentication
The project utilizes Django's built-in authentication system for user management. The User model in the loginsystem app is extended using Django's AbstractUser, allowing for custom user attributes and functionalities. User authentication, login, and logout processes are handled in the `views.py` file of the loginsystem app.

#### Courses
The courses app focuses on providing educational content organized into courses and chapters. Views in this app render course information, chapters, and allow users to mark chapters as completed. The `models.py` file defines the data models for courses and chapters, ensuring data integrity and consistency.

#### Database
The project leverages Django's migration system to manage changes to the database schema over time. Migration files in the courses app track and apply these changes, ensuring database compatibility across different versions of the application.

## How to Run SelfLearn?

Follow these steps to run SelfLearn on your local machine:

1. **Clone the Repository**:
```
git clone <url:project>
```
Replace `<url:project>` with repository url.

2. **Navigate to the Project Directory**:
```
cd <selflearn:project-folder>
```
Replace `<selflearn:project-folder>` with the folder you cloned the repository into.

3. **Install Dependencies**:
```
pip install -r requirements.txt
```

4. **Start the Server**:
```
python3 manage.py runserver
```

## Future Development
**Implement Additional Features**:
* Add an AI chatbot to allow users to clear any confusions present. This feature is disabled for this version of the app.

* Add a feature to allow users to interact with instructors or other students.

* Integrate a discussion forum for each course to enhance collaborative learning.

* Implement a recommendation system to suggest courses based on user interests or completion history.

**Enhance User Experience**:
* Improve the UI/UX design to make the platform more visually appealing and user-friendly.

* Implement responsive design to ensure a seamless experience across different devices.

**Enhance Security**:
* Implement additional security measures such as HTTPS, CSRF protection, and input validation to protect user data.
Regularly update Django and other dependencies to address security vulnerabilities.

**Performance Optimization**:
* Optimize database queries and use caching mechanisms to improve performance.

* Implement lazy loading for course content to reduce initial page load times.

**Expand Course Content**:
* Collaborate with educational content providers to expand the range of courses offered.

* Allow instructors to create and publish their courses on the platform.

**Localization and Internationalization**:
* Implement multi-language support to cater to a global audience.

* Provide localization features to adapt content based on the user's location.

**Testing and Quality Assurance**:
* Write comprehensive unit tests to ensure code quality and prevent regressions.

* Conduct usability testing to gather feedback from users and improve the overall experience.

## Conclusion
Overall, the "SelfLearn" project demonstrates the power and flexibility of Django in building robust web applications. With its well-structured codebase, clear separation of concerns, and adherence to Django best practices, the project provides a solid foundation for creating an engaging and interactive learning platform.