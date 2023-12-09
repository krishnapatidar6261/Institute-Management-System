from django.db import models

# Create your models here.
class User(models.Model):
    choice=(
        ('teacher','teacher'),
        ('student','student'),
        ('HOD',"HOD"),
    )
    br=(
        ('CSA','CSA'),
        ('agreeculture','agreeculture'),
        ('pharmacy','pharmacy'),
    )
    
    fname=models.CharField( max_length=50)
    lname=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    email=models.EmailField()
    profile_pic=models.ImageField(upload_to='profile_pic/',default="usericon.jpg")
    user_type=models.CharField(max_length=50, default="student", choices=choice)
    dob=models.CharField(max_length=100)
    gender=models.CharField(max_length=50, default="Others")
    mobile=models.PositiveIntegerField(default=0)
    father_name=models.CharField( max_length=50,null=True,blank=True)
    father_occu=models.CharField( max_length=50,null=True,blank=True)
    mother_name=models.CharField( max_length=50,null=True,blank=True)
    mother_occu=models.CharField( max_length=50,null=True,blank=True)
    femail=models.EmailField(null=True,blank=True)
    fmobile=models.PositiveIntegerField(null=True,blank=True,default=0)
    present_addr=models.CharField( max_length=50,null=True,blank=True)
    permanent_addr=models.CharField( max_length=50,null=True,blank=True)
    branch=models.CharField(max_length=50, choices=br)
    
    def __str__(self):
        
        return self.email
    
    
class Holiday(models.Model):
    holiday_name=models.CharField(max_length=50)
    holiday_type=models.CharField(max_length=50)
    start_date=models.CharField(max_length=50)
    end_date=models.CharField(max_length=50)
    
    def __str__(self):
        return self.start_date+" "+self.holiday_name