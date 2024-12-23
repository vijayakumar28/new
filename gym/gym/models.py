from django.db import models

class product(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    product_type=models.CharField(max_length=100,null=True)
    price=models.FloatField(default=0)
    
    food_product=models.BooleanField(default=False)

    def __str__(self):
        return self.product_name + " "+ self.product_type
    
class membership(models.Model):
        
        PACKAGE_CHOICES = [
        ('basic', 'Basic Package'),
        ('premium', 'Premium Package'),
        ('vip', 'VIP Package'),
        ]
        month_choices=[('one month','one'),
                       ('three month','Three'),
                       ('six month','six'),
                       ('twelve month','twelve')                       
                       ]
        name=models.CharField(max_length=100,null=True)
        age=models.IntegerField(default=0)
        package = models.CharField(max_length=10, choices=PACKAGE_CHOICES, default='basic')
        months = models.CharField(max_length=12, choices=month_choices, default='one')

        Strength_Training=models.BooleanField(default=False)
        Cardio=models.BooleanField(default=False)
        Yoga=models.BooleanField(default=False)
        Zumba=models.BooleanField(default=False)
        HIIT=models.BooleanField(default=False)
        Functional_Training=models.BooleanField(default=False)
        def __str__(self):
            return f"{self.name} - {self.package}"




