from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address= models.CharField(max_length=40)
    dob = models.DateField()




class Student(models.Model):
    name = models.CharField(max_length=40)
    fees = models.FloatField()
    dept = models.CharField(max_length=40)
    #courses
    class Meta:
        db_table = 'STUDENT_MASTER'


class Course(models.Model):
    name = models.CharField(max_length=40)
    sfees = models.FloatField()
    author = models.CharField(max_length=40)
    students = models.ManyToManyField(Student,related_name='courses')

    class Meta:
        db_table = 'COURSE_MASTER'


class Address(models.Model):
    city = models.CharField(max_length=40)
    pincode = models.IntegerField()
    state = models.CharField(max_length=40)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='addresses')

    class Meta:
        db_table = 'ADDRESS_MASTER'

class Professors(models.Model):
    name = models.CharField(max_length=40)
    salary = models.FloatField()
    skill = models.CharField(max_length=40)
    students = models.ManyToManyField(Student, related_name='professors')
    college = models.ForeignKey('College',on_delete=models.CASCADE,related_name='professors')

    class Meta:
        db_table = 'PROFESSOR_MASTER'

class College(models.Model):
    name = models.CharField(max_length=40)
    startdate = models.DateField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE)

    class Meta:
        db_table = 'COLLEGE_MASTER'