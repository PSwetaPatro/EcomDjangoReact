from django.contrib import admin
from .models import SignupForm, SignInForm


@admin.register(SignupForm)
class SignupFormAdmin(admin.ModelAdmin):
    list_display = ['email', 'firstname', 'lastname', 'mobilenumber', 'createpassword']
    search_fields = ['email', 'firstname', 'lastname', 'mobilenumber']


@admin.register(SignInForm)
class SignInFormAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'password']
    search_fields = ['identifier']