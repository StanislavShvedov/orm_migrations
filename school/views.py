from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    student_list = Student.objects.order_by(ordering)
    for student in student_list:
        print(student.teachers)
    template = 'school/students_list.html'
    context = {'object_list': student_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
