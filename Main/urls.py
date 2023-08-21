from django.urls import path
from .views import index, resume, contact, project, download_resume, Send_mail

urlpatterns = [
    path('', index, name="index"),
    path('project', project, name="project"),
    path('resume', resume, name="resume"),
    path('contact', contact, name="contact"),
    path('download', download_resume, name="download"),
    path('Send_mail', Send_mail, name="Send_mail"),
]
