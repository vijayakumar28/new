from django.db import models

class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()  # Normalize state names
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True, default="Unknown City")
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)  # Make 'state' nullable

    def save(self, *args, **kwargs):
        self.name = self.name.strip().title()  # Normalize city names
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Property(models.Model):
    property_id = models.CharField(max_length=32, primary_key=True,)
    property_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)  # Link to City
    address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True,unique=True)
    owner_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.property_name
