from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    EMPLOYMENT_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Intern'),
    ]
    
    # 1. Full Name
    full_name = models.CharField(max_length=255)
    
    # 2. Date of Birth
    dob = models.DateField()  # Date of Birth
    
    # 3. Gender
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # 4. Marital Status
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    
    # 5. Employee ID
    employee_id = models.CharField(max_length=20, unique=True)
    
    # 6. Department
    department = models.CharField(max_length=100)
    
    # 7. Position
    position = models.CharField(max_length=100)
    
    # 8. Contact Number
    contact_number = models.CharField(max_length=15)
    
    # 9. Email Address
    email = models.EmailField()
    
    # 10. Date of Joining
    date_of_joining = models.DateField()

    def __str__(self):
        return self.full_name
