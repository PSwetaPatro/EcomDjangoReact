from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SignupForm, SignInForm
from .serializers import SignupFormSerializer, SignInFormSerializer

class SignupFormviewSet(viewsets.ModelViewSet):
    queryset = SignupForm.objects.all()
    serializer_class = SignupFormSerializer

@api_view(['POST'])
def sign_up_Form(request):
    if request.method == 'POST':
        serializer = SignupFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignInFormViewSet(viewsets.ModelViewSet):
    queryset = SignInForm.objects.all()
    serializer_class = SignInFormSerializer

@api_view(['POST'])
def sign_in_form(request):
    if request.method == 'POST':
        serializer = SignInFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)