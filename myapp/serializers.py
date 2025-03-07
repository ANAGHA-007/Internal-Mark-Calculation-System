
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *



class Login_serializer(ModelSerializer):
    class Meta:
        model = login_model
        fields = ['username', 'password', 'user_type']
        
class Institution_serializer(ModelSerializer):
    class Meta:
        model = institution_model
        fields = ['institution_name', 'institution_address', 'institution_contact', 'institution_email', 'institution_accreditation']
        
class Department_serializer(ModelSerializer):
    class Meta:
        model = department_model
        fields = ['institution_id', 'department_name']
        
class Faculty_serializer(ModelSerializer):
    department_name = serializers.CharField(source='dep_id.department_name', read_only=True)
    department_id = serializers.CharField(source='dep_id.id', read_only=True)
    class Meta:
        model = faculty_model
        fields = ['LOGIN_ID', 'faculty_id', 'faculty_name', 'faculty_email', 'faculty_phone', 'faculty_address', 'department_name','department_id']        
class Course_serializer(ModelSerializer):
    class Meta:
        model = course_model
        fields = ['dep_id', 'course_name', 'course_code', 'course_credit']
        
class Sem_serializer(ModelSerializer):
    class Meta:
        model = sem_model
        fields = ['course_id', 'semester_name']
        
class Exam_serializer(ModelSerializer):
    class Meta:
        model = exam_model
        fields = ['subject_id', 'exam_name']
        
class Student_serializer(ModelSerializer):
    class Meta:
        model = student_model
        fields = ['id','LOGIN_ID', 'institution_id', 'SEMID', 'addmission_number', 'student_name', 'student_email', 'student_phone', 'student_address']
        
class Mark_serializer(ModelSerializer):
    class Meta:
        model = mark_model
        fields = [' teacher_id ', 'exam_id', 'student_id', 'mark']
        
class Grievances_serializer(ModelSerializer):
    class Meta:
        model = Grievances_model
        fields = ['teacher_id', 'student_id', 'grievance', 'status', 'date']
        
class Notification_serializer(ModelSerializer):
    class Meta:
        model = Notification_model
        fields = ['title', 'description', 'date']

from rest_framework import serializers
from .models import department_model, course_model, sem_model, Subject_models

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_models
        fields = ['id', 'subject_name', 'subject_code', 'subject_credit']

class SemesterSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True, source='subject_models_set')  # Corrected reverse relation

    class Meta:
        model = sem_model
        fields = ['id', 'semester_name', 'subjects']

class CourseSerializer(serializers.ModelSerializer):
    semesters = SemesterSerializer(many=True, read_only=True, source='sem_model_set')  # Corrected reverse relation

    class Meta:
        model = course_model
        fields = ['id', 'course_name', 'course_code', 'course_credit', 'semesters']

class DepartmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True, source='course_model_set')  # Corrected reverse relation

    class Meta:
        model = department_model
        fields = ['id', 'department_name', 'courses']        
from rest_framework import serializers
from .models import mark_model, exam_model

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = exam_model
        fields = "__all__"

class MarkSerializer(serializers.ModelSerializer):
    exam = ExamSerializer(read_only=True)  # Nested serialization

    class Meta:
        model = mark_model
        fields = "__all__"
        
class SubjectMarkSerializer(serializers.ModelSerializer):
    subject=serializers.CharField(source='exam_id.subject_id.subject_name', read_only='True')
    exam=serializers.CharField(source='exam_id.exam_name', read_only='True')
     # Nested serialization

    class Meta:
        model = mark_model
        fields = ['teacher_id','exam','student_id','mark','mark_outof','weightage','assignmentmark','assignment_outof','seminarmark','seminar_outof', 'subject']

from rest_framework import serializers
from .models import Feedback_model

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback_model
        fields = '__all__'
