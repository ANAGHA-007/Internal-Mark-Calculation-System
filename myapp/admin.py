from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(login_model)
admin.site.register(institution_model)
admin.site.register(department_model)
admin.site.register(faculty_model)
admin.site.register(student_model)
admin.site.register(course_model)
admin.site.register(Subject_models)
admin.site.register(mark_model)
admin.site.register(Grievances_model)
admin.site.register(sem_model)
admin.site.register(exam_model)
admin.site.register(Notification_model)
admin.site.register(Feedback_model)

