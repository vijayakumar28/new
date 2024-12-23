from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    EMPLOYMENT_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Intern'),
    ]
    
    # Fields for the employee model
    full_name = models.CharField(max_length=255)
    dob = models.DateField()  # Date of Birth
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    employment_type = models.CharField(max_length=2, choices=EMPLOYMENT_TYPE_CHOICES)

    def __str__(self):
        return self.full_name
        

class Comment(models.Model):
    message = models.TextField()

    def __str__(self):
        return str(self.id)
