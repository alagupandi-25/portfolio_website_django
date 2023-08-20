from django.db import models

# Create your models here.


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    to_display = models.BooleanField(default=True)


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    company = models.CharField(max_length=254, null=False, blank=False)
    position = models.CharField(max_length=254, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    to_display = models.BooleanField(default=True)


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    institution = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    to_display = models.BooleanField(default=True)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    programming_language = models.BooleanField(default=False)
    to_display = models.BooleanField(default=True)

    def __str__(self):
        return f"Skill object {self.name} and id - {self.id}"
