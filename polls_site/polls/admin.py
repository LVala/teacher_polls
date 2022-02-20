from django.contrib import admin

from .models import Teacher, Subject, Choice

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Choice)