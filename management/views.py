from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.

def index(request):
    return render(request,'index.html')

def students(request):
    return render(request,'students.html')

def teachers(request):
    return render(request,'teachers.html')

def HOD_index(request):
    return render(request,'HOD.html')


def teachers_details(request):
    return render(request,'teachers-details.html')


def CSA(request):
    return render(request,'CSA.html')

def agreeculture(request):
    return render(request,'agreeculture.html')

def pharmacy(request):
    return render(request,'pharmacy.html')

def holiday(request):
        user=User.objects.get(email=request.session['email'])
        holiday=Holiday.objects.all().order_by('-id')
        if user.user_type=="student":
            return render(request,'holiday.html',{'holiday':holiday})
        elif user.user_type=="teacher":
            return render(request,'teacherHoliday.html',{'holiday':holiday})
        else:
            return render(request,'HOD-Holiday.html',{'holiday':holiday})
def fees(request):
    user=User.objects.get(email=request.session['email'])
    if user.user_type=="student":
        return render(request,'fees.html')
    else:
        return render(request,'teacher-fees.html')


def login(request):
    if request.method=="POST":
        if request.POST['email']=="" or request.POST['password']=="":
           
            msg="Please Enter User and Password"
            return render(request,'login.html',{'msg':msg})
        
        else:
            try:
                user=User.objects.get(email=request.POST['email'])
                if user.password==request.POST['password']:
                    if user.user_type=="student":
                        request.session['email']=user.email
                        request.session['fname']=user.fname
                        request.session['user_type']=user.user_type
                        request.session['profile_pic']=user.profile_pic.url
                        request.session['branch']=user.branch

                        return render(request,'index.html')
                    elif user.user_type=="teacher":
                        request.session['email']=user.email
                        request.session['fname']=user.fname
                        request.session['user_type']=user.user_type
                        request.session['branch']=user.branch
                        request.session['profile_pic']=user.profile_pic.url
                        return render(request,'teacher-index.html')
                    else:
                        request.session['email']=user.email
                        request.session['fname']=user.fname
                        request.session['user_type']=user.user_type
                        request.session['branch']=user.branch
                        request.session['profile_pic']=user.profile_pic.url
                        return render(request,'HOD.html')
                else:
                    msg="Incorrect User Or Password"
                    return render(request,'login.html',{'msg':msg})
            except:
                msg="Email Not Register"
                return render(request,'login.html',{'msg':msg})
            
    else:
        return render(request,'login.html')
    
def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            subject = 'Email For Forgot Password'
            otp=random.randint(1000,9999)
            message = "Hello "+ user.fname+" Your Forgot Password OTP is "+ str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            
            msg="OTP Send Successfully"
            return render(request,'otp.html',{'msg':msg,'email':user.email,'otp':otp})
        except:
            msg="Email Not Register"
            return render(request,'forgot-password.html',{'msg':msg})
    
    else:
        return render(request,'forgot-password.html')
    
def otp(request):
    if request.method=="POST":
        email=request.POST['email']
        otp=request.POST['otp']
        uotp=request.POST['uotp']
        if otp==uotp:
           
            return render(request,'update-password.html',{'email':email})
        else:
            msg="Incorret OTP"
            return render(request,'otp.html',{'msg':msg,'email':email,'otp':otp})
        
def update_password(request):
    email=request.POST['email']
    if request.method=="POST":
       
        if request.POST['new_pwd']==request.POST['cnew_pwd']:
            user=User.objects.get(email=email)
            user.password=request.POST['new_pwd']
            user.save()
            msg="Password Updated Successfully"
            return render(request,'login.html',{'msg':msg})
        
        else:
            msg="Password and confirm Password Does Not Matched"
            return render(request,'update-password.html',{'msg':msg,'email':email})
            
    else:
        return render(request,'update-password.html')
    
        

def update_profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.gender=request.POST['gender']
        user.mobile=request.POST['mobile']
        user.father_name=request.POST['father_name']
        user.femail=request.POST['femail']
        user.fmobile=request.POST['fmobile']
        user.father_occu=request.POST['father_occu']
        user.mother_name=request.POST['mother_name']
        user.mother_occu=request.POST['mother_occu']
        user.present_addr=request.POST['present_addr']
        user.permanent_addr=request.POST['permanent_addr']
        
        try:
            user.profile_pic=request.FILES['profile_pic']
            user.dob=request.POST['dob']
        except Exception as e:
           pass
        user.save()
        request.session['profile_pic']=user.profile_pic.url
        msg="Profile Updated Successfully"
        return render(request,'update-profile.html',{'user':user,'msg':msg})
       
                
    else:
        return render(request,'update-profile.html',{'user':user})

def logout(request):
    
    try:
        del request.session['email']
        del request.session['profile_pic']
        del request.session['fname']
        del request.session['branch']
        del request.session.user_type['user_type']
        
        return redirect('login')
    except:
        return redirect('login')


def teacher_index(request):
    return render(request,'teacher-index.html')

def student_list(request):
    user=User.objects.get(email=request.session['email'])
    student=User.objects.filter(branch=request.session['branch'],user_type='student')
    if user.user_type=='teacher':
        return render(request,'student-list.html',{'student':student})
    else:
        return render(request,'HOD-student-list.html',{'student':student})


