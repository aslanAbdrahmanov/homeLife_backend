from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Регистрация успешна"})

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username=username, password=password)

        if user:
            redirect_to = "admin_panel" if user.is_staff else "main_page"
            return Response({"message": "Успешный вход", "redirect": redirect_to})
        else:
            return Response({"error": "Неверный username или пароль"}, status=status.HTTP_400_BAD_REQUEST)