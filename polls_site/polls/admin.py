from django.contrib import admin

from .models import Teacher, Subject, Choice

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['teacher', 'subject']}),
        ('Voting - values', {'fields': ['total_voters_number', 'total_quality', 'total_friendliness', 'total_motivation', 'total_ease']}),
    ]

    list_display = ('teacher', 'subject')

    list_filter = ['subject']

admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)

# change admin site headers etc.
admin.site.site_header = 'Teacher polls administration'
admin.site.site_title = 'Administration'
admin.site.index_title = 'Teacher polls'