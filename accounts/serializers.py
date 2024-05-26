from rest_framework import serializers
from .models import SignupForm, SignInForm

class SignupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignupForm
        fields = ['email', 'firstname', 'lastname', 'mobilenumber', 'createpassword']

class SignInFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignInForm
        fields = ['identifier', 'password']