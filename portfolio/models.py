from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class Blogs(models.Model):
    title=models.CharField(max_length=60)
    descriptions= models.TextField(default='')
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Internship(models.Model):
    fullname=models.CharField(max_length=60)
    usn= models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    college_name=models.CharField(max_length=60)
    offer_status=models.CharField(max_length=60)
    start_date=models.CharField(max_length=60)
    end_date=models.CharField(max_length=60)
    project_report=models.CharField(max_length=60)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usn
