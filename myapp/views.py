from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .form import *

from .models import *

# Create your views here.


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

class viewaddstudent(View):
    def get(self, request):
        c = institution_model.objects.all()
        return render(request, 'administrator/view_addstudents.html', {'data': c})
    def post(self,request):
        c=student_form(request.POST)
        if c.is_valid():
            reg = c.save(commit=False)
            fac = login_model.objects.create(username=reg.student_email, password=reg.addmission_number, user_type="student")
            reg.LOGIN_ID = fac
            reg.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_student"</script>''')
    
    
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
        c = department_model.objects.all()
        return render(request, 'administrator/viewadd_managecourses.html', {'data': c})
    def post(self,request):
        print(request.POST)
        c=course_form(request.POST)
        if c.is_valid():
            print('---------------------->',c)
            c.save()
            return HttpResponse('''<script>alert ("Data saved successfully");window.location= "/manage_courses"</script>''')
        
class vieweditmanagecourses(View):
    def get(self, request):
        return render(request, 'administrator/viewedit_managecourses.html')
    
    
class viewaddmanagefaculty(View):
    def get(self, request):
        c = department_model.objects.all()
        return render(request, 'administrator/viewadd_managefaculties.html', {'data': c})
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