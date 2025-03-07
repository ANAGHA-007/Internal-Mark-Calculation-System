from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from myapp.serializers import Course_serializer, Department_serializer, DepartmentSerializer, Exam_serializer, Faculty_serializer, Grievances_serializer, Institution_serializer, Login_serializer, Mark_serializer, Notification_serializer, Sem_serializer, Student_serializer

from .form import *

from .models import *

# Create your views here.

class Logout(View):
    def get(self, request):
        return HttpResponse('''<script>alert('Logout successfully');window.location='/'</script>''')



class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = login_model.objects.get(username=username, password=password)
        request.session["loginid"] = login_obj.id
        
        if login_obj.user_type == "admin":
            return HttpResponse('''<script>alert ("Logged in successfully");window.location= "/adminhome"</script>''')

        
class Adminhome(View):
    def get(self, request):
        return render(request, 'administrator/adminhome.html')
    
class institutiondetails(View):
    def get(self, request):
        return render(request, 'administrator/institution_details.html')
    def post(self,request):
        print(request.POST)
        c=institution_form(request.POST)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/view_institution_details"</script>''')
        
class DeleteInst(View):
    def get(self, request, id):
        c = institution_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/view_institution_details"</script>''')

class EditInst(View):
    def get(self, request, id):
        obj=institution_model.objects.get(id=id)
        return render(request, 'administrator/viewedit_institution_details.html',{'val':obj})
    def post(self,request,id):
        obj=institution_model.objects.get(id=id)
        c=institution_form(request.POST,instance=obj)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data Updated successfully");window.location= "/view_institution_details"</script>''')
       
        
class managecourses(View):
    def get(self, request):
        c = course_model.objects.all()
        return render(request, 'administrator/manage_courses.html', {'data': c})


class deletecourse(View):
    def get(self, request, id):
        c = course_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/manage_courses"</script>''')
    
class editcourse(View):
    def get(self, request, id):
        c = department_model.objects.all()
        obj=course_model.objects.get(id=id)
        return render(request, 'administrator/viewedit_managecourses.html',{'val':obj, 'data': c})
    def post(self,request,id):
        obj=course_model.objects.get(id=id)
        c=course_form(request.POST, instance=obj)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data Updated successfully");window.location= "/manage_courses"</script>''')
  
    
class managestudents(View):
    def get(self, request):
        c=student_model.objects.all()
        return render(request, 'administrator/manage_student.html', {'data': c})
    
class deletestudent(View):
    def get(self, request, id):
        c = student_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/manage_student"</script>''')



class managefaculty(View):
    def get(self, request):
        c = faculty_model.objects.all()
        return render(request, 'administrator/manage_faculties.html', {'data': c})
    
class DeleteFac(View):
    def get(self, request, id):
        c = faculty_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/manage_faculties"</script>''')

    
class manageprograms(View):
    def get(self, request):
        c=department_model.objects.all()
        return render(request, 'administrator/manage_program.html',{'data':c})
    
    def post(self,request):
        print(request.POST)
        c=department_form(request.POST)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_programs"</script>''')
        
class deleteprgm(View):
    def get(self, request, id):
        c = department_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/manage_program"</script>''')

class editprgm(View):
    def get(self, request, id):
        c = institution_model.objects.all()
        obj=department_model.objects.get(id=id)
        return render(request, 'administrator/viewedit_manageprogram.html',{'val':obj, 'data': c})
    def post(self,request,id):
        obj=department_model.objects.get(id=id)
        c=department_form(request.POST,instance=obj)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data Updated successfully");window.location= "/manage_program"</script>''')

        