def add_student(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Register"
            if user.user_type=="teacher":
                return render(request,'add-student.html',{'msg':msg})
            else:
                return render(request,'HOD-add-student.html',{'msg':msg})
                            
        except:
            if request.POST['password']==request.POST['cpassword']:
                fmobile=0
                mobile=0
                try:
                     fmobile=int(request.POST['fmobile'])
                except :
                    pass
                try:
                     mobile=int(request.POST['mobile'])
                except :
                    pass
                User.objects.create(
                    fname=request.POST['fname'],    
                    lname=request.POST['lname'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                    profile_pic=request.FILES['profile_pic'],
                    dob=request.POST['dob'],
                    gender=request.POST['gender'],
                    father_name=request.POST['father_name'],
                    father_occu=request.POST['father_occu'],
                    mother_name=request.POST['mother_name'],
                    mother_occu=request.POST['mother_occu'],
                    femail=request.POST['femail'],
                    present_addr=request.POST['present_addr'],
                    permanent_addr=request.POST['permanent_addr'],
                    branch=user.branch,
                    fmobile=fmobile,
                    mobile=mobile
                    )
                msg="Student Added Successfully"
                if user.user_type=="teacher":
                    return render(request,'add-student.html',{'msg':msg})
                else:
                    return render(request,'HOD-add-student.html',{'msg':msg})

                
            else:
                msg="Password and Confirm Password Does Not Matched"
                if user.user_type=="teacher":
                    return render(request,'add-student.html',{'msg':msg})
                else:
                    return render(request,'HOD-add-student.html',{'msg':msg})
                        
    else:
        if user.user_type=="teacher":
            return render(request,'add-student.html')
        else:
            return render(request,'HOD-add-student.html')

    
def view_student_list(request):                     #Edit Student Start
    user=User.objects.get(email=request.session['email'])
    student=User.objects.filter(branch=request.session['branch'], user_type='student')
    if user.user_type=="teacher":
        return render(request,'view-student-list.html',{'student':student})
    else:
        return render(request,'HOD-ViewStudentList.html',{'student':student})


def edit_student(request,pk):
    student=User.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])    
    if request.method=="POST":
        student.fname=request.POST['fname']
        student.lname=request.POST['lname']
        student.email=request.POST['email']
        student.dob=request.POST['dob']
        student.gender=request.POST['gender']
        student.mobile=request.POST['mobile']
        student.father_name=request.POST['father_name']
        student.father_occu=request.POST['father_occu']
        student.mother_name=request.POST['mother_name']
        student.mother_occu=request.POST['mother_occu']
        student.femail=request.POST['femail']
        student.fmobile=request.POST['fmobile']
        student.present_addr=request.POST['present_addr']
        student.permanent_addr=request.POST['permanent_addr']
        try:
            student.profile_pic=request.FILES['profile_pic']
        except:
            pass
        student.save()
        msg="Update Successfully"
        if user.user_type=="teacher":
            return render(request,'edit-student.html',{'student':student,'msg':msg}) #edit student end
        else:
            return render(request,'HOD-edit-student.html',{'student':student,'msg':msg})
        
    else:
        if user.user_type=="teacher":
            return render(request,'edit-student.html',{'student':student}) #edit student end
        else:
            return render(request,'HOD-edit-student.html',{'student':student}) #edit student end

            
def delete_member(request,pk):
    user=User.objects.get(email=request.session['email'])
    member=User.objects.get(pk=pk)
    member.delete()
    if user.user_type=="teacher":
        return redirect('student-list')
    else:
        return redirect('student-list')
    
def teacher_list(request):
    teacher=User.objects.filter(user_type="teacher",branch=request.session['branch'])
    return render(request,'teacher-list.html',{'teacher':teacher})

def add_teacher(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Register"
            return render(request,'add-teacher.html',{'msg':msg})
                            
        except:
            if request.POST['password']==request.POST['cpassword']:
                fmobile=0
                mobile=0
                try:
                     fmobile=int(request.POST['fmobile'])
                except :
                    pass
                try:
                     mobile=int(request.POST['mobile'])
                except :
                    pass
                User.objects.create(
                    fname=request.POST['fname'],    
                    lname=request.POST['lname'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                    profile_pic=request.FILES['profile_pic'],
                    dob=request.POST['dob'],
                    gender=request.POST['gender'],
                    father_name=request.POST['father_name'],
                    father_occu=request.POST['father_occu'],
                    mother_name=request.POST['mother_name'],
                    mother_occu=request.POST['mother_occu'],
                    femail=request.POST['femail'],
                    present_addr=request.POST['present_addr'],
                    permanent_addr=request.POST['permanent_addr'],
                    branch=user.branch,
                    fmobile=fmobile,
                    mobile=mobile,
                    user_type="teacher",
                    )
                msg="Teacher Added Successfully"
                return render(request,'add-teacher.html',{'msg':msg})
                          
            else:
                msg="Password and Confirm Password Does Not Matched"
                return render(request,'add-teacher.html',{'msg':msg})
                        
    else:
        return render(request,'add-teacher.html')


def view_teacher_list(request):
    teacher=User.objects.filter(branch=request.session['branch'],user_type="teacher")
    return render(request,'view-teacher-list.html',{'teacher':teacher})


