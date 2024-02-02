
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
# accounts/views.py

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSignUpSerializer, UserSignInSerializer

from .forms import CustomUserCreationForm

@api_view(['POST'])
def user_signup(request):
    if request.method == 'POST':
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User signed up successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_signin(request):
    if request.method == 'POST':
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                # Perform additional actions if authentication is successful
                return Response({'message': 'User signed in successfully'}, status=status.HTTP_200_OK)
            return Response({'message': 'Unable to log in with provided credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to sign-in page after successful sign-up
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Perform authentication and login if valid
            return redirect('home')  # Redirect to home page after successful sign-in
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

