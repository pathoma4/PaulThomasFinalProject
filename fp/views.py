from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from .models import *

from FinalProject import settings


class Dashboard(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        all_students = Student.objects.all();
        total_courses = Course.objects.all().count();

        students = all_students.count();
        seniors = all_students.filter(year='Senior').count()
        juniors = all_students.filter(year='Junior').count()
        sophomores = all_students.filter(year='Sophomore').count()
        all_gpa_list = all_students.values_list('gpa', flat=True)
        gpa_list = [i for i in all_gpa_list if i]
        average_gpa = sum(gpa_list) + len(all_gpa_list)
        dashboard = {'students': students, 'seniors': seniors, 'juniors': juniors, 'sophomores': sophomores,
                     'total_courses': total_courses, 'average_gpa': average_gpa}

        return render(request, self.template_name, {'dashboard_data': dashboard})


class Courses(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'courses.html'

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all();

        return render(request, self.template_name, {'courses': courses})


class Students(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'students.html'

    def get(self, request, *args, **kwargs):
        students = Student.objects.all().order_by('student_id');

        return render(request, self.template_name, {'students': students})


class Enrollments(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'enrollments.html'

    def get(self, request):
        students = Student.objects.all().order_by('student_id')
        courses = Course.objects.all()
        return render(request, self.template_name, {'students': students, 'courses': courses})


class GraduationRates(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'graduation_rate.html'

    def get(self, request, *args, **kwargs):
        all_grade_rates = GraduationRate.objects.all().order_by('id').reverse()
        years = list(all_grade_rates.values_list('graduation_year', flat=True))
        four_year_gr = list(all_grade_rates.values_list('four_year_grade_rate', flat=True))
        five_year_gr = list(all_grade_rates.values_list('five_year_grade_rate', flat=True))
        six_year_gr = list(all_grade_rates.values_list('six_year_grade_rate', flat=True))

        return render(request, self.template_name,
                      {'years': years, 'four_year_gr': four_year_gr, 'five_year_gr': five_year_gr,
                       'six_year_gr': six_year_gr})


class StudentEnrolledCourses(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL
    template_name = 'enrollment_detail.html'

    def get(self, request):
        student_id = request.GET.get('student_id')
        enrolled_courses = Student.objects.filter(student_id=student_id).first()
        my_courses = enrolled_courses.courses.all()
        courses = Course.objects.all()
        return render(request, self.template_name, {'courses': courses, 'my_courses':my_courses})

class EnrollStudent(LoginRequiredMixin, View):
    login_url = settings.LOGOUT_REDIRECT_URL

    def get(self, request, *args, **kwargs):
        student_id = request.GET.get('student_id')
        course_id = request.GET.get('course_id')
        message = 'error'
        student = Student.objects.filter(student_id=student_id).first()
        if len(student.courses.all()) < 3:
            message = 'success'
            course = Course.objects.filter(course_id=course_id).first()
            student.courses.add(course)

        return HttpResponse(message, status=200)
