from django.db import models


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=100)
    course_title = models.CharField(max_length=20)
    course_name = models.CharField(max_length=20)
    course_section_code = models.IntegerField()
    course_department = models.CharField(max_length=20)
    course_instructor_name = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.course_id, self.course_title, self.course_name, self.course_section_code, self.course_department, self.course_instructor_name)


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=100)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    gpa = models.FloatField(null=True, blank=True)
    courses = models.ManyToManyField(Course,  blank=True)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.student_id, self.first_name, self.last_name, self.major, self.year, self.gpa)


class GraduationRate(models.Model):
    campus = models.CharField(max_length=30)
    graduation_year = models.CharField(max_length=50)
    four_year_grade_rate = models.FloatField()
    five_year_grade_rate = models.FloatField()
    six_year_grade_rate = models.FloatField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.campus, self.graduation_year, self.four_year_grade_rate, self.five_year_grade_rate, self.six_year_grade_rate)
