from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404

def myProfile(request):
    return render(request,template_name='mainProfile.html')

def myEducation(request):
    return render(request, 'education.html')