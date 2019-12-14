from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path('courses', views.Courses.as_view(), name='courses'),
    path('students', views.Students.as_view(), name='students'),
    path('enrollments', views.Enrollments.as_view(), name='enrollments'),
    path('graduation-rate', views.GraduationRates.as_view(), name='graduation-rate'),
    path('get-enrollments', views.StudentEnrolledCourses.as_view(), name='get-enrollments'),
    path('enroll', views.EnrollStudent.as_view(), name='enroll'),
]