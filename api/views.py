from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.
#Registration 

class RegisterUserView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class = ProfileSerializer 

class LoginUserView(TokenObtainPairView):
    pass

class ProtectedView(APIView):
    permission_class = [IsAuthenticated]
    def get(self,request):
        return Response({"message":"This is a protected Resource!"})