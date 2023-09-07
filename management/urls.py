from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name='index'),  #Student and Everone Dashboard Start
    path('students/',views.students, name='students'),
    path('teachers/',views.teachers, name='teachers'),
    path('teachers-details/',views.teachers_details, name='teachers-details'),
    path('CSA/',views.CSA, name='CSA'),
    path('agreeculture/',views.agreeculture, name='agreeculture'),
    path('pharmacy/',views.pharmacy, name='pharmacy'),
    path('holiday/',views.holiday, name='holiday'),   
    path('fees/',views.fees, name='fees'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('update/',views.update_profile, name='update-profile'),      #Student and Everone Dashboard End
    path('forgot-password/',views.forgot_password, name='forgot-password'),  #Comman Field Start
    path('otp/',views.otp, name='otp'),
    path('update-password/',views.update_password, name='update-password'),
    path('update/',views.update_profile, name='update-profile'),  #Comman Field End
    
    path('teacher/',views.teacher_index, name='teacher'),
    path('student-list/',views.student_list, name='student-list'),   #student Operations
    path('HOD-student-list.html/',views.student_list, name='HOD-student-list.html'),
    path('add-student/',views.add_student, name='add-student'),
    path('view-student-list', views.view_student_list, name='view-student-list'), #before edit student whose student is edit
    path('edit-student/<int:pk>/',views.edit_student, name='edit-student'),
    path('HOD/',views.HOD_index, name='HOD'),       #HOD
    path('delete/<int:pk>', views.delete_member, name="delete-member"),
    # Teacher Operations BY Hod Pannel
    path('teacher-list',views.teacher_list, name='teacher-list'),
    path('add-teacher',views.add_teacher, name='add-teacher'),
    path('view-teacher-list',views.view_teacher_list, name='view-teacher-list'),
    
    


    
]
