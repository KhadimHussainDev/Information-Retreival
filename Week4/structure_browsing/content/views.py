from django.shortcuts import render, get_object_or_404
from .models import Course, Subject

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    return render(request, 'subject_detail.html', {'subject': subject})
