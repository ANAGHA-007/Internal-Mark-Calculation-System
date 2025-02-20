from django.db import models

# Create your models here.
class login_model(models.Model):
    username = models.CharField(max_length=100, null=True ,blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    user_type =models.CharField(max_length=100, null=True ,blank=True)
    
class institution_model(models.Model):
    institution_name = models.CharField(max_length=100, null=True, blank=True)
    institution_address = models.CharField(max_length=100, null=True, blank=True)
    institution_contact = models.CharField(max_length=100, null=True, blank=True)
    institution_email = models.CharField(max_length=100, null=True, blank=True)
    institution_accreditation = models.CharField(max_length=100, null=True, blank=True)
    
class department_model(models.Model):
    institution_id = models.ForeignKey(institution_model, on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.CharField(max_length=100, null=True, blank=True)
    

class faculty_model(models.Model):
    LOGIN_ID = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    dep_id = models.ForeignKey(department_model, on_delete=models.CASCADE, null=True, blank=True)
    faculty_id = models.CharField(max_length=100, null=True, blank=True)
    faculty_name = models.CharField(max_length=100, null=True, blank=True)
    faculty_email = models.CharField(max_length=100, null=True, blank=True)
    faculty_phone = models.CharField(max_length=100, null=True, blank=True)
    faculty_address = models.CharField(max_length=100, null=True, blank=True)
    




class course_model(models.Model):
    dep_id = models.ForeignKey(department_model, on_delete=models.CASCADE, null=True, blank=True)
    course_name = models.CharField(max_length=100, null=True, blank=True)
    course_code = models.CharField(max_length=100, null=True, blank=True)
    course_credit = models.CharField(max_length=100, null=True, blank=True)
    
class sem_model(models.Model):
    course_id = models.ForeignKey(course_model, on_delete=models.CASCADE, null=True, blank=True)
    semester_name = models.CharField(max_length=100, null=True, blank=True)
    
class Subject_models(models.Model):
    sem_id = models.ForeignKey(sem_model, on_delete=models.CASCADE, null=True, blank=True)
    subject_name = models.CharField(max_length=100, null=True, blank=True)
    subject_code = models.CharField(max_length=100, null=True, blank=True)
    subject_credit = models.CharField(max_length=100, null=True, blank=True)

class exam_model(models.Model):
    subject_id = models.ForeignKey(Subject_models, on_delete=models.CASCADE, null=True, blank=True)
    exam_name = models.CharField(max_length=100, null=True, blank=True)
    
class student_model(models.Model):
    LOGIN_ID = models.ForeignKey(login_model, on_delete=models.CASCADE, null=True, blank=True)
    institution_id = models.ForeignKey(institution_model, on_delete=models.CASCADE, null=True, blank=True)
    SEMID = models.ForeignKey(sem_model, on_delete=models.CASCADE, null=True, blank=True)
    addmission_number = models.CharField(max_length=100, null=True, blank=True)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_email = models.CharField(max_length=100, null=True, blank=True)
    student_phone = models.CharField(max_length=100, null=True, blank=True)
    student_address = models.CharField(max_length=100, null=True, blank=True)

class mark_model(models.Model):
    teacher_id = models.ForeignKey(faculty_model, on_delete=models.CASCADE, null=True, blank=True)
    exam_id = models.ForeignKey(exam_model, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True, blank=True)
    mark = models.CharField(max_length=100, null=True, blank=True)


class Grievances_model(models.Model):
    teacher_id = models.ForeignKey(faculty_model, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.ForeignKey(student_model, on_delete=models.CASCADE, null=True, blank=True)
    grievance = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
class Notification_model(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    
