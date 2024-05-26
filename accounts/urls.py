from django.urls import path, include
from rest_framework import routers
from .views import SignupFormviewSet, sign_up_Form
from .views import SignInFormViewSet, sign_in_form


router = routers.DefaultRouter()
router.register(r'signupform', SignupFormviewSet)
router.register(r'signinform', SignInFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/sign_up_Form/', sign_up_Form, name='sign_up_Form'),
     path('api/sign_in_form/', sign_in_form, name='sign_in_form'),
]
