from django.shortcuts import render

from rest_framework.views import APIView

from user.models import User,StudentProfile

from user.serializers import UserSerializer

from rest_framework.generics import CreateAPIView

class RegisterView(CreateAPIView):

    serializer_class = UserSerializer


class LoginCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)



