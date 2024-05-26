from django.db import models

class SignupForm(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobilenumber = models.CharField(max_length=10)
    createpassword = models.CharField(max_length=50)  # Replace with Django's User model for real apps

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.email})"

class SignInForm(models.Model):
    identifier = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  # Note: In a real app, handle passwords securely

    def __str__(self):
        return self.identifier