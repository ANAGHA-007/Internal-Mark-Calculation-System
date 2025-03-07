
from django.urls import include, path # type: ignore

from .views import *

urlpatterns = [
   path('', Login.as_view(), name='login'),
   path('logout', Logout.as_view(), name='logout'),
   path('adminhome', Adminhome.as_view(), name='adminhome'),
   path('institution_details', institutiondetails.as_view(), name='institution_details'),
   path('manage_courses', managecourses.as_view(), name='manage_courses'),
   path('manage_student', managestudents.as_view(), name='manage_student'),
   path('manage_faculties', managefaculty.as_view(), name='manage_faculties'),
   path('addsubject',AddSubject.as_view(),name='addsubject'),
   path('managesubject',managesubject.as_view(),name='managesubject'),
   path('editsubject/<int:id>', Edit_Subject.as_view(), name='editsubject'),
   path('deletesub/<int:id>', Delete_Subject.as_view(), name='deletesub'),
   path('manage_program', manageprograms.as_view(), name='manage_program'),
   path('notification', notification.as_view(), name='notification'),
   path('view_addstudents', viewaddstudent.as_view(), name='view_addstudents'),
   path('get_departments/', get_departments, name='get_departments'),
    path('get_courses/', get_courses, name='get_courses'),
    path('get_semesters/', get_semesters, name='get_semesters'),
   path('get-departments/', GetDepartments.as_view(), name='get_departments'),  # AJAX UR
   path('view_editstudents/<int:id>', vieweditstudents.as_view(), name='view_editstudents'),
   path('view_institution_details', view_institutiondetails.as_view(), name='view_institution_details'),
   path('viewadd_managecourses', viewaddmanagecourses.as_view(), name='viewadd_managecourses'),
   path('viewedit_managecourses', vieweditmanagecourses.as_view(), name='viewedit_managecourses'),
   path('viewadd_managefaculties', viewaddmanagefaculty.as_view(), name='viewadd_managefaculties'),
   path('get_depts/', get_depts, name='get_departments'),
   path('viewedit_managefaculties/<int:id>', vieweditmanagefaculty.as_view(), name='viewedit_managefaculties'),
   path('viewadd_manageprogram', viewaddmanageprogram.as_view(), name='viewadd_manageprogram'),
   path('viewedit_manageprogram', vieweditmanageprogram.as_view(), name='viewedit_manageprogram'),
   path('componenty and weightage', componentsandweightage.as_view(), name='componenty and weightage'),
   path('entermark', entermark.as_view(), name='entermark'),
   path('facultyfunction', facultyfunction.as_view(), name='facultyfunction'),
   path('facultyhome', facultyhome.as_view(), name='facultyhome'),
   path('report', report.as_view(), name='report'),
   path('viewreport', viewreport.as_view(), name='viewreport'),
   path('viewnotification', viewnotification.as_view(), name='viewnotification'),
   path('deletenot/<int:id>', DeleteNotification.as_view(), name='deletenot'),
   path('deleteint/<int:id>', DeleteInst.as_view(), name='deleteint'),
   path('editint/<int:id>', EditInst.as_view(), name='editint'),
   path('deletepgm/<int:id>', deleteprgm.as_view(), name='deletepgm'),
   path('editpgm/<int:id>', editprgm.as_view(), name='editpgm'),
   path('deletecourse/<int:id>', deletecourse.as_view(), name='deletecourse'),
   path('editcourse/<int:id>', editcourse.as_view(), name='editcourse'),
   path('deletefac/<int:id>', DeleteFac.as_view(), name='deletefac'),
   path('deletestu/<int:id>', deletestudent.as_view(), name='deletestu'),
   path('notification', notification.as_view(), name='notification'),
   path('managesemester', Manage_Semester.as_view(), name='managesemester'),
   path('addsemester', Add_Semester.as_view(), name='addsemester'),
   path('deletesemester/<int:id>', Delete_Semester.as_view(), name='deletesemester'),
   path('editsemester/<int:id>/', EditSemester.as_view(), name='editsemester'),
   path('Login_serializer',LoginAPIView.as_view(),name='Login_serializer'),
   path('Institution_serializer',InstitutionAPIView.as_view(),name='Institution_serializer'),
   path('Department_serializer',DepartmentAPIView.as_view(),name='Department_serializer'),
   path('Faculty_serializer', FacultyAPIView.as_view(),name=' Faculty_serializer'),
   path('Course_serializer',CourseAPIView.as_view(),name='Course_serializer'),
   path('Sem_serializer',SemAPIView.as_view(),name='Sem_serializer'),
   path('Subject_serializer',SubjectAPIView.as_view(),name='Subject_serializer'),
   path('Exam_serializer',ExamAPIView.as_view(),name='Exam_serializer'),
   path('Student_serializer',StudentAPIView.as_view(),name='Student_serializer'),
   path(' Mark_serializer',MarkAPIView.as_view(),name=' Mark_serializer'),
   path('Grievances_model.objects',GrievancesAPIView.as_view(),name='Grievances_model.objects'),
   path('NotificationSerializer',NotificationAPIView.as_view(),name='NotificationSerializer'),
   
   path('departments/', DepartmentListAPIView.as_view(), name='department-list'),   
   path('LoginPage',LoginAPIView.as_view(),name='LoginPage'),
   path('addmarks',MarkAPIView.as_view(),name='MarkAPIView'),
   path('coursewise',CourseAPIView.as_view(),name='CourseAPIView'),
   path('editmark',MarkAPIView.as_view(),name='MarkAPIView'),
   path('feedback',GrievancesAPIView.as_view,name='GrievancesAPIView'),
   path('getapproval',GrievancesAPIView.as_view,name='GrievancesAPIView'),
   
   path('getstudentbysemcodep/<int:sem>/<int:co>/<int:dep>',getstudentbysemcodep.as_view(),name='getstudentbysemcodep'),
   path('marks/', MarkAPIView.as_view(), name="mark-list-create"),
   path('marks/<int:pk>/', MarkAPIView.as_view(), name="mark-detail"),
   path('getmarksofstudents/<int:student_id>/', StudentsMarkAPIView.as_view(), name="mark-detail"),
   
   
   path('feedback/', FeedbackAPIView.as_view(), name='feedback-list'),
   path('feedback/<int:pk>/', FeedbackAPIView.as_view(), name='feedback-detail'),
   
   path('feedbackoffaculty/<int:pk>/', FeedbackoffacultyAPIView.as_view(), name='feedback-detail'),
   
   path('ViewSubjectsApi/<int:lid>/', ViewSubjectsApi.as_view(), name='ViewSubjectsApi'),
   path('ViewFacultyApi/<int:lid>/', ViewFacultyApi.as_view(), name='ViewFacultyApi'),
   
   
   
   
]
