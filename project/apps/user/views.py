from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import SignUpSerializer, UserSerializer, MyTokenObtainPairSerializer


class SignUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        refresh_token = RefreshToken.for_user(user)

        return Response(
            {'user_token': str(refresh_token.access_token),
             'refresh': str(refresh_token)},
            status=status.HTTP_201_CREATED
        )

class Login(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh = request.data['refresh']
            RefreshToken(refresh).blacklist()
            return Response(
                {'message': 'logout'},
                status=status.HTTP_200_OK
            )
        except (KeyError, TokenError):
            return Response(
                {'message': 'Logout failed'},
                status=status.HTTP_400_BAD_REQUEST
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