class notification(View):
    def post(self, request):
        c = Notificationform(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/viewnotification"</script>''')
    
class viewnotification(View):
    def get(self, request):
        c = Notification_model.objects.all()
        return render(request, 'administrator/viewnotification.html', {'data': c})
    def post(self, request):
        c = Notificationform(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert("Notification Added Successfully");window.location='/viewnotification'</script>''')
        
class DeleteNotification(View):
    def get(self, request, id):
        c = Notification_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert("deleted successfully");window.location='/viewnotification'</script>''')
    
def get_departments(request):
    institution_id = request.GET.get('institution_id')
    departments = department_model.objects.filter(institution_id=institution_id).values('id', 'department_name')
    return JsonResponse(list(departments), safe=False)

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = course_model.objects.filter(dep_id=department_id).values('id', 'course_name')
    return JsonResponse(list(courses), safe=False)

def get_semesters(request):
    course_id = request.GET.get('course_id')
    semesters = sem_model.objects.filter(course_id=course_id).values('id', 'semester_name')
    return JsonResponse(list(semesters), safe=False)    
    

    
class viewaddstudent(View):
    def get(self, request):
        c = institution_model.objects.all()
        
        return render(request, 'administrator/view_addstudents.html', {'data': c})
    def post(self, request):
        institution_id = request.POST.get('institution_id')
        semester_id = request.POST.get('semester')

        # Get multiple values from the form
        admission_numbers = request.POST.getlist('admission_number[]')
        student_names = request.POST.getlist('student_name[]')
        student_emails = request.POST.getlist('student_email[]')
        student_phones = request.POST.getlist('student_phone[]')
        student_addresses = request.POST.getlist('student_address[]')

        for i in range(len(admission_numbers)):
            if admission_numbers[i] and student_names[i] and student_emails[i]:  # Ensure required fields are filled
                # Create a login entry for the student
                fac = login_model.objects.create(
                    username=student_emails[i],
                    password=admission_numbers[i], 
                    user_type="student"
                )

                # Save student details
                student_model.objects.create(
                    LOGIN_ID=fac,
                    institution_id_id=institution_id,
                    SEMID_id=semester_id,
                    addmission_number=admission_numbers[i],
                    student_name=student_names[i],
                    student_email=student_emails[i],
                    student_phone=student_phones[i],
                    student_address=student_addresses[i]
                )

        return HttpResponse('''<script>alert("Students added successfully!"); window.location="/manage_student"</script>''')
    
    
class vieweditstudents(View):
    def get(self, request, id):
        c=student_model.objects.get(id=id)
        d = institution_model.objects.all
        return render(request, 'administrator/view_editstudents.html', {'val': c, 'data': d})

    def post(self,request, id):
        obj = student_model.objects.get(id=id)
        c=student_form(request.POST , instance=obj)
        if c.is_valid():
            c.save(commit=False)
            student = login_model.objects.get(id=obj.LOGIN_ID.id)
            student.username = request.POST['student_email']
            student.password = request.POST['addmission_number']
            student.save()
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_student"</script>''')
    
class view_institutiondetails(View):
   def get(self, request):
        c = institution_model.objects.all()
        return render(request, 'administrator/view_institution_details.html', {'data': c})
  
    
class viewaddmanagecourses(View):
    def get(self, request):
        
        c = institution_model.objects.all()
        return render(request, 'administrator/viewadd_managecourses.html', {'data': c})
    def post(self,request):
        print(request.POST)
        c=course_form(request.POST)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_courses"</script>''')
        
        
class GetDepartments(View):
    def get(self, request):
        institution_id = request.GET.get('institution_id')
        if institution_id:
            # Use the correct field name 'department_name'
            departments = department_model.objects.filter(institution_id=institution_id).values('id', 'department_name')
            return JsonResponse(list(departments), safe=False)
        return JsonResponse([], safe=False)
        
class vieweditmanagecourses(View):
    def get(self, request):
        return render(request, 'administrator/viewedit_managecourses.html')
    

def get_depts(request):
    institution_id = request.GET.get('institution_id')
    departments = department_model.objects.filter(institution_id=institution_id).values('id', 'department_name')
    return JsonResponse({'departments': list(departments)})
    
    
class viewaddmanagefaculty(View):
    def get(self, request):
        institutions = institution_model.objects.all()  # Fetch institutions
        return render(request, 'administrator/viewadd_managefaculties.html', {'institutions': institutions})
    def post(self,request):
        c=faculty_form(request.POST)
        if c.is_valid():
            reg = c.save(commit=False)
            fac = login_model.objects.create(username=reg.faculty_email, password=reg.faculty_id, user_type="faculty")
            reg.LOGIN_ID = fac
            reg.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_faculties"</script>''')
        
        
class vieweditmanagefaculty(View):
    def get(self, request, id):
        c = department_model.objects.all()
        obj=faculty_model.objects.get(id=id)
        return render(request, 'administrator/viewedit_managefaculties.html', {'val': obj, 'data': c})
    def post(self, request, id):
        obj = faculty_model.objects.get(id=id)
        c = faculty_form(request.POST, instance=obj)
        if c.is_valid():
            c.save(commit=False)
            faculty = login_model.objects.get(id=obj.LOGIN_ID.id)
            faculty.username = request.POST['faculty_email']
            faculty.password = request.POST['faculty_id']
            faculty.save()
            c.save()
            return HttpResponse('''<script>alert ("Data Updated successfully");window.location= "/manage_faculties"</script>''')
        
    
    
class viewaddmanageprogram(View):
    def get(self, request):
        c = institution_model.objects.all()
        return render(request, 'administrator/viewadd_manageprogram.html', {'data': c})
    def post(self,request):
        c=department_form(request.POST)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_program"</script>''')
    
    
    
class vieweditmanageprogram(View):
    def get(self, request):
        return render(request, 'administrator/viewedit_manageprogram.html')
    
    
class componentsandweightage(View):
    def get(self, request):
        return render(request, 'faculty/components and weightage.html')
    
class entermark(View):
    def get(self, request):
        return render(request, 'faculty/entermark.html')
    
class facultyfunction(View):
    def get(self, request):
        return render(request, 'faculty/facultyfunction.html')
    
class facultyhome(View):
    def get(self, request):
        return render(request, 'faculty/facultyhome.html')
    
class report(View):
    def get(self, request):
        return render(request, 'faculty/report.html')
    
class viewreport(View):
    def get(self, request):
        return render(request, 'faculty/viewreport.html')
    

class Manage_Semester(View):
    def get(self, request):
        c = sem_model.objects.all()
        return render(request, 'administrator/managesemester.html', {'data': c})
    
class EditSemester(View):
    def get(self, request, id):
        d = sem_model.objects.get(id=id)
        c = course_model.objects.all()
        return render(request, 'administrator/EditSemester.html', {'data': c, 'val': d})
    def post(self, request, id):
        d = sem_model.objects.get(id=id)
        f = sem_form(request.POST, instance=d)
        if f.is_valid():
            f.save()
            return HttpResponse('''<script>alert("edited successfully");window.location='/managesemester'</script>''')
    
class Add_Semester(View):
    def get(self, request):
        c = course_model.objects.all()
        return render(request, 'administrator/viewaddmanage_semester.html', {'data': c})
    def post(self, request):
        c = sem_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/managesemester"</script>''')
        
class Delete_Semester(View):
    def get(self, request, id):
        c = sem_model.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert ("Data Deleted successfully");window.location= "/managesemester"</script>''')
    
    
    
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import login_model  # Import your login model
from django.contrib.auth import authenticate

# Serializer
#class LoginSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = login_model  # Replace with your model
        #fields = ['username', 'password', 'user_type']


# API View

from rest_framework import status
class LoginAPIView(APIView):
    def post(self, request):
        print("---------------->")
        response_dict = {}
        print("------------>", request.data)
      # Get data from the request
        username = request.data.get("username")
        print(username)
        password = request.data.get("password")
        print(password)
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the user from LoginTable
        t_user = login_model.objects.filter(username=username,password=password).first()
        print(t_user)
        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)
        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        response_dict["user_type"] = t_user.user_type
        

        return Response(response_dict, status=status.HTTP_200_OK)
    
    
class InstitutionAPIView(APIView):
    # GET request to fetch institution data
    def get(self, request, *args, **kwargs):
        institutions = institution_model.objects.all()  # Get all institutions
        serializer = Institution_serializer(institutions, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new institution
    def post(self, request, *args, **kwargs):
        serializer = Institution_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new institution instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import serializers, generics

class DepartmentListAPIView(APIView):
    def get(self, request):
        departments = department_model.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        print("--------------------->", serializer.data)  # Debugging: Prints serialized data
        return Response({"departments": serializer.data}, status=status.HTTP_200_OK) 

class DepartmentAPIView(APIView):
    # GET request to fetch all departments
    def get(self, request, *args, **kwargs):
        departments = department_model.objects.all()  # Get all departments
        serializer = Department_serializer(departments, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new department
    # def post(self, request, *args, **kwargs):
    #     serializer = DepartmentSerializer(data=request.data)
        
    #     if serializer.is_valid():  # Validate the incoming data
    #         serializer.save()  # Save the new department instance
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FacultyAPIView(APIView):
    # GET request to fetch all faculty members
    def get(self, request, *args, **kwargs):
        faculty_members = faculty_model.objects.all()  # Get all faculty records
        serializer = Faculty_serializer(faculty_members, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new faculty member
    def post(self, request, *args, **kwargs):
        serializer = Faculty_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new faculty instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseAPIView(APIView):
    # GET request to fetch all courses
    def get(self, request, *args, **kwargs):
        courses = course_model.objects.all()  # Get all course records
        serializer = Course_serializer(courses, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new course
   



class SemAPIView(APIView):
    # GET request to fetch all semester details
    def get(self, request, *args, **kwargs):
        semesters = sem_model.objects.all()  # Get all semester records
        serializer = Sem_serializer(semesters, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new semester
    



class SubjectAPIView(APIView):
    # GET request to fetch all subjects
    def get(self, request, *args, **kwargs):
        subjects = Subject_models.objects.all()  # Get all subject records
        serializer = Subject_serializer(subjects, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new subject
    def post(self, request, *args, **kwargs):
        serializer = Subject_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new subject instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ExamAPIView(APIView):
    # GET request to fetch all exams
    def get(self, request, *args, **kwargs):
        exams = exam_model.objects.all()  # Get all exam records
        serializer = Exam_serializer(exams, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new exam
    def post(self, request, *args, **kwargs):
        serializer = Exam_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new exam instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Serializer
#class StudentSerializer(serializers.ModelSerializer):
    #class Meta:
       # model = student_model  # Replace with your model
        #fields = ['LOGIN_ID', 'institution_id', 'SEMID', 'addmission_number', 'student_name', 'student_email', 'student_phone', 'student_address']

# API View

class getstudentbysemcodep(APIView):
    def get(self,request,sem,co,dep):
        print(sem,co,dep)
        students=student_model.objects.filter(SEMID=sem,SEMID__course_id__id=co,SEMID__course_id__dep_id__id=dep)
        print("asdfghjkl",students)
        serializer = Student_serializer(students, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class StudentAPIView(APIView):
    # GET request to fetch all students
    def get(self, request, *args, **kwargs):
        students = student_model.objects.all()  # Get all student records
        serializer = Student_serializer(students, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new student
    def post(self, request, *args, **kwargs):
        serializer = Student_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new student instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API View
class MarkAPIView(APIView):
    # GET request to fetch all marks
    def get(self, request, *args, **kwargs):
        marks = mark_model.objects.all()  # Get all mark records
        serializer = Mark_serializer(marks, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new mark entry
    def post(self, request, *args, **kwargs):
        serializer = Mark_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new mark entry
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# API View
class GrievancesAPIView(APIView):
    # GET request to fetch all grievances
    def get(self, request, *args, **kwargs):
        grievances = Grievances_model.objects.all()  # Get all grievances
        serializer = Grievances_serializer(grievances, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new grievance
    def post(self, request, *args, **kwargs):
        serializer = Grievances_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new grievance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# API View
class NotificationAPIView(APIView):
    # GET request to fetch all notifications
    def get(self, request):
        notifications = Notification_model.objects.all()  # Get all notifications
        serializer = Notification_serializer(notifications, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST request to create a new notification
    def post(self, request, *args, **kwargs):
        serializer = Notification_serializer(data=request.data)
        
        if serializer.is_valid():  # Validate the incoming data
            serializer.save()  # Save the new notification
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import mark_model, exam_model, student_model, faculty_model
from .serializers import MarkSerializer, ExamSerializer, SubjectMarkSerializer
from django.shortcuts import get_object_or_404

class MarkAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        """Retrieve all marks with related exam details."""
        marks = mark_model.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Create a new mark entry with multiple exams."""
        data = request.data
        print(data)
        student = get_object_or_404(student_model, id=data.get("student_id"))
        print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",student)
        
        teacher = faculty_model.objects.filter(LOGIN_ID__id=request.data.get('teacher_id'))
        print("---++++++-------->",request.data.get('teacher_id'))
        print("--------teacher------->",teacher)
        print("teacher",teacher)
        data['teacher_id']=teacher.id
        data['student_id']=student.id      

        for exam_data in data.get("exam", []):
            print(exam_data)
            exam = exam_model.objects.create(
                exam_name=exam_data["examname"]
            )
            mark_instance = mark_model.objects.create(
                teacher_id=teacher,
                student_id=student,
                exam_id=exam,
                mark=exam_data["marks"],
                mark_outof=exam_data["out_of"],
                weightage=exam_data["weightage"],
                assignmentmark=exam_data["assignment_mark"],
                assignment_outof=exam_data["assignment_outof"],
                seminarmark=data.get("seminar_mark"),
                seminar_outof=data.get("seminar_outof"),
            )
        
        return Response({"message": "Marks added successfully!"}, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """Update an existing mark entry."""
        mark_instance = get_object_or_404(mark_model, id=pk)
        serializer = MarkSerializer(mark_instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        """Delete a mark entry."""
        mark_instance = get_object_or_404(mark_model, id=pk)
        mark_instance.delete()
        return Response({"message": "Mark deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
 
        
        
class StudentsMarkAPIView(APIView):

    def get(self, request,student_id, *args, **kwargs):
        """Retrieve mark entries for a given student ID"""
        # student_id = request.query_params.get("student_id")  # Get student_id from query params
        if not student_id:
            return Response({"error": "student_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        student = get_object_or_404(student_model, id=student_id)
        marks = mark_model.objects.filter(student_id=student)

        if not marks.exists():
            return Response({"message": "No marks found for this student"}, status=status.HTTP_404_NOT_FOUND)

        # Preparing the response data
        marks_data = []
        for mark in marks:
            marks_data.append({
                "exam_name": mark.exam_id.exam_name,
                "marks": mark.mark,
                "out_of": mark.mark_outof,
                "weightage": mark.weightage,
                "assignment_mark": mark.assignmentmark,
                "assignment_outof": mark.assignment_outof,
                "seminar_mark": mark.seminarmark,
                "seminar_outof": mark.seminar_outof,
                "teacher_id": mark.teacher_id.id if mark.teacher_id else None
            })

        return Response({"student_id": student.id, "marks": marks_data}, status=status.HTTP_200_OK)



#  //////////////////////////////////////// STUDENT ////////////////////////////////////////////


class StudentMarkAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """Retrieve all marks with related exam details."""
        marks = Subject_models.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Retrieve all marks with related exam details."""
        marks = mark_model.objects.all()
        serializer = MarkSerializer(marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SubjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Subject_models
        fields = ['id', 'subject_name', 'subject_code', 'subject_credit']

class SemesterSerializer1(serializers.ModelSerializer):
    subjects = SubjectSerializer1(source='Subject_models_set', many=True, read_only=True)  # Correct reverse relation to fetch subjects

    class Meta:
        model = sem_model
        fields = ['id', 'semester_name', 'subjects']


class ViewSubjectsApi(APIView):
        def get(self, request,lid):
            s_id=request.data.get('lid')

            marks = mark_model.objects.filter(student_id__LOGIN_ID_id=lid)

            serializer = SubjectMarkSerializer(marks, many=True)
            print('--------------------->', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)

class ViewFacultyApi(APIView):
        def get(self, request,lid):
            student_obj = student_model.objects.get(LOGIN_ID_id=lid)
            faculty_obj = faculty_model.objects.filter(dep_id__id=student_obj.SEMID.course_id.dep_id.id)
            serializer = Faculty_serializer(faculty_obj, many=True)
            print('--------------------->', serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)


from .serializers import FeedbackSerializer

class FeedbackAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                feedback = Feedback_model.objects.filter(student_id__LOGIN_ID__id=pk).all()
                serializer = FeedbackSerializer(feedback,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Feedback_model.DoesNotExist:
                return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            feedbacks = Feedback_model.objects.all()
            serializer = FeedbackSerializer(feedbacks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        data={}
        student_id=student_model.objects.filter(LOGIN_ID__id=request.data['student_id']).first()
        data=request.data
        data['student_id']=student_id.id
        faculty_id=faculty_model.objects.filter(LOGIN_ID__id=request.data['teacher_id']).first()
        data['teacher_id']=faculty_id.id
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            feedback = Feedback_model.objects.get(pk=pk)
        except Feedback_model.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            feedback = Feedback_model.objects.get(pk=pk)
            feedback.delete()
            return Response({"message": "Feedback deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Feedback_model.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)

class FeedbackoffacultyAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                feedback = Feedback_model.objects.filter(teacher_id__LOGIN_ID__id=pk).all()
                serializer = FeedbackSerializer(feedback,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Feedback_model.DoesNotExist:
                return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            feedbacks = Feedback_model.objects.all()
            serializer = FeedbackSerializer(feedbacks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        data={}
        student_id=student_model.objects.filter(LOGIN_ID__id=request.data['student_id']).first()
        data=request.data
        data['student_id']=student_id.id
        faculty_id=faculty_model.objects.filter(LOGIN_ID__id=request.data['teacher_id']).first()
        data['teacher_id']=faculty_id.id
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            feedback = Feedback_model.objects.get(pk=pk)
        except Feedback_model.DoesNotExist:
            return Response({"error": "Feedback not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AddSubject(View):
    def get(self,request):
        c = institution_model.objects.all()
        return render(request, 'administrator/AddSubject.html', {'institutions': c})
    def post(self, request):
        c = subject_form(request.POST)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('subject added successfully');window.location='/managesubject'</script>''')
    
    
