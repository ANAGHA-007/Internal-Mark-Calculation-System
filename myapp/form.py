

from django.forms import ModelForm

from .models import *


class institution_form(ModelForm):
    class Meta:
        model=institution_model
        fields=['institution_name', 'institution_address','institution_contact','institution_email','institution_accreditation']
        

class department_form(ModelForm):
    class Meta:
        model=department_model
        fields=['institution_id','department_name']

class faculty_form(ModelForm):
    class Meta:
        model=faculty_model
        fields=['dep_id','faculty_id','faculty_name','faculty_email','faculty_phone','faculty_address']
        
class student_form(ModelForm):
    class Meta:
        model=student_model
        fields=['institution_id','addmission_number','student_name','student_email','student_phone','student_address']
        
class course_form(ModelForm):
    class Meta:
        model=course_model
        fields=['dep_id','course_name','course_code','course_credit']
        
class sem_form(ModelForm):
    class Meta:
        model=sem_model
        fields=['course_id','semester_name']
        
class subject_form(ModelForm):
    class Meta:
        model=Subject_models
        fields=['sem_id','subject_name','subject_code','subject_credit']
        
class exam_form(ModelForm):
    class Meta:
        model=exam_model
        fields=['subject_id','exam_name']
        
class mark_form(ModelForm):
    class Meta:
        model=mark_model
        fields=['teacher_id','exam_id','student_id','mark']
        
class Grievancesform(ModelForm):
    class Meta:
        model=Grievances_model
        fields=['teacher_id','student_id','grievance','status','date']
        
        
class Notificationform(ModelForm):
    class Meta:
        model=Notification_model
        fields=['title','date', 'description']
    