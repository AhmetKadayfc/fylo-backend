from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer
from .admin import CreateUserForm
from .models import User


class UserDetail(APIView):
    '''
    User class-based api detail view
    '''
    permission_classes = [IsAuthenticated, ]

    def get(sefl, request):
        user = UserSerializer(request.user)
        return Response(user.data, status=status.HTTP_200_OK)


class RegisterView(APIView):
    '''
    Register class_based view
    '''
    queryset = User.object.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        user = JSONParser().parse(request)
        form = CreateUserForm(user)

        if form.is_valid():
            form.save()
            return Response(form.data, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class BlackListTokenView(APIView):
    '''
    Blacklists the previously created token of the logged out user(logout)
    '''

    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = ResfreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