class managesubject(View):
    def get(self,request):
        c = Subject_models.objects.all()
        return render(request,'administrator/managesubject.html',{'data':c})
    
class Edit_Subject(View):
    def get(self, request, id):
        # Fetch the subject object by ID
        subject = Subject_models.objects.get(id=id)
        
        # Access the related institution, department, course, and semester
        institution = subject.sem_id.course_id.dep_id.institution_id
        department = subject.sem_id.course_id.dep_id
        course = subject.sem_id.course_id
        semester = subject.sem_id
        print(institution,'institution')
        print(department,'department')
        print(course,'course')
        print(semester,'semester')
        # Fetch all the necessary data to populate the dropdowns
        institutions = institution_model.objects.all()
        departments = department_model.objects.filter(institution_id=institution)
        courses = course_model.objects.filter(dep_id=department)
        semesters = sem_model.objects.filter(course_id=course)
        
        # Pass all the necessary data to the template
        return render(request, 'administrator/editsubject.html', {
            'subject': subject,
            'institutions': institutions,
            'departments': departments,
            'courses': courses,
            'semesters': semesters,
            'institution':institution,
            'department':department,
            'course':course,
            'semester':semester
            
        })
        
    def post(self, request, id):
        subject = Subject_models.objects.get(id=id)
        c = subject_form(request.POST,instance=subject)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('subject edited successfully');window.location='/managesubject'</script>''')
    


class Delete_Subject(View):
    def get(self, request, id):
        c = Subject_models.objects.get(id=id)
        c.delete()
        return HttpResponse('''<script>alert('deleted successfully');window.location='/managesubject'</script>''')