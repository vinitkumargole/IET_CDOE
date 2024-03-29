from email.mime import image
from re import template
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

class Slide(models.Model):
    image = models.ImageField(upload_to='images/slides/')

class Index(models.Model):
    #home section
    slides = models.ManyToManyField(Slide)
    welcome_header=models.CharField(max_length=200)
    slider_text=models.CharField(max_length=200)
    about_head=models.CharField(max_length=200)
    about_body=models.TextField(null=False,blank=False)
    header_image=models.ImageField(null=True ,upload_to='images/index/')
    fb_link=models.URLField()
    twitter_link=models.URLField()
    insta_link=models.URLField()
    address=models.TextField()
    map_link=models.URLField(max_length=200)
    contact_num=models.CharField(max_length=12)
    email_id=models.EmailField() 

# class Program(models.Model):
#     program_id=models.CharField(max_length=200)
#     program_name=models.CharField(max_length=200)
#     description=models.TextField(null=True,blank=True)
#     eligibility=models.CharField(max_length=200)
#     updated=models.DateTimeField(auto_now=True)
#     created=models.DateTimeField(auto_now_add=True)
#     Syllabus=models.TextField(null=True,blank=True)
#     Program_objective=models.TextField(null=True,blank=True)
#     Course_objective=models.TextField(null=True,blank=True)
#     fees=models.CharField(max_length=200)
#     apply_now=models.CharField(max_length=200)
class Faculty(models.Model):

    name = models.CharField(max_length=100, blank=False)
    post = models.CharField(max_length=100, blank=False)
    linked_in = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    

    def __str__(self) :
        return (self.name)
class Programs(models.Model):
    program_id=models.CharField(max_length=100)
    program_name=models.CharField(primary_key='True',max_length=200)
    def __str__(self):
        return (self.program_name) 
class course_type(models.Model):
    type_id=models.CharField(max_length=100)
    course_type=models.CharField(primary_key='True',max_length=200)
    def __str__(self):
        return (self.course_type) 

class course_head(models.Model):
    course_id=models.CharField(max_length=100)  
    program_name=models.ForeignKey(Programs,on_delete=models.CASCADE)
    course_name=models.CharField(primary_key='True',max_length=200)
    card_image=models.ImageField(upload_to='images/course_image/',null=True)
    course_type=models.ForeignKey(course_type,on_delete=models.CASCADE)
    def __str__(self):
        return (self.course_name)
class course_categories(models.Model):
    category_id=models.CharField(max_length=100)
    category_name=models.CharField(primary_key='True',max_length=200)
    def __str__(self):
        return (self.category_name)
class course_details(models.Model):
    course_name=models.ForeignKey(course_head,on_delete=models.CASCADE)
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    display_title=models.CharField(max_length=200)
    category=models.ForeignKey(course_categories,on_delete=models.CASCADE)
    display_image=models.ImageField(upload_to='images/course_image/display_images/')
    def __str__(self):
        return (self.course_name.course_name)
    

class Announcement(models.Model):

    title = models.CharField(max_length=100, blank=False)
    link = models.URLField(blank=False)
    new = models.BooleanField(default=True)

    def __str__(self) :
        return (self.title)

class Notice(models.Model):

    subject = models.CharField(max_length=200, blank=False)
    date = models.DateField(auto_now=True)
    attachement = models.URLField(blank=False)

    def __str__(self) :
        return (self.subject)



class ComingSoonMailList(models.Model):

    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    template = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")
    
    def send(self, request):
        # contents = str(self.template.read().decode('utf-8'))
        subscribers = ComingSoonMailList.objects.all()
        response_email = render_to_string(self.template.name)
        for sub in subscribers:
            mail = EmailMultiAlternatives(self.subject, response_email, settings.EMAIL_HOST_USER, [sub.email])
            mail.content_subtype = 'html'
            mail.send()

