import os
import mimetypes
from django.http import Http404
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Project, Skill, Experience, Education
from django.http.response import HttpResponse, HttpResponseRedirect



def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, 'contact.html')


def project(request):
    project_object = Project.objects.filter()
    context = {
        'project_object': project_object,
    }
    return render(request, 'projects.html',context)


def resume(request):
    skill_object = Skill.objects.filter(to_display=True)
    experience_object = Experience.objects.filter(to_display=True)
    education_object = Education.objects.filter(to_display=True)

    context = {
        'education_object': education_object,
        'skill_object': skill_object,
        'experience_object': experience_object,
    }
    return render(request, 'resume.html', context)


def download_resume(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, 'static', 'assets', 'resume.pdf')

    if os.path.isfile(filepath):
        mime_type, _ = mimetypes.guess_type(filepath)

        with open(filepath, 'rb') as file:
            response_obj = HttpResponse(file.read(), content_type=mime_type)
            response_obj['Content-Disposition'] = "attachment; filename=resume.pdf"
            return response_obj

    else:
        return HttpResponseRedirect(request.path_info)


def Send_mail(request):
    try:
        print(request.method)
        print(request.POST)
        subject = "Contact us Mail test"
        message = "Test mail from you to you"
        email_address = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_address, [email_address])

        return redirect('contact')

    except:
        raise Http404


