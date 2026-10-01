from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate

from .serializers import SignUpSerializer, LoginSerializer, UserSerializer


class SignUp(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token, _= Token.objects.get_or_create(user=user) # "_" отвечает за получение существующего токена
        return Response(
            {'user_token': token.key},
            status=status.HTTP_201_CREATED
        )

class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response(
                {'password': 'Login failed'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {'user_token': token.key},
            status=status.HTTP_200_OK
        )

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(
            {'message': 'logout'},
            status=status.HTTP_200_OK
        )

class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(
            {'user': serializer.data},
            status=status.HTTP_200_OK
        )
    def patch(self,request):
        serializer=UserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'data updated successfully'},
            status=status.HTTP_200_OK
        )
